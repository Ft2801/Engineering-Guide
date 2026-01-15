# Decision Matrix: CI/CD Platform Selection

**Decision ID**: DM-005  
**Date**: 2026-04-01  
**Author**: DevOps Lead  
**Related Standard**: [Testing & Quality Assurance](../standards/testing-and-quality-assurance.md)

---

## Context
We need to consolidate our CI/CD tooling. Currently, teams use a mix of Jenkins, CircleCI, and GitHub Actions. We want to standardize on a single platform for maintainability.

## Evaluation Matrix

| Criterion | Weight | **GitHub Actions** (Raw) | **GitHub Actions** (Wtd) | **GitLab CI** (Raw) | **GitLab CI** (Wtd) | **CircleCI** (Raw) | **CircleCI** (Wtd) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Native Git Integration** | 5 | 5 | 25 | 5 | 25 | 4 | 20 |
| **Marketplace / Actions** | 4 | 5 | 20 | 3 | 12 | 4 | 16 |
| **Self-Hosted Runners** | 3 | 4 | 12 | 5 | 15 | 3 | 9 |
| **Cost (at scale)** | 4 | 3 | 12 | 4 | 16 | 3 | 12 |
| **Matrix Builds** | 3 | 5 | 15 | 4 | 12 | 5 | 15 |
| **Security (OIDC)** | 4 | 5 | 20 | 4 | 16 | 4 | 16 |
| **TOTAL SCORE** | - | - | **104** | - | **96** | - | **88** |

## Decision
**SELECTED: GitHub Actions**

GitHub Actions wins due to its native integration with our existing GitHub repositories and the extensive marketplace of pre-built actions.

## Implementation Notes
- Use **Reusable Workflows** for DRY (Don't Repeat Yourself) pipelines.
- Deploy **Self-Hosted Runners** on EKS for cost optimization on large builds.
- Implement **OIDC Authentication** to AWS (no long-lived secrets).

---

## See Also
*   **[AppSec Lifecycle](../standards/appsec-lifecycle.md)**: Integrating SAST/DAST into CI.
*   **[Infrastructure as Code](../standards/infrastructure-as-code.md)**: Terraform in CI pipelines.
