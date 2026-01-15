# Decision Matrix: Language Selection for Ledger Service

**Date**: 2026-01-15  
**Related RFC**: [RFC-001: Adopt Rust](./../rfcs/2026-01-15-adopt-rust.md)

## Evaluation Matrix

| Criterion | Weight (1-5) | **Rust** (Raw) | **Rust** (Weighted) | **Go** (Raw) | **Go** (Weighted) | **Java** (Raw) | **Java** (Weighted) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Performance (Latency)** | 5 | 5 | 25 | 4 | 20 | 3 | 15 |
| **Memory Safety** | 5 | 5 | 25 | 3 | 15 | 3 | 15 |
| **Developer Experience** | 3 | 2 | 6 | 5 | 15 | 4 | 12 |
| **Ecosystem Maturity** | 4 | 4 | 16 | 5 | 20 | 5 | 20 |
| **Hiring / Talent Pool** | 3 | 2 | 6 | 5 | 15 | 5 | 15 |
| **Maintenance (TCO)** | 4 | 5 | 20 | 4 | 16 | 3 | 12 |
| **TOTAL SCORE** | - | - | **98** | - | **101** | - | **89** |

## Analysis

### The Paradox
Mathematically, **Go (101)** beats **Rust (98)** because of the heavy weights on *Hiring* and *Ecosystem*.
However, the key constraints of this specific project are "Performance" and "Memory Safety" (Weights of 5).

### Override Justification
While Go is the "Rational General Choice", for the specific domain of a **Financial Ledger**, the risk of `nil pointer` exceptions (Go) and GC pauses (Go/Java) is an disqualifying factor.

Rust scores 25/25 on the critical dimensions (Performance + Safety).
Therefore, we choose to overrule the matrix total in favor of the critical constraints.

## Conclusion
**Winner**: **Rust**  
**Runner-up**: Go

**Note**: This decision applies *only* to the Ledger Service. General-purpose APIs should continue to use Go/Java/Node based on the previous standard.
