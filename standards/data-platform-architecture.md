# Data Platform Architecture (Modern Data Stack)

## 1. Abstract
Data is an asset only if it is accessible, trusted, and fresh. The era of the "Monolithic Data Warehouse" managed by IT is over. We adopt the **Data Mesh** principle: Data as a Product, owned by domain teams.

---

## 2. Ingestion Strategy: ETL vs ELT

Transformation is the bottleneck. We move it to the end.

| Strategy | Flow | Compute Location | Use Case |
| :--- | :--- | :--- | :--- |
| **ETL** (Legacy) | Extract -> Transform -> Load | Specialized Server (Informatica) | Strict regulatory compliance (PII masking *before* loading). Slow. |
| **ELT** (Modern) | Extract -> Load -> Transform | The Warehouse (Snowflake/BigQuery) | **Standard**. Dump raw data fast. Transform using SQL (dbt). |

**Standard**: Use **ELT**. Pay for storage (cheap) to save engineering time (expensive).

---

## 3. Storage Architecture: The Lakehouse

We do not separate "Data Lake" (Files) and "Data Warehouse" (SQL). We merge them.

### 3.1 The Format
*   **Open Table Formats**: We standardize on **Apache Iceberg** or **Delta Lake**.
*   *Benefit*: ACID transactions on S3/GCS files. Time Travel (Rollback). No vendor lock-in to Snowflake.

### 3.2 Tiered Storage
1.  **Bronze (Raw)**:  JSON dumps from APIs. Immutable. Retention: 7 years.
2.  **Silver (Clean)**: Deduplicated, typed, PII-masked.
3.  **Gold (Aggregated)**: Business-ready metrics ("Daily Active Users"). Served to BI tools.

---

## 4. Transformation Logic (dbt)

**dbt (data build tool)** is mandatory.
*   **Code**: All business logic implies SQL `SELECT` statements in git.
*   **Testing**: `dbt test` runs assertions (`unique`, `not_null`) on every pipeline run.
*   **Docs**: `dbt docs` generates lineage graphs automatically.

---

## 5. Orchestration (Workflow Management)

Do not use Cron for data pipelines. Use a DAG (Directed Acyclic Graph) engine.

*   **Standard**: **Apache Airflow** (or Prefect/Dagster).
*   **Requirement**: All tasks must be *Idempotent*. A retry of a failed task must not duplicate data.

---

## 6. The Data Mesh Governance

Data is not "owned" by the Data Team. It is owned by the Service Team.

*   **Producer Responsibility**: The "Checkout Service" team is responsible for publishing high-quality "Checkout Events" to the Bronze layer.
*   **Consumer Responsibility**: The "Marketing Team" consumes these events to build dashboards.
*   **Data Contract**: A schema registry (Protobuf/Avro) enforces compatibility preventing producers from breaking consumers.
