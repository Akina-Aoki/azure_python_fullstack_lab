"""
FastAPI endpoints for the eClipsedBord Dashboard.

The API allows clients to:
1. Retrieve lunar and solar eclipse year and eclipse category.
2. Filter year and eclipse category based on requested filters .
"""

from fastapi import FastAPI
from typing import any
import pandas as pd

# Import the processed data and filtering functions.
from backend.data_processing import (
    filter_lunar_by_category,
    filter_lunar_by_year,
    filter_solar_by_category,
    filter_solar_by_year,
    lunar_eclipses,
    solar_eclipses,

)


# Create the FastAPI application.
# The "app" object receives requests and connects them to functions.
app = FastAPI(
    title = "eClipseBord by FastlyDep",
    description="Explore transformed Solar and Lunar eclipse data by year and category.",
)

def json_records(data: pd.DataFrame) -> list[dict[str, Any]]:
    """Convert a DataFrame, including missing values, into JSON-safe records."""
    clean_data = data.astype(object).where(pd.notna(data), None)
    return clean_data.to_dict(orient="records")


# ============================================================
# ENDPOINT 1: Return all solar eclipses 
# ============================================================

# @app.get() creates an HTTP GET endpoint.
#
# This endpoint can be accessed at:
# GET /solar-eclipses
@app.get("/solar-eclipses",
        summary = "Get solar eclipses",
        description = "Optionally filter solar eclipses by year and category",
         )

async def get_solar_eclipses(
    year: int | None = None,
    eclipse_category: str | None = None,
):
    """
    Return Solar eclipse records for the selected filters.
    """
    data = solar_eclipses
    if year is not None:
        data = filter_solar_by_year(year)
    if eclipse_category is not None:
        data = (
             filter_solar_by_category(eclipse_category)
            if year is None
            else data[data["Eclipse Category"] == eclipse_category]
        )
    return json_records(data)           
        


# ============================================================
# ENDPOINT 2: Return all lunar eclipses 
# ============================================================

# This endpoint can be accessed at:
# GET /lunar_eclipses
@app.get(
    "/lunar-eclipses",
    summary="Get Lunar eclipses",
    description="Optionally filter Lunar eclipses by year and category.",
)
async def get_lunar_eclipses(
    year: int | None = None,
    eclipse_category: str | None = None,
):
    """Return Lunar eclipse records for the selected filters."""
    data = lunar_eclipses
    if year is not None:
        data = filter_lunar_by_year(year)
    if eclipse_category is not None:
        data = (
            filter_lunar_by_category(eclipse_category)
            if year is None
            else data[data["Eclipse Category"] == eclipse_category]
        )
    return json_records(data)

