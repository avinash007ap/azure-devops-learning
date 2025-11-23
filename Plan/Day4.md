Day 4: Azure VM + Application Permissions Example
Estimated Cost: $30-40
Time: 6 hours

Assignment 4.1: Create Ubuntu VM for Testing
```bash
# Create VM (B2s for cost efficiency)
az vm create \
  --resource-group devops-learning-rg \
  --name devops-test-vm \
  --image Ubuntu2204 \
  --size Standard_B2s \
  --admin-username azureuser \
  --generate-ssh-keys

# Get public IP
az vm show -d -g devops-learning-rg -n devops-test-vm --query publicIps -o tsv
```
Deliverable: VM running Ubuntu

Assignment 4.2: Application Permissions Example (Organizational Context)
Note: This demonstrates the difference - requires organizational account.​

File: graph_app_permissions.py (For comparison only)

Documentation: Create comparison document explaining delegated vs application permissions

Deliverable: Documentation and working delegated example
