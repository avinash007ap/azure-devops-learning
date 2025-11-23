Day 5: GitHub Actions + ACR Integration
Estimated Cost: $0 (using GitHub free tier)
Time: 5 hours

Assignment 5.1: GitHub Actions Workflow - Docker Build
File: .github/workflows/docker-build-push.yml

Setup GitHub Secrets:
```bash
# Get ACR credentials
az acr credential show --name devopslearningacr2025

# Add to GitHub: Settings → Secrets → Actions
# ACR_USERNAME: <username>
# ACR_PASSWORD: <password>
```
Deliverable: Automated Docker builds on push

Assignment 5.2: Multi-Stage Build Optimization
File: graph-client/Dockerfile.optimized
Deliverable: Optimized Docker image (reduced size)