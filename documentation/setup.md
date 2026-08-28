# Setting up the environment

## Initialize uv
- `uv init --no-package --python 3.13`
- Result: Creates .python-version, pyproject.toml, main.py (not needed)

## Add pakacges & 2 separate workspaces. 1 in backend and 1 in frontend
- `uv init --package backend`
- `uv init --package frontend`


## Add dependencies in backend and frontend pyproject.toml
`dependencies = ["uvicorn", "fastapi", "pandas"]`
`dependencies = ["streamlit", "httpx"]`
