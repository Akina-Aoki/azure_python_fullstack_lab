# Azure python fullstack lab
Show knowledge in Python, FastAPI,  Streamlit as well as Docker and Azure to build deployable fullstack application.

## Project overview
eClipseBord displays solar and lunar eclipse data in a web dashboard. The project uses transformed CSV data, a FastAPI backend, and a Streamlit frontend.

- Picture by AIgineer AB
![Task](assets/1.png)

## Dataset
https://www.kaggle.com/datasets/nasa/solar-eclipses?resource=download

## Main features

- Filter eclipse records by year.
- Filter records by eclipse category.
- Switch between Solar and Lunar views.

![Dashboard1](assets/dashboard1.png)
![Dashboard2](assets/dashboard2.png)

## Brief Video Explanation
[![Watch the project demo](assets/yt_thumbnail.png)](https://youtu.be/H0DdgOV8x0w)

## Data transformation
- EDA **IS NOT** the main focus on this lab. The focus is about the deployment of an app locally and with Terraform to Azure.
- The notebooks in `eda/` use pandas to prepare the raw CSV files. 
- They add a numeric `Year` column from `Calendar Date` and an `Eclipse Category` column that turns eclipse type codes into clear category names. 
- The results are saved in `backend/data/transformed/`.

## Technology stack

- Python and pandas for data preparation and filtering
- FastAPI for the API
- Streamlit and HTTPX for the dashboard and API requests
- Docker and Docker Compose for containers
- Azure as the lab's deployment target

<table>
  <tr>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="36" height="36" alt="Python"><br><sub>Python</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" width="36" height="36" alt="FastAPI"><br><sub>FastAPI</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pydantic/pydantic-original.svg" width="36" height="36" alt="Pydantic"><br><sub>Pydantic</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" width="36" height="36" alt="Pandas"><br><sub>Pandas</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg" width="36" height="36" alt="Streamlit"><br><sub>Streamlit</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" width="36" height="36" alt="Docker"><br><sub>Docker</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azure/azure-original.svg" width="36" height="36" alt="Azure"><br><sub>Azure</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/terraform/terraform-original.svg" width="36" height="36" alt="Terraform"><br><sub>Terraform</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" width="36" height="36" alt="Git"><br><sub>Git</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" width="36" height="36" alt="GitHub"><br><sub>GitHub</sub></td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg" width="36" height="36" alt="Bash"><br><sub>Bash</sub></td>
    <td></td>
  </tr>
</table>

## Application architecture
![Streamlit to Fast API flow](assets/2.png)

![Dockerization](assets/dockerization1.png)

FastAPI loads the transformed solar and lunar CSV files. Streamlit requests the records from FastAPI and shows the filters and tables.

## Repository structure

Separate pyproject.toml files are created because each part of the project has a different responsibility and different dependencies.

```text
azure_python_fullstack_lab/
├── assets/
│
├── backend/
│   ├── data/
│   │   ├── raw/
│   │   └── transformed/
│   └── src/backend/
│        └── pyproject.toml            
│
├── frontend/
│   └── src/frontend/
│       └── pyproject.toml
│
├── eda/
├── dockerfiles/
│       ├── backend.dockerfile
│       └── frontend.dockerfile
│
├── documentation/
├── infra/
│   ├── acr.tf
│   ├── api.tf
│   ├── input_variables.tf
│   ├── outputs.tf
│   ├── providers.tf
│   ├── random.tf
│   ├── resource_group.tf
│   └── web_app.tf
├── docker-compose.yaml
├── docker-compose.azure.yaml
├── pyproject.toml
├── deploy_infra.sh
└── README.md
```
| File                      | Reason                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Root `pyproject.toml`     | Manages the whole project as a **uv workspace** and lists `backend` and `frontend` as members. It can also hold shared development tools such as Jupyter and testing packages. |
| `backend/pyproject.toml`  | Contains only backend dependencies, such as FastAPI, Uvicorn, and pandas.                                                                                                      |
| `frontend/pyproject.toml` | Contains only frontend dependencies, such as Streamlit, httpx, and pandas.                                                                                                     |



- Backend runs FastAPI on port `8000`.
- Frontend runs Streamlit on port `8501`.
- Each container installs only the packages it needs.
- You can deploy, update, or troubleshoot one service without affecting the other.
- The root file lets you run and manage everything together during local development.

----

## Documentations
- [Set up](documentation/set_up.md)
- [Running app locally](documentation/run_app.md)
- [Terraform Infra Set up](documentation/terraform_setup.md)
- [Cloud Azure Course (Kokchun's Github):](https://github.com/AIgineerAB/cloud_databricks_azure_course)

## My YouTube Videos: Learning Terraform Step by Step

[![Terraform Part 1: Intro & Providers](assets/yt_thumbnail_tf1.png)](https://www.youtube.com/watch?v=eucMow2W4PE)

[![Terraform Part 2: Input Variables](assets/yt_thumbnail_tf2.png)](https://youtu.be/yMYMsDSpLD0)

[![Terraform Part 3: Resource Group & Azure Container Registry](assets/yt_thumbnail_tf3.png)](https://www.youtube.com/watch?v=WppCffxy8QA)

[![Terraform Part 4: Container App & Environment — Backend](assets/yt_thumbnail_tf4.png)](https://www.youtube.com/watch?v=4ViBG8tlmWk)

[![Terraform Part 5: Azure Web App — Frontend](assets/yt_thumbnail_tf5.png)](https://youtu.be/tuIOHfakgpI)

[![Terraform Part 6: Outputs and Bash Deployment](assets/yt_thumbnail_tf6.png)](https://youtu.be/Tvz70buazuI)