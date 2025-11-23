from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient

# This ONLY works with organizational accounts
# Personal accounts CANNOT use application permissions

class OrgGraphClient:
    def __init__(self, tenant_id, client_id, client_secret):
        self.credential = ClientSecretCredential(
            tenant_id=tenant_id,  # NOT "consumers"
            client_id=client_id,
            client_secret=client_secret
        )
        self.graph_client = GraphServiceClient(
            credentials=self.credential,
            scopes=["https://graph.microsoft.com/.default"]
        )
    
    async def get_all_users(self):
        # Requires User.Read.All application permission
        users = await self.graph_client.users.get()
        return users.value

# THIS WILL FAIL WITH PERSONAL ACCOUNTS
# Use delegated permissions instead (see Day 1)
