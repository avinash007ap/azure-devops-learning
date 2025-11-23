Day 7: Free Azure Services - Static Web Apps
Estimated Cost: $0 (free tier)
Time: 5 hours

Assignment 7.1: DevOps Portfolio Static Site
File: portfolio/index.html
```bash
# Install SWA CLI
npm install -g @azure/static-web-apps-cli

# Deploy
az staticwebapp create \
  --name devops-portfolio \
  --resource-group devops-learning-rg \
  --source https://github.com/yourusername/azure-devops-learning \
  --location eastus \
  --branch main \
  --app-location "/portfolio" \
  --output-location "/"
```
Deliverable: Live portfolio website

