# Azure DevOps Learning Project

## Overview
12-day intensive Azure DevOps learning project implementing containerized applications, CI/CD pipelines, and Microsoft Graph API integration.

## Architecture
```
GitHub Repository
    ↓
GitHub Actions (CI/CD)
    ↓
Azure Container Registry
    ↓
Azure Kubernetes Service
    ↓
Microsoft Graph API (Personal Account)
    ↓
OneDrive / Outlook Integration
```

## Technologies
- **Cloud:** Azure (AKS, ACR, Cosmos DB, Functions, Blob Storage)
- **Containers:** Docker, Kubernetes
- **CI/CD:** GitHub Actions, Azure DevOps Pipelines
- **Languages:** Python 3.11
- **Testing:** pytest, pytest-cov
- **APIs:** Microsoft Graph API

## Project Structure
```
├── .github/workflows/       # GitHub Actions
├── graph-client/           # Python Graph API client
├── k8s/                    # Kubernetes manifests
├── tests/                  # pytest test suite
├── azure-functions/        # Azure Functions code
├── portfolio/              # Static web app
└── docs/                   # Documentation
```

## Setup Instructions
### Prerequisites
```
# Azure CLI
az login

# Kubectl
kubectl version --client

# Docker
docker --version
```

### Deployment
```
# 1. Create Azure resources
./scripts/setup-azure-resources.sh

# 2. Build and push Docker image
./scripts/build-and-push.sh

# 3. Deploy to AKS
kubectl apply -f k8s/
```

## Cost Analysis
| Service | Cost (12 days) | Post-Credits |
|---------|----------------|--------------|
| AKS | $30-40 | Stop cluster |
| Cosmos DB | $25-35 | Free tier (1000 RU/s) |
| Blob Storage | $15-20 | ~$2/month |
| Static Web Apps | $0 | Free tier |
| **Total** | **$100-135** | **~$2/month** |

## Learning Outcomes
- ✅ Containerized Python applications
- ✅ Kubernetes orchestration on AKS
- ✅ CI/CD with GitHub Actions
- ✅ Microsoft Graph API (delegated auth)
- ✅ Azure Cosmos DB integration
- ✅ Cross-cloud automation (AWS + Azure)

## Certifications Targeted
- AZ-104: Azure Administrator
- AZ-400: DevOps Engineer Expert
- CKA: Certified Kubernetes Administrator

## Contact
- LinkedIn: [Your Profile]
- GitHub: [Your Username]
- Email: your.email@example.com
```

Ready to start? Let me know if you need clarification on any assignment! 🚀
