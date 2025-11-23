# Azure DevOps Accelerator - 12-Day Implementation Plan
## Overview
**Duration:** _12 days (November 19 - November 30, 2025)_ <br>
**Azure Credits:** _$200 (strategic consumption)_ <br>
**Focus:** _Azure services, containerization, CI/CD, Graph API with personal account_ <br>
**Outcome:** _Production-ready DevOps portfolio with GitHub Actions, Docker, and Azure integration_ <br>

---

### Prerequisites Setup - Required Accounts & Tools
```bash
# Verify installations
python --version  # 3.10+
docker --version
kubectl version --client
az --version  # Azure CLI

# Install Python packages
pip install azure-identity msgraph-sdk azure-storage-blob \
    azure-cosmos pandas openpyxl python-pptx requests

# GitHub CLI (optional but recommended)
gh --version
Azure Account Verification
```

```bash
# Login to Azure
az login

# Check credit balance
az account show --query "{Name:name, SubscriptionId:id, State:state}"

# Set default subscription
az account set --subscription "YOUR_SUBSCRIPTION_ID"
```

Personal Microsoft Account App Registration
**Note:** Personal accounts CAN register apps but with delegated permissions only (not application permissions).​

###### Steps:
1. Navigate to: https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade
2. New registration
    - Name: DevOps-Personal-Graph-API
    - Supported account types: Accounts in any organizational directory and personal Microsoft accounts
    - Redirect URI: http://localhost:8000 (for local testing)
3. Certificates & secrets → New client secret (6 months)
4. API Permissions → Add permission → Microsoft Graph → Delegated permissions:
    - User.Read
    - Files.ReadWrite
    - Mail.Read
    - offline_access

### Phase 1: Days 1-4 (Azure Credits Intensive)
Goal: Consume ~$120-140 of credits on high-value Azure services

### Phase 2: Days 5-8 (Free Tier + GitHub Actions)
Goal: Build CI/CD pipelines using free services

### Phase 3: Days 9-12 (Portfolio + Cleanup)
Goal: Create deliverables and optimize costs
