Day 3: Azure DevOps + Blob Storage Analytics
Estimated Cost: $15-20
Time: 6 hours

Assignment 3.1: Azure Blob Storage for Artifacts

```bash
# Create storage account
az storage account create \
  --name devopslearningstorage \
  --resource-group devops-learning-rg \
  --location eastus \
  --sku Standard_LRS

# Create container for build artifacts
az storage container create \
  --name build-artifacts \
  --account-name devopslearningstorage
```
Deliverable: Storage account with container

Assignment 3.2: Automated Artifact Upload
File: upload-artifacts.py
Deliverable: Automated artifact management

Assignment 3.3: Azure DevOps Pipeline Integration
File: .azure-pipelines/build-and-store.yml
Deliverable: Azure DevOps pipeline with blob storage
