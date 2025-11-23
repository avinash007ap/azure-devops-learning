# Day 2: Azure Cosmos DB + Azure Functions
<u>Estimated Cost: $25-35</u><br>
<u>Time: 6 hours</u><br>

### Assignment 2.1: Create Cosmos DB Free Tier

```bash
# Create Cosmos DB account (free tier - 1000 RU/s, 25 GB)
az cosmosdb create \
  --name devops-learning-cosmos \
  --resource-group devops-learning-rg \
  --enable-free-tier true \
  --default-consistency-level Session
```
**Note:** Free tier provides lifetime free usage​

**Deliverable:** Cosmos DB account created

### Assignment 2.2: Python Script - DevOps Metrics Storage

**File:** `cosmos-devops-metrics.py`
**Deliverable:** DevOps metrics stored in Cosmos DB

### Assignment 2.3: Azure Function - GitHub Webhook Handler


```bash
# Create Azure Function App
az functionapp create \
  --resource-group devops-learning-rg \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.11 \
  --functions-version 4 \
  --name devops-webhook-handler \
  --storage-account devopslearningstorage
```

**File:** `azure-functions/github-webhook/__init__.py`
**Deliverable:** Azure Function receiving GitHub webhooks