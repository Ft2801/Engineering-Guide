# Architectural Decision Record (ADR) Template

## Metadata
*   **ADR ID**: ADR-XXX
*   **Date**: YYYY-MM-DD
*   **Status**: [Proposed | Accepted | Deprecated | Superseded by ADR-YYY]
*   **Deciders**: [List of architects/leads involved]

---

## 1. Title

A short, descriptive title (e.g., "Use PostgreSQL for Primary Data Store").

---

## 2. Context

Describe the technical, business, or political forces at play. What is the problem we are trying to solve? What constraints do we have?

*Example*:
> We need to select a database for our new e-commerce platform. The system must support 10,000 transactions per second, maintain ACID compliance for financial operations, and be operationally simple for our small SRE team.

---

## 3. Decision

State the architectural decision that was made. Be explicit and concise.

*Example*:
> We will use Amazon Aurora PostgreSQL as our primary OLTP database.

---

## 4. Rationale

Explain why this decision was made. List the options that were considered and why they were rejected.

| Option | Pros | Cons | Verdict |
| :--- | :--- | :--- | :--- |
| **Aurora PostgreSQL** | Managed, Postgres-compatible, Read Replicas | Vendor Lock-in (AWS) | **Chosen** |
| **CockroachDB** | Horizontal scaling, Global | Operational complexity | Rejected |
| **Self-Hosted Postgres** | Full control | High operational burden | Rejected |

---

## 5. Consequences

Describe the resulting context after applying the decision. Include both positive and negative consequences.

**Positive**:
*   Reduced operational burden (AWS manages patching, backups).
*   Fast read scaling via Aurora Read Replicas.

**Negative**:
*   Vendor lock-in to AWS.
*   No built-in horizontal write scaling (future risk).

---

## 6. Related Documents

*   [Link to RFC or Decision Matrix]
*   [Link to related ADR]

---

## See Also
*   **[Documentation as Code](../standards/documentation-as-code.md)**: ADR best practices.
*   **[Legacy Modernization](../guides/legacy-modernization-strategy.md)**: Using ADRs to document "Why" decisions.
