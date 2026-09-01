"""Reusable eclipse event cards for the Solar and Lunar tabs."""

from collections.abc import Mapping, Sequence
from typing import Any

import pandas as pd
import streamlit as st

from frontend.filters import format_eclipse_year


COMMON_FIELDS = (
    ("Time", "Eclipse Time", ""),
    ("Saros number", "Saros Number", ""),
    ("Location", ("Latitude", "Longitude"), ""),
)

# A small configuration captures only the schema differences between datasets.
EVENT_FIELDS = {
    "solar": (
        ("Magnitude", "Eclipse Magnitude", ""),
        ("Duration", "Central Duration", ""),
        ("Path width", "Path Width (km)", " km"),
        ("Eclipse type", "Eclipse Type", ""),
        *COMMON_FIELDS,
    ),
    "lunar": (
        ("Magnitude", "Umbral Magnitude", ""),
        (
            "Duration",
            {
                "Penumbral": "Penumbral Eclipse Duration (m)",
                "Partial": "Partial Eclipse Duration (m)",
                "Total": "Total Eclipse Duration (m)",
            },
            " min",
        ),
        ("Penumbral magnitude", "Penumbral Magnitude", ""),
        ("Eclipse type", "Eclipse Type", ""),
        *COMMON_FIELDS,
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


def field_value(row: pd.Series, source: Any) -> Any:
    """Read a direct, combined, or category-dependent configured field."""
    if isinstance(source, Mapping):
        return row.get(source.get(row.get("Eclipse Category"), ""))
    if isinstance(source, tuple):
        values = [str(row.get(column)) for column in source if is_present(row.get(column))]
        return ", ".join(values) if values else None
    return row.get(source)


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

    fields: Sequence[tuple[str, Any, str]] = EVENT_FIELDS[kind]
    for _, row in chronological_events(data).iterrows():
        date = row.get("Calendar Date", "Date unavailable")
        category = row.get("Eclipse Category")
        heading = f"**{date}**" + (f" · {category}" if is_present(category) else "")
        with st.container(border=True):
            st.markdown(heading)
            values = []
            for label, source, suffix in fields:
                value = field_value(row, source)
                if is_present(value):
                    values.append((label, f"{value}{suffix}"))
            for start in range(0, len(values), 4):
                batch = values[start : start + 4]
                for column, (label, value) in zip(st.columns(len(batch)), batch):
                    column.metric(label, value)