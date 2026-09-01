"""Configuration and shared layout for both eclipse tabs."""
# LLM Generated code to keep the frontend DRY

import streamlit as st

from frontend.api_client import get_eclipse_data
from frontend.events import show_event_cards
from frontend.filters import show_filters
from frontend.metrics import show_kpis


# Only values that differ between tabs live in this configuration.
ECLIPSE_TABS = (
    {
        "title": "Solar eclipses",
        "label": "Solar",
        "kind": "solar",
        "route": "solar-eclipses",
    },
    {
        "title": "Lunar eclipses",
        "label": "Lunar",
        "kind": "lunar",
        "route": "lunar-eclipses",
    },
)


def show_eclipse_tab(config: dict[str, str]) -> None:
    """Render the common filters, summary and events for one tab."""
    # The unfiltered request supplies every available selector option.
    all_eclipses = get_eclipse_data(config["route"])
    params = show_filters(all_eclipses, config["label"], config["route"])

    # Request the selected subset once, then reuse it for all dashboard parts.
    filtered_eclipses = get_eclipse_data(config["route"], params=params)

    st.divider()
    show_kpis(filtered_eclipses, config["kind"])
    selected_year = params.get("year", "All years")
    show_event_cards(filtered_eclipses, config["kind"], selected_year)
