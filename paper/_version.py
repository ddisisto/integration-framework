"""Write version from git describe into Quarto files, README, and CITATION.cff."""

import re
import subprocess
from pathlib import Path

here = Path(__file__).parent
root = here.parent

version = subprocess.check_output(
    ["git", "describe", "--tags", "--always"],
    cwd=here,
    text=True,
).strip()

# Quarto metadata and LaTeX macro
(here / "_version.yml").write_text(f'version: "{version}"\n')
(here / "_version.tex").write_text(f"\\newcommand{{\\version}}{{{version}}}\n")

# README.md — prose and bibtex
readme = root / "README.md"
if readme.exists():
    text = readme.read_text()
    text = re.sub(r"currently v[\d.]+", f"currently {version}", text)
    text = re.sub(r"Living document, v[\d.]+", f"Living document, {version}", text)
    readme.write_text(text)

# CITATION.cff
citation = root / "CITATION.cff"
if citation.exists():
    text = citation.read_text()
    # strip leading v for semver field
    text = re.sub(r'version: "[\d.]+"', f'version: "{version.lstrip("v")}"', text)
    citation.write_text(text)

print(f"_version → {version}")
