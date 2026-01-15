# Post-Mortem Report Template

## Metadata
*   **Incident ID**: INC-XXXX
*   **Date**: YYYY-MM-DD
*   **Severity**: [P1 | P2 | P3]
*   **Duration**: HH:MM
*   **Author**: [Incident Commander]

---

## 1. Executive Summary

A 2-3 sentence summary for leadership. What happened? What was the impact? Is it fixed?

*Example*:
> On 2026-03-15, the payment processing system was unavailable for 47 minutes due to a misconfigured database connection pool. Approximately 1,200 transactions failed. The issue was resolved by reverting a recent deployment.

---

## 2. Timeline (All times in UTC)

| Time | Event |
| :--- | :--- |
| 14:00 | Deployment of `payment-service v2.3.1` begins. |
| 14:05 | Deployment completes. |
| 14:12 | Monitoring alert: Error rate > 5%. |
| 14:15 | Incident declared. On-call engineer paged. |
| 14:25 | Root cause identified: Connection pool exhaustion. |
| 14:35 | Rollback initiated. |
| 14:47 | Service restored. Incident closed. |

---

## 3. Root Cause Analysis (The 5 Whys)

1.  **Why** did transactions fail? -> Database connections timed out.
2.  **Why** did connections time out? -> Connection pool was exhausted.
3.  **Why** was the pool exhausted? -> Pool size was reduced from 100 to 10 in the new config.
4.  **Why** was the pool size reduced? -> A typo in the environment variable (`DB_POOL=10` instead of `DB_POOL=100`).
5.  **Why** wasn't this caught? -> Configuration changes are not reviewed in CI.

**True Root Cause**: Lack of automated validation for configuration changes.

---

## 4. Impact

*   **User Impact**: 1,200 failed transactions. Estimated revenue loss: $5,400.
*   **SLO Impact**: Error budget consumed: 15% of monthly budget.

---

## 5. Action Items

| Action | Owner | Due Date | Status |
| :--- | :--- | :--- | :--- |
| Add config validation to CI pipeline. | @platform-team | 2026-03-22 | [ ] |
| Create runbook for connection pool exhaustion. | @sre-team | 2026-03-25 | [ ] |
| Add dashboard for connection pool metrics. | @sre-team | 2026-03-20 | [x] |

---

## 6. Lessons Learned

*   **What went well**: Alerting fired within 7 minutes. Rollback was fast.
*   **What went poorly**: No one noticed the config change in PR review.
*   **Where we got lucky**: Incident happened during low-traffic hours.

---

## See Also
*   **[SRE Methodology](../guides/sre-methodology.md)**: Blameless Post-Mortems and Error Budgets.
*   **[Observability Strategy](../standards/observability-strategy.md)**: Golden Signals for alerting.
