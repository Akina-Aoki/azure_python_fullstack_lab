# Azure python fullstack lab
Show knowledge in Python, FastAPI,  Streamlit as well as Docker and Azure to build deployable fullstack application.

## Project overview
eClipseBord displays solar and lunar eclipse data in a web dashboard. The project uses transformed CSV data, a FastAPI backend, and a Streamlit frontend.

![Task](assets/1.png)

## Dataset
https://www.kaggle.com/datasets/nasa/solar-eclipses?resource=download

## Main features

- Filter eclipse records by year.
- Filter records by eclipse category.
- Switch between Solar and Lunar views.

## Data transformation

The notebooks in `eda/` use pandas to prepare the raw CSV files. They add a numeric `Year` column from `Calendar Date` and an `Eclipse Category` column that turns eclipse type codes into clear category names. The results are saved in `backend/data/transformed/`.

## Technology stack

- Python and pandas for data preparation and filtering
- FastAPI for the API
- Streamlit and HTTPX for the dashboard and API requests
- Docker and Docker Compose for containers
- Azure as the lab's deployment target
- Terraform is not currently included in this repository

## Application architecture
![Streamlit to Fast API flow](assets/2.png)

![Dockerization](assets/dockerization1.png)

FastAPI loads the transformed solar and lunar CSV files. Streamlit requests the records from FastAPI and shows the filters and tables.

## Repository structure

```text
azure_python_fullstack_lab/
├── backend/
│   ├── data/
│   │   ├── raw/
│   │   └── transformed/
│   └── src/backend/
├── frontend/
│   └── src/frontend/
├── eda/
├── dockerfiles/
├── documentation/
├── docker-compose.yaml
├── pyproject.toml
└── README.md
```


----

## Running the Application Locally

The backend and frontend must run simultaneously in separate terminals.

### 1. Start the FastAPI backend

```bash
cd backend/src/backend
uv run uvicorn api:app --reload
```

FastAPI runs at:

```text
http://127.0.0.1:8000
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### 2. Start the Streamlit frontend

Open a second terminal:

```bash
cd frontend/src/frontend
uv run streamlit run dashboard.py
```

Streamlit runs at:

```text
http://localhost:8501
```

The frontend sends HTTP requests to the FastAPI backend. If the backend is not running, HTTPX returns a connection error such as `WinError 10061`.


----
Notes:
Request URL:
`https://airaeclipseboard-container.happytree-7c375eed.swedencentral.azurecontainerapps.io`