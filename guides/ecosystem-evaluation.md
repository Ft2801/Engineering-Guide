# Ecosystem Evaluation Methodology

## 1. Introduction

The **Ecosystem** of a technology is the totality of the community, tooling, documentation, and economic incentives that surround it. Empirical research suggests that ecosystem health is a stronger predictor of project success than raw technical superiority.

> "Software ecosystems are socio-technical networks. A failure in the social layer inevitably propagates to the technical layer." — *Jansen et al., 2009*

---

## 2. Quantitative Analysis Framework

We employ a multi-variate analysis to quantify ecosystem vitality.

### 2.1 The Velocity Coefficient ($V_c$)
Velocity measures the rate of productive change. We distinguish between *churn* and *progress*.

$$
V_c = \frac{\sum_{i=1}^{n} (C_i \times W_i)}{T}
$$

Where:
*   $C_i$: Commit code $i$.
*   $W_i$: Impact weight (Feature = 1.0, Bugfix = 0.5, Refactor = 0.2).
*   $T$: Time period (usually rolling 12 months).

**Interpretation**:
*   $V_c \rightarrow 0$: Stagnation. Risk of unpatched security vulnerabilities (`Left-pad` incident).
*   $V_c \rightarrow \infty$: Instability. High risk of breaking changes (e.g., early-stage Javascript frameworks).

### 2.2 The Bus Factor and Centralization Risk
The "Bus Factor" ($B_f$) is the minimum number of developers that must be incapacitated for the project to halt.

**Risk Tiers**:
| Tier | $B_f$ | Risk Description | Governance Model |
| :--- | :---: | :--- | :--- |
| **Critical** | 1 | Single point of failure. | Benevolent Dictator (Personal) |
| **High** | 2-4 | Vulnerable to acqui-hiring or startup failure. | Small Team |
| **Moderate** | 5-20 | Resilient to normal turnover. | Foundation (Apache, CNCF) |
| **Low** | >20 | Institutional persistence. | Global Consensus (Linux, Kubernetes) |

### 2.3 Triage Latency ($L_t$)
 Responsiveness is a proxy for maintainer bandwidth.

$$
L_t = P90(t_{response} - t_{open})
$$

*   **Requirement**: For production-critical infrastructure, $L_t$ must be $< 48$ hours.

---

## 3. Qualitative Assessment Vectors

### 3.1 Documentation Quality Framework
Documentation is evaluated on four dimensions (The Diátaxis Framework):
1.  **Tutorials**: Learning-oriented (Lesson).
2.  **How-to Guides**: Problem-oriented (Steps).
3.  **Reference**: Information-oriented (Description).
4.  **Explanation**: Understanding-oriented (Discussion).

*Failure Mode*: An ecosystem with only "Reference" docs (e.g., auto-generated API docs) has a steep learning curve and high TCO.

### 3.2 The "Standard Library" Effect
*   **Strong Standard Library** (Go, Python): Reduces dependency on 3rd party packages. Increases security and stability.
*   **Weak Standard Library** (Javascript): Forces reliance on fragmented micro-packages. Increases "Supply Chain Attack" surface area.

---

## 4. Case Studies

### 4.1 Case Study: The AngularJS to Angular 2 Migration (2016)
*   **Event**: A complete rewrite of the framework that broke backward compatibility.
*   **Impact**: Massive fragmentation of the ecosystem. Many teams migrated to React.
*   **Lesson**: Avoid ecosystems where the core team exhibits a willingness to violate Semantic Versioning for architectural purity.

### 4.2 Case Study: The OpenTofu Fork (2023)
*   **Event**: Terraform changed license from MPL to BSL.
*   **Impact**: Community forked the project to OpenTofu under Linux Foundation.
*   **Lesson**: Single-vendor open source (HashiCorp) carries a "License Change Risk". Multi-vendor governance (CNCF) is safer for long-term bets.

---

## 5. Evaluation Checklist

| Dimension | Metric | Best Practice Threshold |
| :--- | :--- | :--- |
| **License** | Open Source Definition | MIT, Apache 2.0, BSD-3, MPL |
| **Governance** | Foundation Backing | CNCF, Apache, Linux Foundation |
| **Package Count** | Registry Growth | Positive YoY growth |
| **StackOverflow** | Answer Rate | > 70% of questions answered |
