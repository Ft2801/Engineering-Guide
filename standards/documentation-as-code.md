# Documentation as Code Standards

## 1. Introduction
Documentation is a first-class citizen of the software engineering process. It must be versioned, reviewed, and deployed alongside the code. 

> **Principle**: "If it isn't documented, it doesn't exist. If it's documented in a private DM or a fleeting Slack message, it still doesn't exist."

---

## 2. The Diátaxis Framework

We categorize all documentation into four distinct types based on the user's intent.

| Type | Goal | Style | Intent |
| :--- | :--- | :--- | :--- |
| **Tutorials** | Learning by doing. | Lessons | "Let's build a Hello World." |
| **How-To Guides** | Solving a specific problem. | Steps | "How do I deploy to EKS?" |
| **Reference** | Technical description. | Specification | "API endpoint parameters." |
| **Explanation** | Understanding concepts. | Discussion | "Why we chose Kafka." |

**Standard**: Every repository MUST contain a balance of these four types. Use the `docs/` directory.

---

## 3. Architectural Decision Records (ADR)

An ADR captures the "Why" behind a significant architectural choice. This prevents "Chesterton's Fence" (deleting something because you don't know why it's there).

### 3.1 ADR Structure (Michael Nygard Template)
1.  **Title**: Short and descriptive.
2.  **Status**: Proposed, Accepted, Deprecated, Superseded.
3.  **Context**: The problem and constraints at the time.
4.  **Decision**: What we chose to do.
5.  **Consequences**: The trade-offs (positive and negative).

**Standard**: Store ADRs in the root `/docs/adr/` folder using N-prefixed naming (e.g., `adr-001-use-rust.md`).

---

## 4. Documentation Lifecycle

### 4.1 Peer Review
Documentation changes must go through the same PR (Pull Request) process as code. Correctness is verified by peers.

### 4.2 Automated Verification
*   **Link Checking**: Automated tools (`lychee`, `markdown-link-check`) must run in CI to prevent 404s.
*   **Diagrams**: Use **Mermaid.js** within markdown. Never commit binary `.png` or `.svg` files that cannot be edited via text.

---

## 5. Knowledge Discovery: Internal Dev Portals

As organizations scale beyond 50 services, discovery becomes the bottleneck.

*   **Standard**: Use **Backstage (Spotify)** or a similar catalog.
*   **Mandate**: Every service must have a `catalog-info.yaml` file defining the owner, the documentation link, and the public API spec.

---

## See Also
*   **[ADR Template](../templates/adr-template.md)**: Ready-to-use ADR format.
*   **[Service Catalog Template](../templates/service-catalog-template.md)**: Backstage `catalog-info.yaml`.
*   **[RFC: Internal Dev Portal](../rfcs/2026-07-01-adopt-internal-dev-portal.md)**: Backstage adoption proposal.
*   **[Post-Mortem Template](../templates/post-mortem-template.md)**: Incident documentation standard.
*   **[Legacy Modernization](../guides/legacy-modernization-strategy.md)**: Using ADRs to preserve context.

