"""Small HTTP client used by the Streamlit dashboard."""
# LLM Generated code to keep the frontend DRY


import os

import httpx
import pandas as pd


# Docker supplies BACKEND_URL; local development uses FastAPI's default address.
BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")


def get_eclipse_data(route: str, params: dict | None = None) -> pd.DataFrame:
    """Request eclipse records from FastAPI and return a DataFrame."""
    # `params` contains only filters selected by the user.
    response = httpx.get(f"{BASE_URL}/{route}", params=params, timeout=30.0)
    # Turn unsuccessful API responses into clear HTTPX errors.
    response.raise_for_status()

    # Streamlit charts, metrics, and tables all work naturally with DataFrames.
    return pd.DataFrame(response.json())