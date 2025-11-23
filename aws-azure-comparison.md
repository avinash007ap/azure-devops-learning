# AWS boto3 vs Azure SDK - DevOps Operations

## S3 vs Blob Storage

### List Objects
**AWS (boto3)**
```
import boto3
s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket='my-bucket')
for obj in response['Contents']:
    print(obj['Key'])
```

**Azure**
```
from azure.storage.blob import BlobServiceClient
blob_service = BlobServiceClient.from_connection_string(conn_str)
container_client = blob_service.get_container_client("my-container")
for blob in container_client.list_blobs():
    print(blob.name)
```

### Upload File
**AWS (boto3)**
```
s3.upload_file('local.txt', 'my-bucket', 'remote.txt')
```

**Azure**
```
blob_client = blob_service.get_blob_client("my-container", "remote.txt")
with open("local.txt", "rb") as data:
    blob_client.upload_blob(data)
```

## RDS vs Azure SQL

### Create Database Instance
**AWS (boto3)**
```
rds = boto3.client('rds')
rds.create_db_instance(
    DBInstanceIdentifier='mydb',
    DBInstanceClass='db.t3.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='password'
)
```

**Azure**
```
az sql server create \
  --name myserver \
  --resource-group mygroup \
  --location eastus \
  --admin-user admin \
  --admin-password password

az sql db create \
  --resource-group mygroup \
  --server myserver \
  --name mydb \
  --service-objective S0
```

## EC2 vs Azure VMs

### Launch Instance
**AWS (boto3)**
```
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-xxxxxxxx',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)
```

**Azure**
```
az vm create \
  --resource-group mygroup \
  --name myvm \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser