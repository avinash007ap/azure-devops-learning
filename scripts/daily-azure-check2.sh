#!/bin/bash
# save as: daily-azure-check.sh
# run: bash daily-azure-check.sh

echo "=== Azure Daily Health Check ==="

# 1. Verify login & subscription
az account show --output table

# 2. Check credits balance (MCA only)
echo "=== Credits & Balance ==="
if az billing balance show --billing-account-name $(az billing account list --query "[0].name" -o tsv) -o table 2>/dev/null; then
  echo "Credits balance shown above (MCA subscription)."
else
  echo "Credits balance not available via CLI. Showing recent consumption instead..."
  az consumption usage list --top 5 --query "[].{Date:usageStart, Service:instanceName, Cost:pretaxCost}" -o table
fi

# 3. Register required providers (safe to re-run daily)
providers=(
  Microsoft.Web
  Microsoft.Storage
  Microsoft.DocumentDB
  Microsoft.ContainerService
  Microsoft.ContainerRegistry
  Microsoft.Compute
  Microsoft.KeyVault
  Microsoft.CostManagement
  Microsoft.Authorization
  Microsoft.Resources
)

echo "=== Provider Registration Check ==="
printf "\n%-30s %-15s\n" "Provider Namespace" "Status"
printf "%-30s %-15s\n" "------------------" "------"

for ns in "${providers[@]}"; do
  state=$(az provider show --namespace $ns --query "registrationState" -o tsv 2>/dev/null)
  if [ "$state" != "Registered" ]; then
    echo " -> Registering $ns..."
    az provider register --namespace $ns >/dev/null
    state="Registering"
  fi
  printf "%-30s %-15s\n" "$ns" "$state"
done

# 4. Check quotas (example: VM cores, AKS)
echo "=== Quota Check ==="
az vm list-usage --location eastus -o table
az aks list --output table

echo -e "\n=== Done. Providers checked, credits/consumption listed, quotas shown. ==="
