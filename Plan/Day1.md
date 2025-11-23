# Day 1: Azure Kubernetes Service (AKS) + Container Registry
<u>Estimated Cost: $30-40</u><br>
<u>Time: 6 hours</u>

### Assignment 1.1: Create AKS Cluster

```bash
# Create resource group
az group create --name devops-learning-rg --location eastus

# Create Azure Container Registry (ACR)
az acr create --resource-group devops-learning-rg \
  --name devopslearningacr2025 --sku Basic

# Create AKS cluster (2 nodes for cost optimization)
az aks create \
  --resource-group devops-learning-rg \
  --name devops-cluster \
  --node-count 2 \
  --node-vm-size Standard_B2s \
  --attach-acr devopslearningacr2025 \
  --generate-ssh-keys

# Get credentials
az aks get-credentials --resource-group devops-learning-rg --name devops-cluster
```

**Deliverable:** _AKS cluster running with ACR integration_

### Assignment 1.2: Dockerize Python Graph API Client
**File:** `graph-client/Dockerfile`

**File:** `graph-client/graph_auth_delegated.py`

***Build and push to ACR:***

```bash
cd graph-client

# Build Docker image
docker build -t devopslearningacr2025.azurecr.io/graph-client:v1 .

# Login to ACR
az acr login --name devopslearningacr2025

# Push image
docker push devopslearningacr2025.azurecr.io/graph-client:v1
```

**Deliverable:** _Docker image in ACR_

### Assignment 1.3: Deploy to AKS
**File:** `k8s/graph-client-deployment.yaml`

**Deploy:**

```bash
kubectl apply -f k8s/graph-client-deployment.yaml
kubectl get pods
kubectl logs -f deployment/graph-client
```

**Deliverable:** _Running pod in AKS_

