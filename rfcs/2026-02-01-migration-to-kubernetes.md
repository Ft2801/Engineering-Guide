# RFC-005: Platform Migration from Heroku to Amazon EKS

**Status**: Draft  
**Author**: Staff Site Reliability Engineer  
**Date**: 2026-02-01  
**Stakeholders**: CTO, Platform Team, Finance Dept

---

## 1. Executive Summary
We propose migrating our core core services (`api-monolith`, `worker-cluster`) from Heroku Enterprise to a self-hosted Kubernetes cluster on Amazon EKS. While Heroku served us well during the startup phase, we have hit the "PaaS Ceiling" in terms of cost and networking flexibility.

## 2. Problem Statement

### 2.1 The "PaaS Tax" (Cost)
*   **Current Bill**: $45,000/month.
*   **Unit Cost**: We pay ~$500/month for a "Performance-L" dyno (14GB RAM). The underlying AWS equivalent (`r6g.large`) costs ~$40/month. We are paying a **1200% premium** for abstraction.

### 2.2 Shared Tenancy Limitations
*   **Noisy Neighbors**: We observe random P99 latency spikes (200ms -> 1500ms) on Heroku due to shared CPU credits.
*   **Networking**: We cannot easily peer with our AWS RDS VPC, incurring NAT Gateway charges.

## 3. Proposed Solution
Migrate to **Amazon EKS (Elastic Kubernetes Service)**.

### 3.1 Architecture
*   **Control Plane**: Managed EKS (High Availability).
*   **Data Plane**: Managed Node Groups using **Karpenter** for autoscaling.
*   **Ingress**: AWS Load Balancer Controller (ALB).

### 3.2 The "Day 2" Stack
Kubernetes is naked. We must build the platform:
*   **GitOps**: ArgoCD for deployment synchronization.
*   **Observability**: Prometheus Operator + Grafana Cloud.
*   **Security**: OPA Gatekeeper (Policy enforcement) + Falco (Runtime security).

## 4. Alternative Solutions

| Solution | Pros | Cons |
| :--- | :--- | :--- |
| **AWS ECS (Fargate)** | Simpler than K8s. Native IAM integration. | Vendor lock-in. Less ecosystem charts (Helm). |
| **Render / Fly.io** | Modern PaaS. Cheaper than Heroku. | Still imposes a "PaaS Tax". Migration path is risky for stateful workloads. |
| **Nomad (HashiCorp)** | Simple binary. Great batch processing. | Smaller ecosystem. Finding engineers is harder than K8s. |

## 5. Strategic Evaluation

### 5.1 Ecosystem (Kubernetes Wins)
Kubernetes is the "Operating System of the Cloud". The CNCF landscape provides ready-made solutions for every problem (e.g., Cert-Manager for SSL).

### 5.2 Hiring (The K8s Bump)
Hiring K8s engineers is expensive, but the talent pool is massive. Using ECS/Nomad restricts us to niche experts.

### 5.3 Complexity Analysis (The Trade-off)
We are trading **Financial Cost** for **Operational Complexity**.
*   *Before*: `git push heroku master` (Zero Ops).
*   *After*: Managing Helm charts, VPC CNI, IAM OIDC Roles.
*   *Mitigation*: We will hire 2 dedicated SREs before the migration starts.

## 6. Migration Roadmap

### Phase 1: The Foundation (Month 1-2)
*   Build VPC, EKS Cluster (Terraform).
*   Deploy "Walking Skeleton" (Hello World app) with ArgoCD.

### Phase 2: Dual Run (Month 3)
*   Deploy `api-monolith` to EKS but keep Traffic on Heroku.
*   Have `worker-cluster` consume 1% of Kafka events from EKS.

### Phase 3: The Cutover (Month 4)
*   Weighted DNS Routing (Route53) shift: 10% -> 50% -> 100%.

## 7. Cost Projection (Projected 3-Year TCO)

| Item | Heroku Cost | EKS Cost |
| :--- | :--- | :--- |
| **Compute** | $540,000/yr | $120,000/yr |
| **Eng Salary** | $0 (Devs do Ops) | $320,000/yr (2 SREs) |
| **Total** | **$540,000** | **$440,000** |

**Net Savings**: $100,000/yr + Infinite Scale Capability.

## 8. Decision
**APPROVED**. The org has crossed the "Scale Threshold" where building internal platform capability is cheaper than renting abstractions.
