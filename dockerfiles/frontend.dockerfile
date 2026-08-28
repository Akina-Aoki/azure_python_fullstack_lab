# Use a lightweight Python 3.13 image as the starting point
FROM python:3.13-slim

# Copy everything from the frontend folder into /app
COPY frontend/ /app/

# Install uv, which manages the Python packages
RUN pip install --no-cache-dir uv

# Set /app as the current working folder
WORKDIR /app

# Install the frontend dependencies from pyproject.toml
# --no-dev skips packages only needed during development
RUN uv sync --no-dev

# Move to the folder containing the Streamlit application
WORKDIR /app/src/frontend

# Start the Streamlit dashboard
# 0.0.0.0 makes the app accessible outside the Docker container
# ells Streamlit to run on port 8501 inside the container. ""--server.port=8501", "--server.address=0.0.0.0""
# Start the Streamlit app on port 8501 and make it accessible through Docker.
CMD ["uv", "run", "streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]