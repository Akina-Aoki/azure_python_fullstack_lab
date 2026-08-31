"""Configuration and shared layout for both eclipse tabs."""
# LLM Generated code to keep the frontend DRY

import streamlit as st

from frontend.api_client import get_eclipse_data
from frontend.charts import show_charts
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
    """Render the common filters, visualizations, and table for one tab."""
    # The unfiltered request supplies every available selector option.
    all_eclipses = get_eclipse_data(config["route"])
    params = show_filters(all_eclipses, config["label"], config["route"])

    # Request the selected subset once, then reuse it for all dashboard parts.
    filtered_eclipses = get_eclipse_data(config["route"], params=params)

    st.divider()
    show_kpis(filtered_eclipses, config["kind"])
    show_charts(filtered_eclipses)

    # Keep the detailed source records below the summary visualizations.
    st.subheader(f"{config['label']} eclipse records")
    st.caption(
        f"{len(filtered_eclipses)} {config['label'].lower()} eclipse record(s) "
        "match the selected filters."
    )
    st.dataframe(filtered_eclipses, use_container_width=True)