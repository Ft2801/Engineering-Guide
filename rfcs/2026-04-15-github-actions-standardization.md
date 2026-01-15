# RFC-025: Adopting GitHub Actions for CI/CD Standardization

**Status**: Approved  
**Author**: DevOps Lead  
**Date**: 2026-04-15  
**Stakeholders**: All Engineering Teams  
**Related Decision**: [Decision Matrix: CI/CD Platform](../decisions/2026-04-01-cicd-platform.md)

---

## 1. Executive Summary
We propose consolidating all CI/CD pipelines onto **GitHub Actions**, deprecating Jenkins and CircleCI. This will reduce operational overhead and improve developer experience through native GitHub integration.

## 2. Problem Statement
*   **Fragmentation**: Teams use Jenkins (legacy), CircleCI (frontend), and GitHub Actions (new projects).
*   **Maintenance Burden**: Jenkins requires dedicated infrastructure and plugin management.
*   **Context Switching**: Developers must learn 3 different YAML syntaxes.

## 3. Proposed Solution
Standardize on **GitHub Actions** for all CI/CD workflows.

### 3.1 Migration Strategy
1.  **Phase 1 (Month 1)**: Create reusable workflow templates for common patterns (Build, Test, Deploy).
2.  **Phase 2 (Month 2-3)**: Migrate all CircleCI pipelines (~15 repos).
3.  **Phase 3 (Month 4-6)**: Migrate Jenkins pipelines (~25 repos) and decommission Jenkins.

### 3.2 Reusable Workflows
We will create a central `.github` repository with:
*   `build-docker.yml`: Standard Docker image build.
*   `deploy-eks.yml`: Kubernetes deployment to EKS.
*   `security-scan.yml`: SAST + SCA pipeline.

## 4. Cost Analysis

| Platform | Monthly Cost | Notes |
| :--- | :--- | :--- |
| **Jenkins** | $2,400 | EC2 instances + maintenance |
| **CircleCI** | $1,200 | Paid tier |
| **GitHub Actions** | $800 | Using self-hosted runners on EKS |

**Annual Savings**: ~$33,600

## 5. Decision
**APPROVED**. We proceed with the migration starting Q2 2026.

---

## See Also
*   **[Decision Matrix: CI/CD Platform](../decisions/2026-04-01-cicd-platform.md)**: Quantitative evaluation.
*   **[AppSec Lifecycle](../standards/appsec-lifecycle.md)**: Integrating security scans.
*   **[Testing & QA Standards](../standards/testing-and-quality-assurance.md)**: Test execution in CI.
