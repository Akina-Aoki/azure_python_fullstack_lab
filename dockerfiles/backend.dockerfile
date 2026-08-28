# Use a lightweight Python 3.13 image as the starting point
FROM python:3.13-slim

# Copy everything from the backend folder into /app
COPY backend/ /app/

# Install uv, which manages the Python packages
RUN pip install --no-cache-dir uv

# Set /app as the current working folder
WORKDIR /app

# Install the backend dependencies from pyproject.toml
# --no-dev skips packages only needed during development
RUN uv sync --no-dev

# Move to the folder containing the FastAPI application
WORKDIR /app/src/backend

# Start the FastAPI application using Uvicorn
# api:app means: use the variable named "app" inside api.py
# 0.0.0.0 makes the API accessible outside the Docker container
CMD ["uv", "run", "uvicorn", "api:app", "--host", "0.0.0.0"]