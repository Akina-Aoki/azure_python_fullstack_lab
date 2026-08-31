# Setting up the environment
LINK for code and video: https://github.com/AIgineerAB/cloud_databricks_azure_course/tree/main/15_dockerize_deploy_fastapi_streamlit


## Initialize uv
- `uv init --no-package --python 3.13`
- Result: Creates .python-version, pyproject.toml, main.py (not needed)

## Add pakacges & 2 separate workspaces. 1 in backend and 1 in frontend
- `uv init --package backend`
- `uv init --package frontend`


## Add dependencies in backend and frontend pyproject.toml
- `dependencies = ["uvicorn", "fastapi", "pandas"]`
- `dependencies = ["streamlit", "httpx"]`


## Sync packacges
- Installs all the dependencies and creates a venv in thr root.
- `uv sync --all-packages`

## Create the backend scripts
- `api.py`, `constants.py`, `data_processing.py`
- All sample code from lecture available in the link

## Add EDA dependencies and update uvlock
- `uv add --dev pandas ipykernel matplotlib seaborn`
- This automatically updates pyproject.toml and uv.lock.


