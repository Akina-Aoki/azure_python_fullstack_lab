# Building Terraform Infra with Azure
Video Link: https://www.youtube.com/watch?v=8C-Gh6BAWe4
Github Link: https://github.com/AIgineerAB/cloud_databricks_azure_course/tree/main/16_IaC_terraform_deploy_container
Documentation: https://developer.hashicorp.com/terraform/tutorials/azure-get-started/azure-build
Containers: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app

## Add terraform to .gitignore if not exists in .gitignore yet
```
# Terraform
**/.terraform/*
*.tfstate
*.tfstate.*
*.tfvars
.terraform.lock.hcl
crash.log
.terraform
```

## Create `infra` folder for terraform
- **DOCKER DEKTOP MUST BE OPEN**
- Create the tf scripts (acr, api, input_variables, outputs, providers, random, resource_group, web_app)
- After creating the different outputs via terraform Run the following in the terminal:

## Commands for Terraform in terminal
### Registration

Register to Azure first (if not done yet)
```
az provider register --namespace Microsoft.App
```

So I dont get an error when picking the docker image from the `api.tf` here:
```
  # Container settings
  template {
    container {
      name   = "api"
      image  = "mcr.microsoft.com/k8se/quickstart:latest"  <---- THIS ONE (docker image)
      cpu    = 1.0
      memory = "2Gi"
    }
  }
```

Check if registered
```
az provider show --namespace Microsoft.App --query "registrationState"
```
Should give back
```
"Registered"
```


### Orchestration & Automation
- Create `deploy_infra.sh`
- Create a `BASH` script.

- Go to docker-compose.yaml to change the image varaible on both backend and frontend services.
```
image: ${ACR_LOGIN_SERVER}/backend:${IMAGE_TAG:-latest}
```

In terminal: Execute `deploy_infra.sh`
```
chmod +x deploy_infra.sh
```

```
./deploy_infra.sh
```

Should get:
```
Terraform has been successfully initialized!
```