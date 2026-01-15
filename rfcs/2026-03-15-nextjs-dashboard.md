# RFC-028: Adopting Next.js for B2B Dashboard

**Status**: Approved  
**Author**: Frontend Architect  
**Date**: 2026-03-15  
**Stakeholders**: Frontend Team, Product  
**Related Decision**: [Decision Matrix: Frontend Framework](../decisions/2026-03-01-frontend-framework.md)

---

## 1. Executive Summary
We propose using **Next.js (App Router)** for the new B2B SaaS Dashboard. This framework provides the best balance of SEO capability, developer experience, and ecosystem support.

## 2. Problem Statement
*   **SEO Requirements**: The marketing pages must be indexed by search engines.
*   **Complex State**: The dashboard requires real-time data updates and complex filtering.
*   **Performance**: Target LCP (Largest Contentful Paint) < 2.5 seconds.

## 3. Proposed Solution
Adopt **Next.js 14+** with the App Router architecture.

### 3.1 Architecture
*   **React Server Components (RSC)**: For data fetching on the server (reduces client bundle).
*   **Streaming SSR**: Progressive rendering for perceived performance.
*   **API Routes**: BFF (Backend for Frontend) pattern for aggregating microservice calls.

### 3.2 Styling Stack
*   **Tailwind CSS**: Utility-first styling.
*   **Radix UI**: Accessible headless components.
*   **Framer Motion**: Animations.

## 4. Deployment
*   **Platform**: Vercel (zero-config, automatic preview deployments).
*   **Alternative**: Self-hosted on EKS with `next start`.

## 5. Risk Analysis

| Risk | Mitigation |
| :--- | :--- |
| **Vercel Vendor Lock-in** | Next.js is open-source. Self-hosting is always available. |
| **App Router Maturity** | Stable since Next.js 13.4. Production-tested by Vercel customers. |

## 6. Decision
**APPROVED**. Development begins in Sprint 12.

---

## See Also
*   **[Decision Matrix: Frontend Framework](../decisions/2026-03-01-frontend-framework.md)**: Quantitative evaluation.
*   **[Frontend Selection Criteria](../standards/frontend-selection-criteria.md)**: Core Web Vitals and SSR strategies.
*   **[API Design Styleguide](../standards/api-design-styleguide.md)**: BFF pattern for mobile optimization.
