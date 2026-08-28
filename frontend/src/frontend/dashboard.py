"""
Create the Streamlit frontend for the Pokémon dashboard.

This application:
1. Connects to the FastAPI backend.
2. Retrieves Pokémon data through API requests.
3. Displays a chart and data tables.
4. Allows the user to filter Pokémon by type.
"""

import os

import httpx
import pandas as pd
import streamlit as st


# ============================================================
# BACKEND API ADDRESS
# ============================================================

# os.getenv() looks for an environment variable called BACKEND_URL.
#
# If BACKEND_URL exists, its value will be used.
# This is useful when the frontend and backend are running in Docker
# or deployed to a cloud environment.
#
# If the environment variable does not exist, the application uses:
# http://127.0.0.1:8000
#
# This fallback assumes that FastAPI is running locally on port 8000.
BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


# ============================================================
# MAIN STREAMLIT APPLICATION
# ============================================================

def main():
    """
    Build and display the PokeDash Streamlit dashboard.

    The function retrieves data from the FastAPI backend and displays:

    - The backend URL
    - A bar chart showing the most common Pokémon types
    - A table containing all Pokémon
    - A type-selection dropdown
    - A table containing Pokémon matching the selected type
    """

    # Create the main dashboard title.
    # A single # in Markdown creates a level-one heading.
    st.markdown("# PokeDash")

    # Display the backend URL currently being used.
    # This can be helpful when checking whether the application
    # is connecting to a local or deployed backend.
    st.write(BASE_URL)


    # ========================================================
    # GET ALL POKÉMON
    # ========================================================

    # Send an HTTP GET request to the FastAPI /pokemons/stats endpoint.
    #
    # httpx.get() returns an HTTP Response object.
    # .json() converts the JSON response into Python data.
    #
    # In this case, the result should be a list of dictionaries.
    stats = httpx.get(f"{BASE_URL}/pokemons/stats").json()

    # Display introductory text underneath the dashboard title.
    st.markdown("All cool stuffs u need 2 know abt pokes")


    # ========================================================
    # DISPLAY THE POKÉMON TYPE CHART
    # ========================================================

    # Create a level-two heading.
    st.markdown("## PokeTypes")

    # Request the calculated Pokémon type counts from FastAPI.
    #
    # The expected response looks similar to:
    # {
    #     "Water": 126,
    #     "Normal": 102,
    #     "Flying": 101
    # }
    pokemons_per_type = httpx.get(
        f"{BASE_URL}/pokemons/number_types"
    ).json()

    # Convert the dictionary into a Pandas DataFrame.
    #
    # .items() produces key-value pairs:
    # ("Water", 126), ("Normal", 102), ...
    #
    # list() converts those pairs into a list.
    #
    # The resulting DataFrame has two columns:
    # - type
    # - number
    pokemons_per_type = pd.DataFrame(
        list(pokemons_per_type.items()),
        columns=["type", "number"],
    )

    # Display a bar chart containing the first eight Pokémon types.
    #
    # head(8) selects the first eight rows.
    # x="type" places the Pokémon types on the horizontal axis.
    # y="number" controls the height of each bar.
    st.bar_chart(
        pokemons_per_type.head(8),
        x="type",
        y="number",
    )


    # ========================================================
    # DISPLAY ALL POKÉMON
    # ========================================================

    # Display the complete list of Pokémon as an interactive table.
    st.dataframe(stats)


    # ========================================================
    # CREATE THE TYPE FILTER
    # ========================================================

    # Convert the list of Pokémon dictionaries into a DataFrame.
    # This makes it possible to work with columns such as "Type 1".
    df = pd.DataFrame(stats)

    # Select all unique primary Pokémon types.
    #
    # unique() removes repeated values.
    #
    # Example:
    # ["Grass", "Fire", "Water", "Bug", ...]
    types = df["Type 1"].unique()

    # Display a dropdown menu containing the available types.
    #
    # Streamlit stores the user's selected value in poke_type.
    poke_type = st.selectbox(
        label="Choose pokemon type",
        options=types,
    )


    # ========================================================
    # REQUEST THE FILTERED POKÉMON
    # ========================================================

    # Send the selected type to the FastAPI endpoint as a query parameter.
    #
    # Example request:
    # /pokemons/type?poke_type=Fire
    #
    # The API returns Pokémon whose Type 1 or Type 2 is "Fire".
    poke_types = httpx.get(
        f"{BASE_URL}/pokemons/type?poke_type={poke_type}"
    ).json()

    # Display the filtered Pokémon as another interactive table.
    st.dataframe(poke_types)

    # Display text underneath the filtered table.
    st.markdown("Pokemon stats")


# ============================================================
# APPLICATION ENTRY POINT
# ============================================================

# Python sets __name__ to "__main__" when this file is executed directly.
#
# This condition prevents main() from running automatically if the file
# is imported into another Python module.
if __name__ == "__main__":
    main()