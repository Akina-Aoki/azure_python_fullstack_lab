"""Reusable eclipse event cards for the Solar and Lunar tabs."""

from collections.abc import Sequence
from datetime import datetime
from typing import Any

import pandas as pd
import streamlit as st

from frontend.filters import format_eclipse_year


COMMON_FIELDS = (
    "Catalog Number",
    "Eclipse Time",
    "Delta T (s)",
    "Lunation Number",
    "Saros Number",
    "Eclipse Type",
)

# A small configuration captures only the schema differences between datasets.
EVENT_FIELDS = {
    "solar": (
        *COMMON_FIELDS,
        "Gamma",
        "Eclipse Magnitude",
        "Latitude",
        "Longtitude",
        "Sun Altitude",
        "Sun Azimuth",
        "Path Width",
        "Central Duration",
    ),

    "lunar": (
        *COMMON_FIELDS,
        "Quincena Solar Eclipse",
        "Gamma",
        "Penumbral Magnitude",
        "Umbral Magnitude",
        "Latitude",
        "Longitude",
        "Penumbral Eclipse Duration (m)",
        "Partial Eclipse Duration (m)",
        "Total Eclipse Duration (m)",
    ),
}


def is_present(value: Any) -> bool:
    """Return whether an API value contains a useful display value."""
    if value is None or (isinstance(value, str) and value.strip() in {"", "-"}):
        return False
    try:
        return not bool(pd.isna(value))
    except (TypeError, ValueError):
        return True


def format_value(value: Any) -> str:
    """Format a raw API value without adding precision not present in it."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def format_calendar_date(value: Any) -> str:
    """Move the catalog year to the end for a familiar event-date display."""
    if not is_present(value):
        return "Date unavailable"
    value = str(value)
    parts = value.split(maxsplit=2)
    if len(parts) != 3:
        return value
    year, month, day = parts
    try:
        month = datetime.strptime(month, "%B").strftime("%B")
        display_year = format_eclipse_year(int(year)).removesuffix(" CE")
        return f"{month} {int(day)}, {display_year}"
    except ValueError:
        return value


def event_details(row: pd.Series, fields: Sequence[str]) -> pd.DataFrame:
    """Build the compact property/value table for an eclipse record."""
    details = [
        {"Property": field, "Value": format_value(row.get(field))}
        for field in fields
        if is_present(row.get(field))
    ]
    return pd.DataFrame(details, columns=["Property", "Value"])


def chronological_events(data: pd.DataFrame) -> pd.DataFrame:
    """Return records ordered by their catalog date and time."""
    if data.empty or "Calendar Date" not in data:
        return data
    date_parts = data["Calendar Date"].astype(str).str.extract(
        r"^-?\d+\s+(?P<month>[A-Za-z]+)\s+(?P<day>\d+)$"
    )
    month_numbers = date_parts["month"].map(
        {
            month: number
            for number, month in enumerate(
                (
                    "January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November",
                    "December",
                ),
                1,
            )
        }
    )
    sortable = data.assign(
        _year=pd.to_numeric(data.get("Year"), errors="coerce"),
        _month=month_numbers,
        _day=pd.to_numeric(date_parts["day"], errors="coerce"),
        _time=data.get("Eclipse Time", ""),
    )
    return sortable.sort_values(
        ["_year", "_month", "_day", "_time"], kind="stable", na_position="last"
    ).drop(columns=["_year", "_month", "_day", "_time"])


def show_event_cards(data: pd.DataFrame, kind: str, selected_year: int | str) -> None:
    """Render a compact, shared event summary above the records table."""
    st.subheader(f"Eclipse events for {format_eclipse_year(selected_year)}")
    if data.empty:
        st.info("No eclipse events match the selected filters.")
        return

    fields: Sequence[str] = EVENT_FIELDS[kind]
    for _, row in chronological_events(data).iterrows():
        with st.container(border=True):
            year_column, category_column, date_column = st.columns(3)
            year_column.metric("YEAR", format_value(row.get("Year")))
            category_column.metric(
                "ECLIPSE CATEGORY", format_value(row.get("Eclipse Category"))
            )
            date_column.metric(
                "CALENDAR DATE", format_calendar_date(row.get("Calendar Date"))
            )

            details = event_details(row, fields)
            st.dataframe(
                details,
                hide_index=True,
                use_container_width=True,
                height=min(38 + 35 * len(details), 600),
                column_config={
                    "Property": st.column_config.TextColumn(width="medium"),
                    "Value": st.column_config.TextColumn(width="large"),
                },
            )