# This block tells Terraform which providers and Terraform version
# are required for this project.
terraform {

  # Providers are plugins Terraform uses to communicate
  # with external platforms such as Microsoft Azure.
  required_providers {

    # azurerm is the official Terraform provider for Microsoft Azure.
    azurerm = {
      # This tells Terraform where to download the Azure provider from.
      source = "hashicorp/azurerm"

      # Use version 4.4 or any compatible newer 4.x version.
      # "~> 4.4" allows updates like 4.5, 4.10, etc.,
      # but not a major version like 5.0.
      version = "~> 4.4"
    }
  }

  # This project requires Terraform version 1.13 or newer.
  required_version = ">= 1.13"
}


# This configures the Microsoft Azure provider.
# Terraform will use this provider when creating,
# updating, or deleting Azure resources.
provider "azurerm" {

  # The features block is required by the AzureRM provider.
  # It can also be used to configure optional Azure-specific behavior,
  # but an empty block is enough for this project.
  features {}
}