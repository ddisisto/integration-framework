"""Write version from git describe into Quarto files."""

import subprocess
from pathlib import Path

here = Path(__file__).parent

version = subprocess.check_output(
    ["git", "describe", "--tags", "--always"],
    cwd=here,
    text=True,
).strip()

# Quarto metadata and LaTeX macro
(here / "_version.yml").write_text(f'version: "{version}"\n')
(here / "_version.tex").write_text(f"\\newcommand{{\\version}}{{{version}}}\n")

print(f"_version → {version}")
