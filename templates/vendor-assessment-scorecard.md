# Vendor Risk Assessment (VRA) Scorecard Template

## Metadata
*   **Vendor Name**: [Vendor Name]
*   **Assessment Date**: YYYY-MM-DD
*   **Assessor**: [Your Name / Team]
*   **Data Classification**: [Public | Internal | Confidential | PII]

---

## 1. Vendor Overview

| Field | Value |
| :--- | :--- |
| **Product/Service** | [e.g., "Managed PostgreSQL Hosting"] |
| **Website** | [URL] |
| **Primary Contact** | [Name, Email] |
| **Contract Value (Annual)** | [$XXX,XXX] |

---

## 2. Evaluation Matrix

### 2.1 Security & Compliance (Weight: 40%)

| Criterion | Score (1-5) | Notes |
| :--- | :---: | :--- |
| SOC 2 Type II Certification | | |
| ISO 27001 Certification | | |
| Penetration Test Report (last 12 months) | | |
| Data Encryption (At Rest / In Transit) | | |
| Customer Managed Keys (BYOK) Support | | |
| **Subtotal** | **/25** | |

### 2.2 Financial & Operational Viability (Weight: 30%)

| Criterion | Score (1-5) | Notes |
| :--- | :---: | :--- |
| Years in Business | | |
| Funding Stage / Profitability | | |
| SLA (Uptime Guarantee) | | |
| Support Responsiveness (SLA for P1) | | |
| **Subtotal** | **/20** | |

### 2.3 Exit Strategy & Portability (Weight: 30%)

| Criterion | Score (1-5) | Notes |
| :--- | :---: | :--- |
| Data Export Capability (API / Dump) | | |
| Data Format (Open Standard vs Proprietary) | | |
| Contract Termination Clause | | |
| Estimated Migration Effort | | |
| **Subtotal** | **/20** | |

---

## 3. Final Score Calculation

| Category | Weight | Subtotal | Weighted Score |
| :--- | :---: | :---: | :---: |
| Security & Compliance | 40% | /25 | |
| Financial & Operational | 30% | /20 | |
| Exit Strategy | 30% | /20 | |
| **TOTAL** | **100%** | | **/100** |

---

## 4. Decision

| Score Range | Recommendation |
| :--- | :--- |
| **80-100** | ✅ Approved |
| **60-79** | ⚠️ Conditional Approval (Mitigations Required) |
| **0-59** | ❌ Rejected |

**Final Decision**: [Approved / Conditional / Rejected]

**Mitigations (if Conditional)**:
1.  [e.g., "Require vendor to complete SOC 2 audit within 6 months."]

---

## See Also
*   **[Vendor Risk Assessment Guide](../guides/vendor-risk-assessment.md)**: Full methodology.
*   **[Compliance & Data Privacy](../standards/compliance-and-data-privacy.md)**: GDPR and SOC2 requirements.
