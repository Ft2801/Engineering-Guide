# RFC-021: Improving Service Discovery (Internal Developer Portal)

**Status**: Draft  
**Author**: Platform Engineer  
**Date**: 2026-07-01  
**Stakeholders**: All Engineering Teams

---

## 1. Executive Summary
We propose adopting **Backstage** (by Spotify) as our central Internal Developer Portal (IDP). This will solve the "Discovery Debt" where engineers spend hours searching for documentation, API owners, or service health status.

## 2. Problem Statement
*   **Documentation Fragmentation**: Docs are scattered across READMEs, Notion, and Jira.
*   **Ownership Mystery**: When a service fails, it takes ~20 minutes to find the responsible team.
*   **Onboarding Slowness**: New hires spend days finding the right repositories and tools.

## 3. Proposed Solution
Implement **Backstage** as the "Single Pane of Glass" for the engineering organization.

### 3.1 Core Features
1.  **Software Catalog**: A searchable list of all 150+ microservices.
2.  **TechDocs**: Renders markdown documentation from git directly in the browser with unified search.
3.  **Software Templates (Scaffolding)**: Creating a "New Go Service" will be a 1-click process that generates a repo with our best practices pre-configured.

## 4. Implementation Strategy

### Phase 1: The Catalog (Month 1)
Add a `catalog-info.yaml` to the top 20 critical services.
```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: billing-service
  description: Handles all subscription billing
spec:
  type: service
  owner: billing-team
  lifecycle: production
```

### Phase 2: Scaffolding (Month 2)
Create templates for our standardized stacks (Go, React, Flutter).

## 5. Strategic Evaluation
*   **Productivity**: Estimate a 15% reduction in "context switching" time.
*   **Standardization**: Templates ensure new services are compliant with our DevSecOps and Observability standards from Day 0.

## 6. Decision
**APPROVED**. We will start with a PoC (Proof of Concept) on the Platform Team's internal tools.
