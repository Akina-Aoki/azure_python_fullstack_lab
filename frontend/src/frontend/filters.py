"""Reusable year and category selectors for eclipse tabs."""
# LLM Generated code to keep the frontend DRY


import pandas as pd
import streamlit as st


def format_eclipse_year(year: int | str) -> str:
    """Display astronomical years as user-friendly BCE or CE labels."""
    # Keep the non-numeric option unchanged in the select box.
    if year == "All years":
        return year

    # Astronomical year 0 is displayed as 1 BCE, -1 as 2 BCE, and so on.
    year = int(year)
    if year <= 0:
        return f"{1 - year} BCE"
    return f"{year} CE"


def show_filters(
    data: pd.DataFrame, label: str, route: str
) -> dict[str, int | str]:
    """Display the shared filters and return matching API parameters."""
    # Build filter choices from the API data instead of maintaining them twice.
    years = sorted(data["Year"].dropna().astype(int).unique().tolist())
    year_options = ["All years", *years]
    categories = [
        "All",
        *sorted(data["Eclipse Category"].dropna().unique().tolist()),
    ]

    # Placing the selectors in columns keeps the filter area compact.
    year_column, category_column = st.columns(2)
    with year_column:
        selected_year = st.selectbox(
            f"{label} eclipse year",
            options=year_options,
            format_func=format_eclipse_year,
            key=f"{route}-year",
        )
    with category_column:
        selected_category = st.selectbox(
            f"{label} eclipse category",
            options=categories,
            key=f"{route}-category",
        )

    # An omitted parameter tells FastAPI to return every value for that filter.
    params: dict[str, int | str] = {}
    if selected_year != "All years":
        params["year"] = int(selected_year)
    if selected_category != "All":
        params["eclipse_category"] = selected_category
    return params