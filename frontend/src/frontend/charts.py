"""Shared charts for Solar and Lunar eclipse data."""
# LLM Generated code to keep the frontend DRY


import pandas as pd
import streamlit as st


def eclipse_counts(data: pd.DataFrame, group_column: str) -> pd.DataFrame:
    """Count eclipse rows for each value in a selected column."""
    # Preserve the expected chart columns when no records match the filters.
    if group_column not in data:
        return pd.DataFrame(columns=[group_column, "Number of eclipses"])

    # Return tidy data that can be passed to either Streamlit chart function.
    return (
        data.groupby(group_column, as_index=False)
        .size()
        .rename(columns={"size": "Number of eclipses"})
        .sort_values(group_column)
    )


def show_charts(data: pd.DataFrame) -> None:
    """Display category counts and yearly counts side by side."""
    # The same two aggregations are useful for both Solar and Lunar data.
    category_column, timeline_column = st.columns(2)

    with category_column:
        st.subheader("Eclipses by category")
        category_counts = eclipse_counts(data, "Eclipse Category")
        st.bar_chart(
            category_counts,
            x="Eclipse Category",
            y="Number of eclipses",
            use_container_width=True,
        )

    with timeline_column:
        st.subheader("Eclipses over time")
        yearly_counts = eclipse_counts(data, "Year")
        st.line_chart(
            yearly_counts,
            x="Year",
            y="Number of eclipses",
            use_container_width=True,
        )