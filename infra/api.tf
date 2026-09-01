# Create the environment where the container app will run
resource "azurerm_container_app_environment" "env" {
  name                = "${var.project_name}-cae"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
}

# Create the backend Container App
resource "azurerm_container_app" "api" {
  name                         = "${var.project_name}-api"
  resource_group_name          = azurerm_resource_group.rg.name
  container_app_environment_id = azurerm_container_app_environment.env.id
  revision_mode                = "Single"

  # Container settings
  template {
    container {
      name   = "api"
      image  = "mcr.microsoft.com/k8se/quickstart:latest"
      cpu    = 1.0
      memory = "2Gi"
    }
  }

  # Make the app accessible from the internet
  ingress {
    external_enabled = true
    target_port      = 8000

    # Send all traffic to the latest revision
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}