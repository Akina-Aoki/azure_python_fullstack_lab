"""
Load and process the Pokémon CSV data.

This module:
1. Reads Pokemon.csv into a Pandas DataFrame.
2. Cleans missing secondary Pokémon types.
3. Calculates how many Pokémon belong to each type.
4. Provides a function for filtering Pokémon by type.
"""

import pandas as pd

# Import the path to the project's data folder.
from backend.constants import DATA_PATH


# ============================================================
# LOAD THE DATA
# ============================================================

# DATA_PATH represents the data folder.
# The / operator from pathlib adds "Pokemon.csv" to that path.
#
# pd.read_csv() reads the CSV file and creates a DataFrame.
# A DataFrame is a table containing rows and columns.
df = pd.read_csv(DATA_PATH / "Pokemon.csv")


# ============================================================
# HANDLE MISSING VALUES
# ============================================================

# Some Pokémon only have one type, so their "Type 2" value is empty.
#
# fillna("missing") replaces those empty values with the word "missing".
# This makes the missing values easier to handle during the calculation.
df["Type 2"] = df["Type 2"].fillna("missing")


# ============================================================
# COUNT POKÉMON BY TYPE
# ============================================================

# Create a Pandas Series containing the total number of Pokémon
# associated with every type.
number_per_type = (
    # value_counts() counts how often each value appears.
    #
    # The first value_counts() counts the primary Pokémon types.
    # The second value_counts() counts the secondary Pokémon types.
    #
    # pd.concat() combines the two results into one Series.
    pd.concat(
        [
            df["Type 1"].value_counts(),
            df["Type 2"].value_counts(),
        ]
    )

    # The same type can appear in both Type 1 and Type 2.
    # groupby(level=0) groups matching type names together.
    #
    # For example, all "Fire" counts are placed into one group.
    .groupby(level=0)

    # Add together the Type 1 and Type 2 counts for each type.
    .sum()

    # Sort from the most common type to the least common type.
    .sort_values(ascending=False)

    # Remove the temporary "missing" category that was created earlier.
    .drop("missing")
)


# ============================================================
# FILTER POKÉMON BY TYPE
# ============================================================

def filtered_types(poke_type):
    """
    Return Pokémon that have the requested primary or secondary type.

    Parameters
    ----------
    poke_type:
        The Pokémon type supplied by the user, such as "fire",
        "Water" or "  grass  ".

    Returns
    -------
    pandas.DataFrame
        A filtered table containing Pokémon whose "Type 1" or
        "Type 2" matches the requested type.
    """

    # Remove spaces before and after the input.
    # Capitalize the first letter so inputs such as "fire" become "Fire".
    poke_type = poke_type.capitalize().strip()

    # Filter the DataFrame.
    #
    # Backticks are needed around `Type 1` and `Type 2` because
    # their column names contain spaces.
    #
    # @poke_type tells Pandas to use the Python variable named poke_type.
    #
    # A row is returned when the requested type matches either
    # the primary type or the secondary type.
    return df.query(
        "`Type 1` == @poke_type or `Type 2` == @poke_type"
    )