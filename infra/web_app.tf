# Create the Linux App Service plan that will host the frontend
resource "azurerm_service_plan" "asp" {
  name                = "${var.project_name}-asp"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  # Run the App Service on Linux
  os_type = "Linux"

  # B1 is the pricing / compute tier
  sku_name = "B1"
}


# Create the frontend Web App
resource "azurerm_linux_web_app" "webapp" {

  # Use the project name + random suffix to make the name unique
  name = "${var.project_name}-webapp-${random_string.suffix.result}"

  # Put the Web App inside our resource group
  resource_group_name = azurerm_resource_group.rg.name

  # Use the same Azure region as the resource group
  location = azurerm_resource_group.rg.location

  # Connect this Web App to the App Service plan above
  service_plan_id = azurerm_service_plan.asp.id


  # Configure the Docker container used by the Web App
  site_config {
    application_stack {

      # Docker image and tag to run
      docker_image_name = "frontend:${var.image_tag}"

      # Azure Container Registry where the image is stored
      docker_registry_url = "https://${azurerm_container_registry.acr.login_server}"
    }

    # Let the Web App use its Azure identity to access ACR
    container_registry_use_managed_identity = true
  }


  # Give the Web App its own managed identity
  identity {
    type = "SystemAssigned"
  }


  # Environment settings for the running application
  app_settings = {

    # Streamlit listens on port 8501
    "WEBSITES_PORT" = "8501"

    # Allow the Web App to pull updated images from ACR
    "DOCKER_ENABLE_CI" = "true"
  }
}