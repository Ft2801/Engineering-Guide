# Decision Matrix: Observability Stack Selection

**Decision ID**: DM-003  
**Date**: 2026-02-15  
**Author**: SRE Team Lead  
**Related Standard**: [Observability Strategy](../standards/observability-strategy.md)

---

## Context
We need to select an observability backend to implement the Three Pillars (Metrics, Logs, Traces). The choice is between a fully managed SaaS and a self-hosted open-source stack.

## Evaluation Matrix

| Criterion | Weight | **Datadog** (Raw) | **Datadog** (Wtd) | **Grafana Stack** (Raw) | **Grafana Stack** (Wtd) | **New Relic** (Raw) | **New Relic** (Wtd) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Total Cost (3yr)** | 5 | 2 | 10 | 5 | 25 | 2 | 10 |
| **Setup Complexity** | 3 | 5 | 15 | 2 | 6 | 5 | 15 |
| **Feature Richness** | 4 | 5 | 20 | 4 | 16 | 4 | 16 |
| **Vendor Lock-in Risk** | 4 | 2 | 8 | 5 | 20 | 2 | 8 |
| **Alerting Maturity** | 4 | 5 | 20 | 4 | 16 | 4 | 16 |
| **OpenTelemetry Support** | 3 | 4 | 12 | 5 | 15 | 4 | 12 |
| **TOTAL SCORE** | - | - | **85** | - | **98** | - | **77** |

## Decision
**SELECTED: Grafana Stack (Prometheus + Loki + Tempo + Grafana)**

The open-source stack wins on cost and freedom from vendor lock-in. The operational overhead is accepted as we have internal SRE capacity.

## Implementation Notes
- **Metrics**: Prometheus (with Thanos for long-term storage).
- **Logs**: Loki (Label-based indexing).
- **Traces**: Tempo (Integrated with Grafana).
- **Dashboards**: Grafana Cloud (Free tier for dashboards, self-hosted backends).

---

## See Also
*   **[SRE Methodology](../guides/sre-methodology.md)**: Error Budgets and Burn Rate alerting.
*   **[Total Cost of Ownership](../guides/total-cost-of-ownership.md)**: 3-year TCO modeling.
