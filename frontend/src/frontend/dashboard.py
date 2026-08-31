"""
Streamlit frontend for the eClipseBord dashboard.
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


# AI-assisted refactor:
def get_eclipse_data(route: str, params: dict | None = None) -> pd.DataFrame:
    """Request eclipse records from FastAPI and return them as a DataFrame."""

    # Build the API URL and send an HTTP GET request.
    response = httpx.get(f"{BASE_URL}/{route}", params=params, timeout=30.0)

    # Raise an error if FastAPI returns an unsuccessful status code.
    response.raise_for_status()

    # Convert the JSON response into a Pandas DataFrame.
    return pd.DataFrame(response.json())



# ============================================================
# DISPLAY ONE ECLIPSE TAB
# ============================================================

def format_eclipse_year(year: int) -> str:
    """Display astronomical years as user-friendly BCE or CE labels."""
    if year <= 0:
        return f"{1 - year} BCE"
    return f"{year} CE"


def show_eclipse_tab(label: str, route: str) -> None:
    """Display one eclipse dataset with the approved filters."""
    all_eclipses = get_eclipse_data(route)


    # AI-assisted refactor: category options come directly from transformed data.
    # Get every unique year and sort them from earliest to latest.
    years = sorted(all_eclipses["Year"].dropna().astype(int).unique().tolist())

    # Get every available eclipse category without duplicates.
    categories = ["All", *sorted(all_eclipses["Eclipse Category"].dropna().unique().tolist()),]

    # Create a dropdown menu for selecting a year.
    selected_year = st.selectbox(
        f"{label} eclipse year",
        options=years,
        index=years.index(2000) if 2000 in years else 0,             # select 2000 as default
        format_func = format_eclipse_year,
        key=f"{route}-year",                                        # Give the widget a unique key for the Solar or Lunar tab.
    )


    # Create a dropdown menu for selecting an eclipse category.
    selected_category = st.selectbox(
        f"{label} eclipse category",
        options=categories,
        key=f"{route}-category",
    )


    # Always filter by year, and filter by category when one is selected.
    params = {"year": int(selected_year)}
    if selected_category != "All":
        params["eclipse_category"] = selected_category

    filtered_eclipses = get_eclipse_data(route, params=params)


    # Display the number of matching eclipse records.
    st.write(
        f"{len(filtered_eclipses)} {label.lower()} eclipse record(s) match "
        "the selected filters."
    )

    # Display the matching records as an interactive table.
    st.dataframe(filtered_eclipses, use_container_width=True)



# ============================================================
# MAIN STREAMLIT APPLICATION
# ============================================================

# AI-assisted refactor:
def main() -> None:
    """
    Build the eClipseBord dashboard.

    The dashboard contains separate tabs for Solar and Lunar
    eclipse data. Each tab has its own year and category filters.
    """

    # Configure the browser tab title and use the full page width.
    st.set_page_config(page_title="eClipseBord", layout="wide")

    # Display the dashboard title and introduction.
    st.title("eClipseBord")
    st.markdown("Explore Solar and Lunar eclipses by year and eclipse category.")
    st.markdown(
        "**How to read the years:** BCE means a year before year 1, while "
        "CE means year 1 or later. For example, 2000 BCE is an ancient year, "
        "2026 CE is our modern time, and future eclipse dates are scientific "
        "predictions."
    )


    # Create separate tabs for the two eclipse datasets.
    solar_tab, lunar_tab = st.tabs(["Solar eclipses", "Lunar eclipses"])

    # Display the Solar eclipse filters and table.
    with solar_tab:
        show_eclipse_tab("Solar", "solar-eclipses")

    # Display the Lunar eclipse filters and table.
    with lunar_tab:
        show_eclipse_tab("Lunar", "lunar-eclipses")


# Start the Streamlit application.
main()