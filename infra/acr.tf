# Create an Azure Container Registry (ACR) for Docker images
# This is where Docker Images lives
resource "azurerm_container_registry" "acr" {
  name                = "${var.acr_name}${random_string.suffix.result}"   # must be unique so use this
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Basic"

  # Allow username/password login to the registry
  admin_enabled = true
}

# Apply only the ACR and its dependencies
# terraform apply -auto-approve -target=azurerm_container_registry.acr