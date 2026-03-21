"""Generate figures for §3 from autoloop data exports."""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import Normalize, LinearSegmentedColormap
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# Color map: low surprisal (degrading) = cool slate, high surprisal (enriching) = warm amber
CMAP = LinearSegmentedColormap.from_list("regime", [
    (0.0, "#2b5278"),   # zero surprisal — deep basin, no compressive novelty
    (0.15, "#8ba4b8"),  # low surprisal — mildly degrading
    (0.4, "#e8e8e0"),   # moderate — transitional
    (0.65, "#e8a735"),  # elevated — enriching
    (1.0, "#c44e00"),   # high surprisal — strong novelty (or noise)
])


def load(name):
    with open(DATA_DIR / name) as f:
        return json.load(f)


def surprisal_to_color(surprisal, vmax=5.0):
    """Map surprisal to color. Low = cool (degrading), high = warm (enriching)."""
    norm = Normalize(vmin=0, vmax=vmax)
    return CMAP(norm(surprisal))


def auto_vmax(tokens, percentile=97):
    """Pick a color scale max from the token data — clip outliers."""
    vals = sorted(t["surprisal"] for t in tokens)
    idx = min(int(len(vals) * percentile / 100), len(vals) - 1)
    return max(vals[idx] * 1.1, 1.0)  # floor at 1.0 to avoid degenerate scale


def render_tokens(ax, tokens, fontsize=10, chars_per_line=80, color_vmax=5.0):
    """Render tokens as colored text with background patches, wrapping to fit."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fontprops = {"fontsize": fontsize, "fontfamily": "monospace"}
    x_start = 0.03
    max_width = 0.94
    char_w = max_width / chars_per_line
    token_pad = char_w * 0.35       # horizontal breathing room between tokens
    line_h = 0.075                  # vertical spacing between lines

    x = x_start
    y = 1.0 - line_h * 0.6
    chars_on_line = 0

    for tok_data in tokens:
        color = surprisal_to_color(tok_data["surprisal"], vmax=color_vmax)
        display = tok_data["token"].replace("\n", " ")
        token_chars = len(display)
        token_width = token_chars * char_w

        if chars_on_line + token_chars > chars_per_line and chars_on_line > 0:
            x = x_start
            y -= line_h
            chars_on_line = 0
            if y < -0.02:
                break

        pad_y = line_h * 0.08
        patch = mpatches.FancyBboxPatch(
            (x, y - line_h * 0.38 + pad_y),
            token_width, line_h * 0.68,
            boxstyle="round,pad=0.003",
            facecolor=color, edgecolor="none", alpha=0.82,
        )
        ax.add_patch(patch)
        ax.text(x + char_w * 0.05, y, display, va="center", ha="left",
                color="#1a1a1a", **fontprops)

        x += token_width + token_pad
        chars_on_line += token_chars + 1  # +1 accounts for padding in wrap calc

    return y  # return final y so caller knows how much space was used


def render_tokens_multi_window(ax, windows, fontsize=10, chars_per_line=78,
                                tokens_per_window=30, color_vmax=5.0):
    """Render tokens from multiple windows as one stream with vertical ellipsis breaks."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fontprops = {"fontsize": fontsize, "fontfamily": "monospace"}
    x_start = 0.03
    max_width = 0.94
    char_w = max_width / chars_per_line
    token_pad = char_w * 0.35
    line_h = 0.055                  # tighter lines for multi-window (more content)
    ellipsis_v_space = line_h * 1.4  # vertical space for ⋮ marker

    x = x_start
    y = 1.0 - line_h * 0.6
    chars_on_line = 0

    def place_token(display, color):
        nonlocal x, y, chars_on_line
        token_chars = len(display)
        token_width = token_chars * char_w
        if chars_on_line + token_chars > chars_per_line and chars_on_line > 0:
            x = x_start
            y -= line_h
            chars_on_line = 0
            if y < -0.02:
                return False
        pad_y = line_h * 0.08
        patch = mpatches.FancyBboxPatch(
            (x, y - line_h * 0.38 + pad_y),
            token_width, line_h * 0.68,
            boxstyle="round,pad=0.003",
            facecolor=color, edgecolor="none", alpha=0.82,
        )
        ax.add_patch(patch)
        ax.text(x + char_w * 0.05, y, display, va="center", ha="left",
                color="#1a1a1a", **fontprops)
        x += token_width + token_pad
        chars_on_line += token_chars + 1
        return True

    for i, w in enumerate(windows):
        if i > 0:
            # Force new line, draw vertical ellipsis, then new line
            x = x_start
            chars_on_line = 0
            y -= ellipsis_v_space * 0.45
            if y < -0.02:
                break
            ax.text(0.5, y, "⋮", fontsize=10, ha="center", va="center",
                    color="#999999")
            y -= ellipsis_v_space * 0.55
            if y < -0.02:
                break

        tokens = w["tokens"][:tokens_per_window]
        for tok_data in tokens:
            display = tok_data["token"].replace("\n", " ")
            color = surprisal_to_color(tok_data["surprisal"], vmax=color_vmax)
            if not place_token(display, color):
                break

    return y


def add_colorbar(fig, y_bottom, vmax=5.0):
    """Add horizontal colorbar at a specific vertical position."""
    # Place colorbar axes just below the content
    cbar_ax = fig.add_axes([0.15, y_bottom, 0.7, 0.02])
    sm = plt.cm.ScalarMappable(cmap=CMAP, norm=Normalize(vmin=0, vmax=vmax))
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cbar_ax, orientation="horizontal")
    cbar.set_label("← low surprisal (degrading)          surprisal (nats)          high surprisal (enriching) →",
                   fontsize=7)
    cbar.ax.tick_params(labelsize=6)
    return cbar


# ---------------------------------------------------------------------------
# Figure A: Collapse transition
# ---------------------------------------------------------------------------

def figure_a():
    data = load("figure_a_collapse.json")
    windows = data["windows"]
    all_tokens = [t for w in windows for t in w["tokens"][:30]]
    vmax = auto_vmax(all_tokens)

    fig, ax = plt.subplots(1, 1, figsize=(7, 5.0))

    final_y = render_tokens_multi_window(ax, windows, fontsize=9, chars_per_line=80,
                                          tokens_per_window=30, color_vmax=vmax)

    cbar_y = max(final_y * 0.38 + 0.02, 0.06)
    add_colorbar(fig, cbar_y, vmax=vmax)

    fig.subplots_adjust(left=0.03, right=0.97, top=0.97, bottom=0.02)
    return fig


# ---------------------------------------------------------------------------
# Figure B: Coherent prose
# ---------------------------------------------------------------------------

def figure_b():
    data = load("figure_b_tokens.json")
    vmax = auto_vmax(data["tokens"])

    fig, ax = plt.subplots(1, 1, figsize=(7, 2.8))
    final_y = render_tokens(ax, data["tokens"], fontsize=10, chars_per_line=78,
                            color_vmax=vmax)

    cbar_y = max(final_y * 0.35 + 0.02, 0.06)
    add_colorbar(fig, cbar_y, vmax=vmax)

    fig.subplots_adjust(left=0.03, right=0.97, top=0.96, bottom=0.02)
    return fig


# ---------------------------------------------------------------------------
# Figure C: Noise
# ---------------------------------------------------------------------------

def figure_c():
    data = load("figure_c_noise.json")
    vmax = auto_vmax(data["tokens"])

    fig, ax = plt.subplots(1, 1, figsize=(7, 2.8))
    final_y = render_tokens(ax, data["tokens"], fontsize=10, chars_per_line=78,
                            color_vmax=vmax)

    cbar_y = max(final_y * 0.35 + 0.02, 0.06)
    add_colorbar(fig, cbar_y, vmax=vmax)

    fig.subplots_adjust(left=0.03, right=0.97, top=0.96, bottom=0.02)
    return fig


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    out = Path(__file__).parent / "figures"
    out.mkdir(exist_ok=True)

    for name, func in [("figure_a_collapse", figure_a),
                        ("figure_b_tokens", figure_b),
                        ("figure_c_noise", figure_c)]:
        fig = func()
        fig.savefig(out / f"{name}.png", dpi=200, bbox_inches="tight")
        plt.close(fig)
        print(f"  {name}: OK")
