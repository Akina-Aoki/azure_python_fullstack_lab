"""
Filesystem paths used by the eclipse backend."
"""

from pathlib import Path
# AI-assisted refactor: resolve data paths from this file, not the shell's cwd.
BACKEND_DIR = Path(__file__).resolve().parents[2]
TRANSFORMED_DATA_DIR = BACKEND_DIR / "data" / "transformed"
SOLAR_DATA_PATH = TRANSFORMED_DATA_DIR / "solar.csv"
LUNAR_DATA_PATH = TRANSFORMED_DATA_DIR / "lunar.csv"