"""
Streamlit frontend for the eClipseBord dashboard.
"""

import streamlit as st

from frontend.tabs import ECLIPSE_TABS, show_eclipse_tab

def main() -> None:
    """Configure the page and display the Solar and Lunar tabs."""
    # Page configuration must be the first Streamlit command.
    st.set_page_config(page_title="eClipseBord", layout="wide")

    # Keep introductory text in the entry point because it belongs to the page,
    # rather than to either eclipse tab.
    st.title("eClipseBord")
    st.markdown("Explore Solar and Lunar eclipses by year and eclipse category.")
    st.markdown(
        "**How to read the years:** BCE means a year before year 1, while "
        "CE means year 1 or later. For example, 2000 BCE is an ancient year, "
        "2026 CE is our modern time, and future eclipse dates are scientific "
        "predictions."
    )


    # The configuration list lets both tabs use the same rendering function.
    streamlit_tabs = st.tabs([config["title"] for config in ECLIPSE_TABS])
    for tab, config in zip(streamlit_tabs, ECLIPSE_TABS):
        with tab:
            show_eclipse_tab(config)


# Start the Streamlit application.
if __name__ == "__main__":
    main()