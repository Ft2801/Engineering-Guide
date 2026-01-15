# RFC-030: Adopting Grafana Stack for Unified Observability

**Status**: Approved  
**Author**: SRE Team Lead  
**Date**: 2026-02-20  
**Stakeholders**: SRE, Platform, All Engineering  
**Related Decision**: [Decision Matrix: Observability Stack](../decisions/2026-02-15-observability-stack.md)

---

## 1. Executive Summary
We propose implementing a unified observability stack based on **Grafana Labs** open-source projects (Prometheus, Loki, Tempo, Grafana). This replaces the fragmented mix of Datadog (partial), CloudWatch, and ELK.

## 2. Problem Statement
*   **Cost**: Datadog ingestion costs are growing 40% YoY. Projected $180k/year by 2027.
*   **Fragmentation**: Logs in CloudWatch, Metrics in Datadog, Traces nowhere.
*   **Correlation**: Cannot correlate a trace to its logs without manual timestamp matching.

## 3. Proposed Solution
Deploy the **Grafana LGTM Stack** (Loki, Grafana, Tempo, Mimir/Prometheus).

### 3.1 Architecture
```
┌─────────────────┐     ┌─────────────────┐      ┌─────────────────┐
│   Application   │────▶│  OTel Collector │────▶│     Grafana     │
│  (Instrumented) │     │    (Sidecar)    │      │   (Dashboard)   │
└─────────────────┘     └────────┬────────┘      └─────────────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
              ┌──────────┐ ┌──────────┐ ┌──────────┐
              │Prometheus│ │   Loki   │ │  Tempo   │
              │ (Metrics)│ │  (Logs)  │ │ (Traces) │
              └──────────┘ └──────────┘ └──────────┘
```

### 3.2 Cost Projection (3-Year)

| Solution | Year 1 | Year 2 | Year 3 | Total |
| :--- | :--- | :--- | :--- | :--- |
| **Datadog** | $120k | $168k | $235k | $523k |
| **Grafana Stack** | $45k | $50k | $55k | $150k |
| **Savings** | | | | **$373k** |

## 4. Implementation Plan
1.  **Month 1**: Deploy Prometheus + Grafana for metrics.
2.  **Month 2**: Deploy Loki for logs, migrate from CloudWatch.
3.  **Month 3**: Deploy Tempo for traces, remove remaining Datadog agents.

## 5. Decision
**APPROVED**. Project funded in Q1 2026.

---

## See Also
*   **[Decision Matrix: Observability Stack](../decisions/2026-02-15-observability-stack.md)**: Quantitative evaluation.
*   **[Observability Strategy](../standards/observability-strategy.md)**: Three Pillars and Golden Signals.
*   **[SRE Methodology](../guides/sre-methodology.md)**: Error Budgets and Burn Rate alerting.
