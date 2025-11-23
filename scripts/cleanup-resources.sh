#!/bin/bash

echo "Starting Azure resource cleanup..."

# Stop AKS cluster (don't delete - preserve config)
echo "Stopping AKS cluster..."
az aks stop --resource-group devops-learning-rg --name devops-cluster

# Delete VM (expensive resource)
echo "Deleting VM..."
az vm delete --resource-group devops-learning-rg --name devops-test-vm --yes

# Keep Cosmos DB (free tier - no cost)
echo "Keeping Cosmos DB (free tier)..."

# Keep Blob Storage (minimal cost)
echo "Keeping Blob Storage..."

# Keep Static Web App (free tier)
echo "Keeping Static Web App..."

# Delete ACR (if not needed)
read -p "Delete Azure Container Registry? (y/n): " delete_acr
if [ "$delete_acr" = "y" ]; then
    az acr delete --name devopslearningacr2025 --yes
fi

echo "Cleanup complete!"
echo ""
echo "Remaining resources (low/no cost):"
echo "  - Cosmos DB (free tier)"
echo "  - Blob Storage (~$2/month)"
echo "  - Static Web App (free tier)"
echo "  - AKS (stopped, restart with 'az aks start')"