# Decision Matrix: Kubernetes Distribution Selection

**Decision ID**: DM-002  
**Date**: 2026-02-01  
**Author**: Platform Team Lead  
**Related RFC**: [RFC: Migration to Kubernetes](../rfcs/2026-02-01-migration-to-kubernetes.md)

---

## Context
We need to select a managed Kubernetes distribution for our migration from Heroku. The primary constraints are operational simplicity and cost optimization.

## Evaluation Matrix

| Criterion | Weight | **EKS** (Raw) | **EKS** (Wtd) | **GKE** (Raw) | **GKE** (Wtd) | **AKS** (Raw) | **AKS** (Wtd) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Control Plane Cost** | 4 | 2 | 8 | 4 | 16 | 5 | 20 |
| **Ecosystem (Terraform/Helm)** | 5 | 5 | 25 | 4 | 20 | 3 | 15 |
| **Autopilot / Serverless Mode** | 3 | 3 | 9 | 5 | 15 | 3 | 9 |
| **Networking (VPC CNI)** | 4 | 5 | 20 | 4 | 16 | 3 | 12 |
| **Observability Integration** | 3 | 4 | 12 | 5 | 15 | 3 | 9 |
| **Team Expertise** | 5 | 5 | 25 | 3 | 15 | 2 | 10 |
| **TOTAL SCORE** | - | - | **99** | - | **97** | - | **75** |

## Decision
**SELECTED: Amazon EKS**

Despite GKE having a free control plane and superior Autopilot mode, the team's existing expertise with AWS and the mature Terraform provider ecosystem make EKS the optimal choice for time-to-value.

## Trade-offs Accepted
- We will pay $73/month per cluster for the EKS control plane.
- We lose GKE's "Autopilot" mode but will use Karpenter for node scaling.

---

## See Also
*   **[Infrastructure as Code](../standards/infrastructure-as-code.md)**: Terraform standards for provisioning.
*   **[Cloud Provider Selection](../standards/cloud-provider-selection.md)**: Strategic cloud vendor analysis.
