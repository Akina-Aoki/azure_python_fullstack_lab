# Variables change depending on the Azure variables


# Name of the Azure Resource Group
variable "resource-group-name" {
  default = "azure-lab"
  type    = string
}

# Azure region where resources will be created
variable "location" {
  type    = string
  default = "swedencentral"
}

# Name used for the project resources
variable "project_name" {
  default = "eclipseboard"
}

# Name for the Azure Container Registry
variable "acr_name" {
  default = "eclipseboard"
}

# Docker image version/tag to deploy
variable "image_tag" {
  default = "latest"  # v1 maybe?
}