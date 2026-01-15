# Cloud Provider Selection Strategy

## 1. Introduction
The Cloud is not a commodity. Each provider dictates a distinct architectural style and hiring pool. We avoid "Multi-Cloud" for the sake of it, favoring "Cloud Neutrality" where possible but defaulting to a Primary Cloud.

> **Principle**: "Multi-Cloud is a headache, not a strategy. Pick one, but be ready to leave."

---

## 2. The Big Three Assessment

### 2.1 AWS (Amazon Web Services)
*   **Best For**: General Purpose, "Enterprise Standard".
*   **Pros**: Largest ecosystem (Terraform providers, StackOverflow answers), most mature operational tools.
*   **Cons**: Expensive "hidden" costs (NAT Gateways), User Experience is notoriously complex.

### 2.2 GCP (Google Cloud Platform)
*   **Best For**: Data Engineering, Kubernetes, AI.
*   **Pros**: **BigQuery** (best-in-class operational ease), GKE (purest K8s implementation), Global VPC (networking is simpler).
*   **Cons**: Smaller talent pool. Support can be opaque.

### 2.3 Azure (Microsoft)
*   **Best For**: Integration with Active Directory / Enterprise Licensing.
*   **Pros**: Perfect alignment with .NET/Windows ecosystems. Hybrid cloud features.
*   **Cons**: UX lags behind AWS/GCP.

### 2.4 On-Premise / Bare Metal (Hetzner/Equinix)
*   **Best For**: Predictable massive bandwidth/CPU workloads (e.g., Video Encoding).
*   **Pros**: 1/10th the cost of AWS for raw compute.
*   **Cons**: You own the hardware failures. High operational overhead.

---

## 3. The "Cloud Exit" Strategy (Lock-in Mitigation)

We accept Vendor Lock-in on **IaaS** but resist it on **PaaS** unless the value is extreme.

*   **Commodity (Safe to Lock-in)**: VMs (EC2), Object Storage (S3), Managed Postgres (RDS). Checkered flag: Easy to migrate (Standard APIs).
*   **Proprietary (High Risk)**: DynamoDB, Firestore, Lambda, Step Functions. Checkered flag: Requires complete code rewrite to leave.

**Policy**: Only use Proprietary Services (like DynamoDB) if they offer a >10x advantage over an Open Alternative (like ScyllaDB/Cassandra).

---

## 4. Multi-Cloud Architecture
If regulators mandate a "Secondary Cloud" (e.g., Banking):
1.  **Workload Portability**: Every app must be containerized (Docker).
2.  **Data Replication**: Use storage abstraction layers (e.g., MinIO) to replicate S3 buckets to Azure Blob.
3.  **Traffic Routing**: DNS Failover (Cloudflare) to switch traffic.

---

## See Also
*   **[Decision Matrix: Kubernetes Distribution](../decisions/2026-02-01-kubernetes-distribution.md)**: EKS vs GKE vs AKS.
*   **[Infrastructure as Code](./infrastructure-as-code.md)**: Terraform for multi-cloud provisioning.
*   **[Total Cost of Ownership](../guides/total-cost-of-ownership.md)**: FinOps and cloud cost analysis.
*   **[Green Computing](./green-computing.md)**: ARM instances and carbon-aware region selection.
*   **[Vendor Risk Assessment](../guides/vendor-risk-assessment.md)**: Exit strategy evaluation.

