# Service Specification (Backstage `catalog-info.yaml`) Template

This template defines the metadata for registering a service in the Internal Developer Portal (Backstage).

---

## `catalog-info.yaml`

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: <service-name>
  description: <One-line description of the service>
  annotations:
    # Link to the Grafana dashboard for this service
    grafana/dashboard-selector: "service=<service-name>"
    # Link to the PagerDuty service
    pagerduty.com/service-id: <pagerduty-service-id>
    # Link to the GitHub repo
    github.com/project-slug: <org>/<repo>
  tags:
    - python
    - backend
    - payments
  links:
    - url: https://docs.internal.co/<service-name>
      title: Documentation
      icon: docs
    - url: https://grafana.internal.co/d/<dashboard-id>
      title: Grafana Dashboard
      icon: dashboard
spec:
  type: service
  lifecycle: production # or 'experimental', 'deprecated'
  owner: <team-name> # Must match a Group in Backstage
  system: <system-name> # Logical grouping (e.g., 'payments-platform')
  dependsOn:
    - component:<dependency-service-name>
  providesApis:
    - <api-name>
```

---

## Field Definitions

| Field | Description | Required |
| :--- | :--- | :---: |
| `metadata.name` | Unique identifier for the service (kebab-case). | ✅ |
| `metadata.description` | Human-readable summary. | ✅ |
| `metadata.tags` | Keywords for filtering (e.g., `python`, `backend`). | ⚪ |
| `spec.type` | `service`, `website`, `library`. | ✅ |
| `spec.lifecycle` | `experimental`, `production`, `deprecated`. | ✅ |
| `spec.owner` | The team responsible (must exist as a Backstage Group). | ✅ |
| `spec.system` | Logical grouping of services. | ⚪ |
| `spec.dependsOn` | List of other components this service depends on. | ⚪ |
| `spec.providesApis` | List of APIs (OpenAPI specs) this service exposes. | ⚪ |

---

## Best Practices

1.  **Keep `metadata.description` under 100 characters.**
2.  **Use `spec.dependsOn` to auto-generate architecture diagrams.**
3.  **Link `pagerduty.com/service-id` to enable "Who is on-call?" lookups.**

---

## See Also
*   **[RFC: Internal Dev Portal](../rfcs/2026-07-01-adopt-internal-dev-portal.md)**: Backstage adoption proposal.
*   **[Documentation as Code](../standards/documentation-as-code.md)**: ADR and TechDocs standards.
