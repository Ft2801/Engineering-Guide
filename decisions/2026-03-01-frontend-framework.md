# Decision Matrix: Frontend Framework Selection

**Decision ID**: DM-004  
**Date**: 2026-03-01  
**Author**: Frontend Architect  
**Related Standard**: [Frontend Selection Criteria](../standards/frontend-selection-criteria.md)

---

## Context
We are building a new customer-facing B2B SaaS dashboard. The application requires strong SEO, fast initial load, and complex state management. We need to choose a meta-framework.

## Evaluation Matrix

| Criterion | Weight | **Next.js** (Raw) | **Next.js** (Wtd) | **Remix** (Raw) | **Remix** (Wtd) | **Nuxt 3** (Raw) | **Nuxt 3** (Wtd) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **SSR/SSG Flexibility** | 5 | 5 | 25 | 5 | 25 | 4 | 20 |
| **Ecosystem (Components)** | 4 | 5 | 20 | 3 | 12 | 4 | 16 |
| **Learning Curve** | 3 | 4 | 12 | 3 | 9 | 4 | 12 |
| **Performance (Core Web Vitals)** | 5 | 4 | 20 | 5 | 25 | 4 | 20 |
| **Hiring Pool** | 4 | 5 | 20 | 3 | 12 | 3 | 12 |
| **Vercel/Netlify Deploy** | 3 | 5 | 15 | 4 | 12 | 4 | 12 |
| **TOTAL SCORE** | - | - | **112** | - | **95** | - | **92** |

## Decision
**SELECTED: Next.js (App Router)**

Next.js wins on ecosystem maturity and hiring pool. The React developer market is the largest, reducing recruitment risk.

## Implementation Notes
- Use **App Router** (not Pages Router) for React Server Components.
- Deploy on **Vercel** for zero-config scaling.
- Styling: **Tailwind CSS** + **Radix UI** primitives.

---

## See Also
*   **[Frontend Selection Criteria](../standards/frontend-selection-criteria.md)**: Core Web Vitals and SSR strategies.
*   **[API Design Styleguide](../standards/api-design-styleguide.md)**: BFF pattern for frontend aggregation.
