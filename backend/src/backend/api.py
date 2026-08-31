"""
Create the FastAPI endpoints for the eClipseBord dashboard.

The API allows clients to:

1. Retrieve Solar eclipse records.
2. Retrieve Lunar eclipse records.
3. Optionally filter the records by year.
4. Optionally filter the records by eclipse category.
"""

from fastapi import FastAPI
from typing import Any
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

    """
    dataframe: pd.DataFrame — the input should be a pandas DataFrame.
    -> — shows what the function returns.
    list[...] — it returns a list.
    dict[str, Any] — each item is a dictionary:
        The keys are strings, such as "Year".
        The values can be any type: text, numbers, booleans, or None.

    Parameters
    ----------
    data:
        The DataFrame that should be returned by the API.

    Returns
    -------
        [
            {
                "Year": 2024,
                "Eclipse Category": "Total",
                "Visible": True
            }
        ]
    """

                                                                                
    clean_data = data.astype(object)                                               # Convert the DataFrame to object type so it can contain None values.
    clean_data = data.astype(object).where(pd.notna(data), None)                   # Convert the DataFrame to object type so it can contain None values.
    return clean_data.to_dict(orient="records")                                    # Convert every DataFrame row into a dictionary.


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
      Return Solar eclipse records using the selected filters.

    Parameters
    ----------
    year:
        Optional year selected by the user. If it is not provided,
        records from every year are available.

    eclipse_category:
        Optional eclipse category, such as Partial, Annular, Total,
        or Hybrid.

    Returns
    -------
    list[dict]
        Solar eclipse records converted into JSON-compatible data.  
    """

    # Begin with the complete Solar eclipse dataset.
    data = solar_eclipses
    if year is not None:                                    # Apply the year filter only when the user provides a year.
        data = filter_solar_by_year(year)
    if eclipse_category is not None:                         # Apply the category filter only when the user provides a category.
        data = (
             filter_solar_by_category(eclipse_category)

            # If no year was selected, filter the complete Solar dataset
            # using the category-filtering function.
            if year is None

            # If a year was already selected, filter the year results
            # so that both filters are applied.
            else data[data["Eclipse Category"] == eclipse_category]
        )
    return json_records(data)                               # Convert the filtered DataFrame into JSON-compatible records.     
        


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
    """
    Return Lunar eclipse records using the selected filters.

    Parameters
    ----------
    year:
        Optional year selected by the user. If it is not provided,
        records from every year are available.

    eclipse_category:
        Optional Lunar eclipse category, such as Penumbral,
        Partial, or Total.

    Returns
    -------
    list[dict]
        Lunar eclipse records converted into JSON-compatible data.
    """
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

