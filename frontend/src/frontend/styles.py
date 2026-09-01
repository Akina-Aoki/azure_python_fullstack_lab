"""Shared visual theme for the Streamlit dashboard."""
# LLM Generated Code

import streamlit as st


# Keep the eclipse palette in one place so every component uses the same colors.
COLORS = {
    "deep_navy": "#041E2B",
    "charcoal": "#353E43",
    "steel_blue": "#628699",
    "light_blue": "#B9D9EB",
}


def apply_theme() -> None:
    """Apply the accessible eclipse theme to the current Streamlit page."""
    navy = COLORS["deep_navy"]
    charcoal = COLORS["charcoal"]
    steel = COLORS["steel_blue"]
    light = COLORS["light_blue"]

    st.markdown(
        f"""
        <style>
        :root {{
            --eclipse-navy: {navy};
            --eclipse-charcoal: {charcoal};
            --eclipse-steel: {steel};
            --eclipse-light: {light};
            --eclipse-text: #F3F7F9;
            --eclipse-muted: #D5E1E7;
            --eclipse-radius: 0.75rem;
            --eclipse-glow: 0 0 1rem rgba(185, 217, 235, 0.14);
        }}

        .stApp,
        [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(circle at 88% 2%, rgba(98, 134, 153, 0.20), transparent 24rem),
                var(--eclipse-navy);
            color: var(--eclipse-text);
        }}

        [data-testid="stHeader"] {{
            background: rgba(4, 30, 43, 0.92);
            border-bottom: 1px solid rgba(98, 134, 153, 0.45);
        }}

        h1, h2, h3, h4, h5, h6,
        [data-testid="stMetricValue"] {{
            color: var(--eclipse-light) !important;
        }}

        p, label, [data-testid="stCaptionContainer"],
        [data-testid="stMetricLabel"] {{
            color: var(--eclipse-muted) !important;
        }}

        [data-testid="stTabs"] [role="tablist"] {{
            gap: 0.5rem;
            border-bottom: 1px solid var(--eclipse-steel);
        }}

        [data-testid="stTabs"] button[role="tab"] {{
            color: var(--eclipse-muted);
            border-radius: var(--eclipse-radius) var(--eclipse-radius) 0 0;
            padding-inline: 1.25rem;
        }}

        [data-testid="stTabs"] button[role="tab"]:hover {{
            color: var(--eclipse-light);
            background: rgba(98, 134, 153, 0.22);
        }}

        [data-testid="stTabs"] button[role="tab"][aria-selected="true"] {{
            color: var(--eclipse-light);
            background: var(--eclipse-charcoal);
            box-shadow: var(--eclipse-glow);
        }}

        [data-testid="stSelectbox"] [data-baseweb="select"] > div {{
            color: var(--eclipse-text);
            background: var(--eclipse-charcoal);
            border-color: var(--eclipse-steel);
            border-radius: var(--eclipse-radius);
        }}

        [data-testid="stSelectbox"] [data-baseweb="select"] > div:hover,
        [data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within {{
            border-color: var(--eclipse-light);
            box-shadow: var(--eclipse-glow);
        }}

        [data-baseweb="popover"] [role="listbox"] {{
            background: var(--eclipse-charcoal);
            border: 1px solid var(--eclipse-steel);
        }}

        [data-baseweb="popover"] [role="option"] {{
            color: var(--eclipse-text);
        }}

        [data-baseweb="popover"] [role="option"]:hover,
        [data-baseweb="popover"] [aria-selected="true"] {{
            color: var(--eclipse-navy);
            background: var(--eclipse-light);
        }}

        [data-testid="stVerticalBlockBorderWrapper"] {{
            background: rgba(53, 62, 67, 0.92);
            border-color: var(--eclipse-steel) !important;
            border-radius: var(--eclipse-radius);
            box-shadow: 0 0.35rem 1.2rem rgba(0, 0, 0, 0.18);
        }}

        [data-testid="stMetric"] {{
            padding: 0.7rem;
            border-left: 2px solid var(--eclipse-light);
        }}

        [data-testid="stButton"] button {{
            color: var(--eclipse-navy);
            background: var(--eclipse-light);
            border: 1px solid var(--eclipse-light);
            border-radius: var(--eclipse-radius);
            font-weight: 600;
            box-shadow: var(--eclipse-glow);
        }}

        [data-testid="stButton"] button:hover {{
            color: var(--eclipse-text);
            background: var(--eclipse-steel);
            border-color: var(--eclipse-light);
        }}

        [data-testid="stDivider"] {{
            border-color: var(--eclipse-steel);
        }}

        [data-testid="stDataFrame"] {{
            overflow: hidden;
            background: var(--eclipse-charcoal);
            border: 1px solid var(--eclipse-steel);
            border-radius: var(--eclipse-radius);
            box-shadow: 0 0.35rem 1.2rem rgba(0, 0, 0, 0.18);
        }}

        [data-testid="stAlert"] {{
            color: var(--eclipse-text);
            background: var(--eclipse-charcoal);
            border: 1px solid var(--eclipse-steel);
            border-radius: var(--eclipse-radius);
            box-shadow: var(--eclipse-glow);
        }}

        [data-testid="stSpinner"] {{
            color: var(--eclipse-light);
        }}

        @media (max-width: 640px) {{
            [data-testid="stMainBlockContainer"] {{
                padding-inline: 1rem;
            }}

            [data-testid="stTabs"] button[role="tab"] {{
                flex: 1;
                padding-inline: 0.5rem;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )