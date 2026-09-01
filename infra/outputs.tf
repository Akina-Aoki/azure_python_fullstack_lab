# Show the ACR login server after deployment
output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

# Show the ACR name
output "acr_name" {
  value = azurerm_container_registry.acr.name
}

# Show the Container App name
output "container_app_name" {
  value = azurerm_container_app.api.name
}

# Show the Resource Group name
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}