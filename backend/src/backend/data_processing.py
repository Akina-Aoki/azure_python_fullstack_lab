"""
Load and filter the transformed Solar and Lunar eclipse datasets.

This module:

1. Loads the transformed CSV files into Pandas DataFrames.
2. Filters Solar eclipse data by year or category.
3. Filters Lunar eclipse data by year or category.
"""

import pandas as pd

# Import the paths to the transformed Solar and Lunar CSV files.
from backend.constants import LUNAR_DATA_PATH, SOLAR_DATA_PATH

# application only loads transformed data and applies the two dashboard filters.
solar_eclipses = pd.read_csv(SOLAR_DATA_PATH)
lunar_eclipses = pd.read_csv(LUNAR_DATA_PATH)



# ============================================================
# SOLAR ECLIPSE FILTERS
# ============================================================


def filter_solar_by_year(year: int) -> pd.DataFrame:
    """Return Solar eclipses in the requested year."""
    # Keep rows where the Year column matches the requested year.
    return solar_eclipses[solar_eclipses["Year"] == year]



def filter_solar_by_category(eclipse_category: str) -> pd.DataFrame:
    """Return Solar eclipses in the requested category."""
    # Keep rows where Eclipse Category matches the requested category.
    return solar_eclipses[
        solar_eclipses["Eclipse Category"] == eclipse_category
    ]


def filter_lunar_by_year(year: int) -> pd.DataFrame:
    """Return Lunar eclipses in the requested year."""
    return lunar_eclipses[lunar_eclipses["Year"] == year]


def filter_lunar_by_category(eclipse_category: str) -> pd.DataFrame:
    """Return Lunar eclipses in the requested category."""
    return lunar_eclipses[
        lunar_eclipses["Eclipse Category"] == eclipse_category
    ]