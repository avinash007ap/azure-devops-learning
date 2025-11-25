from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient
import asyncio
import os

client_id = os.getenv("CLIENT_ID")

class PersonalGraphClient:
    def __init__(self):
        # For personal accounts, use device code flow
        self.credential = DeviceCodeCredential(
            client_id=client_id,
            tenant_id="consumers"  # For personal accounts
        )
        self.graph_client = GraphServiceClient(
            credentials=self.credential,
            scopes=["User.Read", "Files.ReadWrite", "Mail.Read"]
        )
    
    async def get_my_profile(self):
        try:
            me = await self.graph_client.me.get()
            print(f"Logged in as: {me.display_name}")
            return me
        except Exception as e:
            print(f"Error: {e}")
    
    async def list_onedrive_files(self):
        try:
            files = await self.graph_client.me.drive.root.children.get()
            for file in files.value[:10]:
                print(f"- {file.name} ({file.size} bytes)")
        except Exception as e:
            print(f"Error: {e}")

async def main():
    client = PersonalGraphClient()
    await client.get_my_profile()
    await client.list_onedrive_files()

if __name__ == "__main__":
    asyncio.run(main())
