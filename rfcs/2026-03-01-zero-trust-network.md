# RFC-008: Deprecation of Corporate VPN (Project Zero Trust)

**Status**: Draft  
**Author**: Chief Information Security Officer (CISO)  
**Date**: 2026-03-01  
**Stakeholders**: IT Security, DevOps, All Employees

---

## 1. Executive Summary
We propose decommissioning the legacy OpenVPN appliances. Access to internal tools (Jenkins, Grafana, Admin Panels) will be migrated to an **Identity-Aware Proxy (IAP)** model. This aligns with the "Zero Trust" maxim: *Never Trust, Always Verify*.

## 2. Problem Statement

### 2.1 The "Hard Shell, Soft Center" Fallacy
Our current security relies on the perimeter. Once a user connects to VPN, they have unchecked network visibility of the entire Production VPC (10.0.0.0/8). A single compromised laptop endangers the entire company (Lateral Movement).

### 2.2 Operational Friction
*   **Latency**: Tromboning traffic through the VPN concentrator adds ~150ms.
*   **Support**: 15% of IT tickets are "VPN Connectivity" issues.

## 3. Proposed Solution
Migrate to **Cloudflare Access** (or Google IAP / AWS Verified Access).

### 3.1 Architecture change
*   **Before**: User -> VPN -> Firewall -> Internal App.
*   **After**: User -> Internet -> Edge Proxy (Auth Check) -> Internal App.

### 3.2 Policy Logic
*   **Identity**: Must be logged in via Okta (SSO).
*   **Context**: Request must come from a Corporate Managed Device (verified via mTLS certificate on the laptop).
*   **Geography**: Block logins from high-risk countries.

## 4. Migration Plan

| Phase | Target Users | Scope |
| :--- | :--- | :--- |
| **Phase 1** | DevOps Team | Grafana, Prometheus, ArgoCD. |
| **Phase 2** | Customer Support | Internal Admin Panels, Retool. |
| **Phase 3** | Engineering | Jenkins, Jira, Confluence. |
| **Phase 4** | **Power Off** | Shutdown OpenVPN Servers. |

## 5. Risk Assessment

*   **Risk**: If the Identity Provider (Okta) goes down, no one can work.
    *   *Mitigation*: Operational "Break Glass" local admin accounts stored in a physical safe.
*   **Risk**: Legacy apps that don't support HTTP (e.g., SSH to DB).
    *   *Mitigation*: Use short-lived ssh certificates via `cloudflared` tunnel.

## 6. Decision
**APPROVED**. The security benefits of eliminating lateral movement justify the architectural overhaul.
