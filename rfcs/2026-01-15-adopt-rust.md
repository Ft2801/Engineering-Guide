# RFC-001: Adopt Rust for Core Transaction Service

**Status**: Approved  
**Author**: Principal Architect  
**Date**: 2026-01-15  
**Stakeholders**: CTO, VP Engineering, Platform Team

---

## 1. Executive Summary
We propose adopting **Rust** as the primary language for the new "Ledger" microservice. This service requires deterministic latency (<5ms P99) and strict memory safety to prevent financial calculation errors. The current Node.js stack incurs GC pauses exceeding our SLOs.

## 2. Problem Statement
The current transaction ledger is built on Node.js.
*   **Latency Violation**: Garbage Collection (GC) pauses cause P99 latency spikes up to 45ms during high load.
*   **Concurrency**: Node's single-threaded Event Loop becomes a bottleneck during complex JSON serialization of large batch payloads.
*   **Business Risk**: Non-deterministic latency causes timeouts in upstream banking partners, leading to failed transactions (~0.5% failure rate).

## 3. Proposed Solution
Build the new `ledger-core` service in **Rust**.
*   **Architecture**: Axum (Web Framework) + Tokio (Runtime) + SQLx (Postgres Driver).
*   **Deployment**: Distroless Docker images (~25MB) running on Kubernetes `c6g.xlarge` instances.

## 4. Alternative Solutions Analysis

| Solution | Key Advantages | Key Disadvantages | Rejection Rationale |
| :--- | :--- | :--- | :--- |
| **Go** | Fast compilation, massive talent pool, simple concurrency. | Stop-the-World GC still exists (though fast). Weak type system (nil panics). | GC pauses (~10ms) are borderline for our <5ms SLO. |
| **C++** | Zero overhead, mature. | Memory unsafe (Segfaults/Buffer Overflows). Extremely high TCO (Debugging time). | Risk of memory corruption in a financial system is unacceptable. |
| **Java** | Standard enterprise choice, huge ecosystem. | Heavy footprint (JVM warm-up), unpredictable JIT optimization. | High resource consumption (RAM) and start-up time. |

## 5. Strategic Evaluation (The 6 Pillars)

### 5.1 Ecosystem and Maturity
Rust has reached stable maturity (Edition 2021). It is now part of the Linux Kernel. AWS and Cloudflare use it for critical infra.

### 5.2 Developer Experience and Tooling
High learning curve (Borrow Checker). However, the compiler provides best-in-class error messages. Cargo is superior to NPM/Maven for dependency management.

### 5.3 Performance and Constraints
*   **Benchmark**: Protobuf serialization is 10x faster than Node.js.
*   **Memory**: Consumes ~20MB RAM vs ~400MB for Java equivalent.

### 5.4 Human Capital
Hiring senior Rust engineers is difficult/expensive. However, internal interest is high. We will execute a "Training Up" strategy for existing Senior Go/Java devs.

### 5.5 Long-term Viability
Backed by the Rust Foundation (AWS, Google, Microsoft). Extremely high viability.

### 5.6 Cost Assessment
*   **Infra Savings**: Estimated 60% reduction in EC2 bill due to lower resource usage.
*   **Training Cost**: 4 weeks of productivity loss during ramp-up.

## 6. Risk Assessment and Mitigation Strategies
*   **Risk**: "Fighting the Borrower Checker" slows down feature dev.
    *   *Mitigation*: Pair programming with an external Rust consultant for the first 2 sprints.
*   **Risk**: Fragmentation of Async ecosystem.
    *   *Mitigation*: Standardize strictly on `Tokio` stack.

## 7. Implementation Roadmap
1.  **Month 1**: PoC of the "Transaction Parsing" module.
2.  **Month 2**: Benchmark PoC against Node.js baseline.
3.  **Month 3**: Hiring/Training workshop.
4.  **Month 4**: Production Pilot (1% Traffic).

## 8. Conclusion and Decision
**APPROVED**. The performance requirements outweigh the hiring friction. The team accepts the TCO of training in exchange for correctness and speed.
