# Observability Strategy Standards

## 1. Introduction
Observability is the property of a system that allows you to understand its internal state based purely on its external outputs. It is distinct from "Monitoring" (checking if the green light is on).

> "Monitoring tells you the system is broken. Observability tells you **why**."

## 2. The Three Pillars

### 2.1 Metrics (The "What")
Aggregated numerical data. Cheap to store, fast to query.
*   **Protocol**: Prometheus / OpenMetrics.
*   **Retention**: 13 months (for YoY trends).
*   **Cardinality Warning**: Do not include `user_id` or `uuid` in labels. This explodes the time-series index cost.

### 2.2 Logs (The "Why")
Discreet events. Expensive to index.
*   **Format**: JSON Structured Logging is **Mandatory**.
    *   *Bad*: `print("Error user failed")`
    *   *Good*: `logger.error({ event: "login_failed", user_id: 123, reason: "bad_password" })`
*   **Standard**: Use **Loki** (Label-based indexing) to reduce cost vs ElasticSearch (Full-text indexing).

### 2.3 Traces (The "Where")
The lifecycle of a request across microservices.
*   **Protocol**: **OpenTelemetry (OTEL)** is the industry standard.
*   **Sampling Strategy**:
    *   *Head Sampling*: Decide at generic (random 1%) - Keep costs low.
    *   *Tail Sampling*: Keep only traces with Errors or Latency > 2s - Maximize value.

---

## 3. Semantic Conventions

To enable cross-service correlation, all services must inject standardized metadata.

| Field | Example | Description |
| :--- | :--- | :--- |
| `service.name` | `payment-api` | Unique identifier of the app. |
| `deployment.environment` | `production` | Logical scope. |
| `trace_id` | `0af765...` | W3C Standard Trace ID. |
| `span_id` | `b7ad...` | Specific unit of work. |

---

## 4. Alerting Design (SRE Paging)

Do not page humans for "High CPU". Page humans for "User Pain".

### 4.1 The Golden Signals (Google SRE)
1.  **Latency**: Time taken to service a request.
2.  **Traffic**: Demand on the system (req/sec).
3.  **Errors**: Rate of requests that fail.
4.  **Saturation**: How "full" is the system (Queue depth).

### 4.2 Alert Hierarchy
*   **P1 (Wake up)**: SLO Violation imminent. (e.g., Error Rate > 1% for 5 mins).
*   **P2 (Next Business Day)**: Metric anomaly. (e.g., Disk 80% full).
*   **P3 (Info)**: Deployment success.

## 5. Implementation Stack
*   **Collector**: OpenTelemetry Collector (Sidecar).
*   **Backend**: Prometheus (Metrics) + Tempo (Traces) + Loki (Logs).
*   **Frontend**: Grafana.

---

## See Also
*   **[SRE Methodology](../guides/sre-methodology.md)**: Error Budgets and Burn Rate alerting.
*   **[Infrastructure as Code](./infrastructure-as-code.md)**: Deploying the observability stack via Terraform.
*   **[RFC: Kubernetes Migration](../rfcs/2026-02-01-migration-to-kubernetes.md)**: Observability requirements for Day 2 Operations.

