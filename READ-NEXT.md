
## Free Services to Continue Learning (Post-12 Days)

### Always Free Azure Services[2][1]
1. **Cosmos DB:** 1000 RU/s, 25 GB (lifetime free)
2. **Static Web Apps:** 100 GB bandwidth/month
3. **Functions:** 1M executions/month
4. **Blob Storage:** 5 GB LRS hot
5. **Azure DevOps:** 5 users, unlimited private repos

### GitHub Free Tier
1. **GitHub Actions:** 2,000 minutes/month
2. **GitHub Packages:** 500 MB storage
3. **GitHub Pages:** Static site hosting

***

## Key Differences: Personal vs Organizational Microsoft Accounts

| Feature | Personal Account | Organizational Account |
|---------|------------------|------------------------|
| App Registration | ✅ Yes | ✅ Yes |
| Delegated Permissions | ✅ Supported | ✅ Supported |
| Application Permissions | ❌ Not Supported | ✅ Supported |
| Tenant | `consumers` | Custom tenant ID |
| Auth Flow | Device Code Flow | Client Credentials |
| Admin Consent | ❌ Not Available | ✅ Required |
| Graph API Scope | Limited (OneDrive, Mail) | Full (Users, Teams, etc.) |

**Recommendation:** Focus on delegated permissions for personal account; use organizational context only for comparison.[3][4]

***

## Estimated Cost Breakdown

| Phase | Days | Services | Estimated Cost |
|-------|------|----------|----------------|
| Phase 1 | 1-4 | AKS, Cosmos DB, VM, Blob | $100-135 |
| Phase 2 | 5-8 | GitHub Actions, Free tier | $0 |
| Phase 3 | 9-12 | Documentation, Cleanup | $0 |
| **Total** | **12** | | **$100-135** |
| **Remaining Credits** | | | **$65-100** |

### Post-12 Days Monthly Cost
- Blob Storage: ~$2/month
- Cosmos DB: $0 (free tier)
- Static Web App: $0 (free tier)
- **Total: ~$2/month**

***

## Questions Before Starting?

1. **Should I extend M365 Personal?** No - this plan works entirely with Azure and free alternatives.[1][2]
2. **What about OneDrive access?** Personal Graph API with delegated permissions provides OneDrive access.[3]
3. **Can I restart AKS later?** Yes: `az aks start --resource-group devops-learning-rg --name devops-cluster`
4. **Will credits expire?** Yes, after 30 days from activation (November 19 - December 19).[6]