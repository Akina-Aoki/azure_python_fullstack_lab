#!/usr/bin/env bash

# ------------------------------------------------------------
# Deployment automation script
#
# Why we use this:
# Instead of manually running Terraform, logging in to Azure Portal,
# building Docker images, and pushing them one by one,
# this script runs the deployment steps in the correct order.
#
# It helps automate and orchestrate:
# Terraform -> Azure infrastructure -> ACR login
# -> Docker build -> Docker push
#
# This makes the deployment repeatable and reduces manual errors.
# ------------------------------------------------------------


# Stop the script if a command fails or a variable is missing
set -euo pipefail


# Create a unique Docker image tag using the current date and time
# This helps Azure know which version of the image to deploy
IMAGE_TAG="${IMAGE_TAG:-$(date +%Y%m%d%H%M%S)}"


# Folder containing the Terraform files
TF_DIR="./infra"


# Go to the Terraform folder
cd "$TF_DIR"


echo "[1] Terraform init"

# Prepare Terraform and download the required providers
terraform init -input=false -lock=false


echo "[2] Deploy infrastructure"

# Create or update the Azure resources with Terraform
# The image tag is also passed to Terraform for deployment
terraform apply \
  -auto-approve \
  -var=image_tag="$IMAGE_TAG" \
  -lock=false


# Get the ACR (Docker images home) login server created by Terraform
# Example: eclipseboard123.azurecr.io
ACR_LOGIN_SERVER="$(terraform output -raw acr_login_server)"

# Get the Azure Container Registry name
ACR_NAME="$(terraform output -raw acr_name)"


echo "[3] Login to ACR"

# Login to Azure Container Registry
# This allows Docker to push images to Azure
# Passwordless login
az acr login --name "$ACR_NAME"


# Make these values available to Docker Compose
export IMAGE_TAG
export ACR_LOGIN_SERVER


# Go back to the project root, thenn access docker-compose.yaml
cd ..


echo "[4] Build and push images"

# Build the frontend and backend Docker images
docker compose build

# Push the images to Azure Container Registry
docker compose push