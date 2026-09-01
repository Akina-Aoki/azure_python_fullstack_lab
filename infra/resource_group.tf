# Create the Azure Resource Group
resource "azurerm_resource_group" "rg" {
  name     = var.resource-group-name
  location = var.location
}