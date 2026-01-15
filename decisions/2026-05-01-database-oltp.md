# Decision Matrix: Database Selection (Primary OLTP)

**Decision ID**: DM-006  
**Date**: 2026-05-01  
**Author**: Data Architect  
**Related Standard**: [Database Selection Criteria](../standards/database-selection-criteria.md)

---

## Context
We are selecting the primary database for a new high-transaction e-commerce platform. Requirements: Strong ACID compliance, horizontal read scaling, and managed operations.

## Evaluation Matrix

| Criterion | Weight | **Aurora PostgreSQL** (Raw) | **Aurora** (Wtd) | **CockroachDB** (Raw) | **CockroachDB** (Wtd) | **PlanetScale** (Raw) | **PlanetScale** (Wtd) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ACID Compliance** | 5 | 5 | 25 | 5 | 25 | 4 | 20 |
| **Horizontal Scaling** | 4 | 3 | 12 | 5 | 20 | 5 | 20 |
| **Operational Simplicity** | 4 | 5 | 20 | 3 | 12 | 5 | 20 |
| **Cost (at 10TB)** | 4 | 3 | 12 | 3 | 12 | 4 | 16 |
| **Postgres Compatibility** | 5 | 5 | 25 | 5 | 25 | 2 | 10 |
| **Global Distribution** | 3 | 2 | 6 | 5 | 15 | 4 | 12 |
| **TOTAL SCORE** | - | - | **100** | - | **109** | - | **98** |

## Decision
**OVERRIDE: Aurora PostgreSQL** (Despite CockroachDB higher score)

CockroachDB scored highest due to horizontal scaling and global distribution. However, we are NOT selecting it because:
1.  **Team Expertise**: Zero engineers have CockroachDB experience.
2.  **Single Region Requirement**: Our e-commerce platform targets a single geography (EU).

Aurora PostgreSQL is selected for its operational simplicity and full Postgres wire-protocol compatibility.

## Trade-offs Accepted
- We accept the risk of vertical scaling limits (Aurora supports up to 128 vCPUs).
- Future global expansion will require a re-evaluation.

---

## See Also
*   **[Database Selection Criteria](../standards/database-selection-criteria.md)**: CAP Theorem and Storage Engines.
*   **[Data Platform Architecture](../standards/data-platform-architecture.md)**: Analytical layer (Lakehouse).
