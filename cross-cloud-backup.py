import boto3
from azure.storage.blob import BlobServiceClient
import os

# AWS S3 setup
s3_client = boto3.client('s3')
bucket_name = 'your-aws-backup-bucket'

# Azure Blob setup
connection_string = os.environ['AZURE_STORAGE_CONNECTION_STRING']
blob_service = BlobServiceClient.from_connection_string(connection_string)
container_name = 'aws-backups'

def backup_s3_to_azure():
    # List S3 objects
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    
    for obj in response.get('Contents', []):
        key = obj['Key']
        print(f"Backing up: {key}")
        
        # Download from S3
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
        content = s3_object['Body'].read()
        
        # Upload to Azure
        blob_client = blob_service.get_blob_client(
            container=container_name,
            blob=f"s3-backup/{key}"
        )
        blob_client.upload_blob(content, overwrite=True)
        
        print(f"✓ Backed up: {key}")

if __name__ == "__main__":
    backup_s3_to_azure()
