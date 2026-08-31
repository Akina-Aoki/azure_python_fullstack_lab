"""KPI calculations and presentation for eclipse data."""
# LLM Generated code to keep the frontend DRY

import pandas as pd
import streamlit as st


LUNAR_DURATION_COLUMNS = {
    "Penumbral": "Penumbral Eclipse Duration (m)",
    "Partial": "Partial Eclipse Duration (m)",
    "Total": "Total Eclipse Duration (m)",
}


def numeric_average(data: pd.DataFrame, column: str) -> float:
    """Return a column average while ignoring missing and non-numeric values."""
    # An empty API response creates a DataFrame without columns.
    if column not in data:
        return float("nan")

    # The source CSV uses "-" for some unavailable measurements.
    return pd.to_numeric(data[column], errors="coerce").mean()


def average_lunar_duration(data: pd.DataFrame) -> float:
    """Average each lunar eclipse's duration for its eclipse category."""
    if data.empty or "Eclipse Category" not in data:
        return float("nan")
    # Lunar duration is stored in a different column for each category. Build
    # one Series containing the relevant duration for every eclipse record.
    durations = pd.Series(index=data.index, dtype="float64")
    for category, column in LUNAR_DURATION_COLUMNS.items():
        if column not in data:
            continue
        rows = data["Eclipse Category"] == category
        durations.loc[rows] = pd.to_numeric(data.loc[rows, column], errors="coerce")
    return durations.mean()


def format_average(value: float, suffix: str = "") -> str:
    """Format an average consistently, including an empty-result state."""
    # NaN means no matching records had a usable measurement.
    if pd.isna(value):
        return "N/A"
    return f"{value:,.2f}{suffix}"


def show_kpis(data: pd.DataFrame, kind: str) -> None:
    """Display the three KPIs appropriate for an eclipse dataset."""
    # Both tabs share the total KPI but use different measurement columns.
    total_column, magnitude_column, third_column = st.columns(3)
    total_column.metric("Total eclipses", f"{len(data):,}")

    if kind == "solar":
        magnitude_column.metric(
            "Average eclipse magnitude",
            format_average(numeric_average(data, "Eclipse Magnitude")),
        )
        third_column.metric(
            "Average path width",
            format_average(numeric_average(data, "Path Width (km)"), " km"),
        )
    else:
        magnitude_column.metric(
            "Average umbral magnitude",
            format_average(numeric_average(data, "Umbral Magnitude")),
        )
        third_column.metric(
            "Average eclipse duration",
            format_average(average_lunar_duration(data), " min"),
        )