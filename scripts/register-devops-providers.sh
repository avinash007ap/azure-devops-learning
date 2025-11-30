#!/bin/bash
# save as: register-devops-providers.sh
# run: bash register-devops-providers.sh

echo "=== Azure DevOps Accelerator Provider Registration ==="

# List of required providers from your stack document
providers=(
  Microsoft.Web               # Functions + Static Web Apps
  Microsoft.Storage           # Blob Storage
  Microsoft.DocumentDB        # Cosmos DB
  Microsoft.ContainerService  # AKS
  Microsoft.ContainerRegistry # ACR
  Microsoft.Compute           # VMs
  Microsoft.KeyVault          # Secrets
  Microsoft.CostManagement    # Cost tracking
  Microsoft.Authorization     # RBAC / Service Principals
  Microsoft.Resources         # Resource Groups (usually auto-registered)
)

# Track results
printf "\n%-30s %-15s\n" "Provider Namespace" "Status"
printf "%-30s %-15s\n" "------------------" "------"

for ns in "${providers[@]}"; do
  state=$(az provider show --namespace $ns --query "registrationState" -o tsv 2>/dev/null)
  if [ "$state" != "Registered" ]; then
    echo "Registering $ns..."
    az provider register --namespace $ns >/dev/null
    state="Registering"
  fi
  printf "%-30s %-15s\n" "$ns" "$state"
done

echo -e "\n=== Done. Providers checked and registered where needed. ==="
echo "Tip: Run 'az provider list --output table' to see full details."
