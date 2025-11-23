from azure.storage.blob import BlobServiceClient
import os

connection_string = "YOUR_CONNECTION_STRING"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def upload_build_artifact(local_file, blob_name):
    blob_client = blob_service_client.get_blob_client(
        container="build-artifacts",
        blob=blob_name
    )
    
    with open(local_file, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    
    print(f"Uploaded: {blob_name}")

# Example: Upload requirements.txt
upload_build_artifact("requirements.txt", "python-api/requirements.txt")

# List all artifacts
container_client = blob_service_client.get_container_client("build-artifacts")
blobs = container_client.list_blobs()
print("\nStored artifacts:")
for blob in blobs:
    print(f"- {blob.name} ({blob.size} bytes)")
