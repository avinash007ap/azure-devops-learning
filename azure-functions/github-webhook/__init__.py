import logging
import json
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('GitHub webhook received')

    try:
        req_body = req.get_json()
        event_type = req.headers.get('X-GitHub-Event')
        
        # Log to Cosmos DB
        endpoint = os.environ["COSMOS_ENDPOINT"]
        key = os.environ["COSMOS_KEY"]
        client = CosmosClient(endpoint, key)
        
        database = client.get_database_client("devops-metrics")
        container = database.get_container_client("github-events")
        
        container.create_item(body={
            'id': req_body.get('id', 'unknown'),
            'event_type': event_type,
            'repository': req_body.get('repository', {}).get('full_name'),
            'timestamp': datetime.now().isoformat()
        })
        
        return func.HttpResponse("Webhook processed", status_code=200)
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse("Error", status_code=500)
