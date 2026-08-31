# azure_python_fullstack_lab
Show knowledge in Python, FastAPI,  Streamlit as well as Docker and Azure to build deployable fullstack application.

## Dataset
https://www.kaggle.com/datasets/nasa/solar-eclipses?resource=download

## NOTES
- `source .venv/Scripts/activate`

```
which python
python --version
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
