from azure.cosmos import CosmosClient, PartitionKey
import os
from datetime import datetime

# Connection details
endpoint = "https://devops-learning-cosmos.documents.azure.com:443/"
key = "YOUR_PRIMARY_KEY"  # Get from Azure Portal

client = CosmosClient(endpoint, key)

# Create database
database_name = "devops-metrics"
database = client.create_database_if_not_exists(id=database_name)

# Create container
container_name = "pipeline-runs"
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/project"),
    offer_throughput=400  # Within free tier
)

# Insert sample pipeline data
def log_pipeline_run(project, status, duration):
    item = {
        'id': f"{project}-{datetime.now().timestamp()}",
        'project': project,
        'status': status,
        'duration_seconds': duration,
        'timestamp': datetime.now().isoformat()
    }
    container.create_item(body=item)
    print(f"Logged: {item}")

# Sample data
log_pipeline_run("aws-automation", "success", 245)
log_pipeline_run("kubernetes-deployment", "failed", 180)
log_pipeline_run("python-api", "success", 320)

# Query data
query = "SELECT * FROM c WHERE c.status = 'success'"
items = list(container.query_items(query=query, enable_cross_partition_query=True))
print(f"\nSuccessful runs: {len(items)}")
for item in items:
    print(f"- {item['project']}: {item['duration_seconds']}s")
