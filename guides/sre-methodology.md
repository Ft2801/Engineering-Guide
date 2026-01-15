# Site Reliability Engineering (SRE) Methodology

## 1. Abstract
SRE applies software engineering principles to infrastructure and operations. The core belief is that **100% reliability is the wrong target**. It is infinitely expensive and prevents innovation. We aim for "Reliability High Enough to keep users happy."

---

## 2. The Language of Reliability

### 2.1 SLI (Service Level Indicator)
A quantitative measure of some aspect of the level of service that is provided.
*   *Example*: "The HTTP status code of the response."
*   *Formula*:
    $$ SLI = \frac{\text{Good Events}}{\text{Valid Events}} \times 100 $$

### 2.2 SLO (Service Level Objective)
A target value or range of values for a service level that is measured by an SLI.
*   *Example*: "99.9% of requests in 30 days must be 200 OK."
*   *Philosophy*: This is the internal contract. If we violate it, we freeze deploys.

### 2.3 SLA (Service Level Agreement)
The explicit or implicit contract with your users that includes consequences (financial penalty).
*   *Target*: Generally lower than the SLO (e.g., 99.5%).

---

## 3. The Error Budget

The Error Budget is the amount of unreliability you are willing to tolerate.

$$ \text{Budget} = 100\% - \text{SLO} $$

**Example**:
*   Requests/Month: 10,000,000
*   SLO: 99.9%
*   Allowed Errors: $10,000,000 \times 0.001 = 10,000$.

**Governance**:
*   If Budget > 0: **Execute**. Push features, run risky experiments.
*   If Budget < 0: **Freeze**. Operations takes the pager. Dev team focuses solely on stability/reliability fixes.

---

## 4. Alerting Theory: Burn Rates

Alerting on raw error rate is noisy. We alert on the rate at which we are consuming the Error Budget.

| Burn Rate | Time to Exhaust Budget | Alert Priority |
| :--- | :--- | :--- |
| **14.4x** | 2 Days | **Page (P1)** - Something is critically broken immediately. |
| **6x** | 5 Days | **Ticket (P2)** - We will run out before the weekend if not fixed. |
| **1x** | 30 Days | **Dashboard** - Normal background noise. |

---

## 5. Incident Management
When the pager rings, we enter "Wartime Mode".

1.  **Commander**: The single source of truth. Does not touch keyboard. Coordinates.
2.  **Scribe**: Writes down timeline.
3.  **Ops**: Touches the keyboard.

**The Post-Mortem**:
After the incident, we write a **Blameless Post-Mortem**.
*   *Root Cause*: NOT "Fabio deployed a bug".
*   *Root Cause*: "The CI pipeline lacked a canary stage to detect the bug before 100% rollout."

---

## See Also
*   **[Observability Strategy](../standards/observability-strategy.md)**: The Three Pillars (Metrics, Logs, Traces) and Golden Signals.
*   **[Testing & QA Standards](../standards/testing-and-quality-assurance.md)**: Building quality gates before production.
*   **[Distributed Systems Patterns](./distributed-systems-patterns.md)**: Circuit Breakers and resiliency.

