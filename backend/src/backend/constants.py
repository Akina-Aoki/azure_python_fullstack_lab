"""
Define the FastAPI application and its Pokémon API endpoints.

The API allows clients to:
1. Retrieve every Pokémon.
2. Retrieve the number of Pokémon belonging to each type.
3. Filter Pokémon by a requested type.
"""

from fastapi import FastAPI

# Import the processed data and filtering function.
from backend.data_processing import df, filtered_types, number_per_type


# Create the FastAPI application.
# The "app" object receives requests and connects them to functions.
app = FastAPI()


# ============================================================
# ENDPOINT 1: RETURN ALL POKÉMON
# ============================================================

# @app.get() creates an HTTP GET endpoint.
#
# This endpoint can be accessed at:
# GET /pokemons/stats
@app.get("/pokemons/stats")
async def show_data():
    """
    Return all Pokémon records.

    Returns
    -------
    list[dict]
        A list in which each dictionary represents one Pokémon row.
        FastAPI converts the result into JSON automatically.
    """

    # orient="records" produces a list of dictionaries.
    #
    # Example:
    # [
    #     {"Name": "Bulbasaur", "Type 1": "Grass"},
    #     {"Name": "Charmander", "Type 1": "Fire"}
    # ]
    return df.to_dict(orient="records")


# ============================================================
# ENDPOINT 2: RETURN THE COUNT FOR EACH TYPE
# ============================================================

# This endpoint can be accessed at:
# GET /pokemons/number_types
@app.get("/pokemons/number_types")
async def number_pokemons_per_type():
    """
    Return the total number of Pokémon associated with each type.

    The count includes Pokémon where the type appears as either
    "Type 1" or "Type 2".

    Returns
    -------
    dict
        A dictionary mapping each Pokémon type to its total count.
    """

    # Convert the Pandas Series into a regular Python dictionary.
    #
    # Example:
    # {
    #     "Water": 126,
    #     "Normal": 102,
    #     "Flying": 101
    # }
    return number_per_type.to_dict()


# ============================================================
# ENDPOINT 3: FILTER BY TYPE
# ============================================================

# Because poke_type is not included directly in the route,
# FastAPI treats it as a required query parameter.
#
# Example request:
# GET /pokemons/type?poke_type=Fire
@app.get("/pokemons/type")
async def filter_pokemon_type(poke_type):
    """
    Return Pokémon matching a requested type.

    Parameters
    ----------
    poke_type:
        A required query parameter containing a Pokémon type,
        such as "Fire", "Water" or "Grass".

    Returns
    -------
    list[dict]
        Matching Pokémon records converted into JSON-compatible data.
    """

    # filtered_types() returns a filtered DataFrame.
    # orient="records" converts each row into a dictionary.
    return filtered_types(poke_type).to_dict(orient="records")