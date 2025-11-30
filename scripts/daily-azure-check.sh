#!/bin/bash
# save as: daily-azure-check.sh
# run: bash daily-azure-check.sh

echo "=== Azure Daily Health Check ==="

# 1. Verify login & subscription
az account show --output table

# 2. Check credits balance
echo "=== Credits & Balance ==="
az billing-benefit list --query "[].{Name:name, Balance:balance}" -o table || \
echo "Use Cost Management in Portal if CLI doesn't show credits"

# 3. Register required providers (safe to re-run daily)
for ns in Microsoft.Web \
          Microsoft.Storage \
          Microsoft.DocumentDB \
          Microsoft.ContainerService \
          Microsoft.ContainerRegistry \
          Microsoft.Compute \
          Microsoft.KeyVault \
          Microsoft.CostManagement; do
  echo "Checking provider: $ns"
  state=$(az provider show --namespace $ns --query "registrationState" -o tsv)
  if [ "$state" != "Registered" ]; then
    echo " -> Registering $ns..."
    az provider register --namespace $ns
  else
    echo " -> Already registered"
  fi
done

# 4. Check quotas (example: VM cores, AKS)
echo "=== Quota Check ==="
az vm list-usage --location eastus -o table
az aks list --output table

echo "=== Done. All providers checked, quotas listed. ==="
