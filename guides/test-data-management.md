# Test Data Management Strategy

## 1. Abstract
The primary reason for "Flaky Tests" is inconsistent or brittle state. Managing the data lifecycle is as important as managing the test code.

---

## 2. Test Doubles Hierarchy (Gerard Meszaros)

Avoid confusion by using precise terminology.

| Type | Definition | Use Case |
| :--- | :--- | :--- |
| **Dummy** | Objects passed around but never used. | Filling mandatory parameters. |
| **Stub** | Provides canned answers to calls. | Simulating a "Success" response from an API. |
| **Spy** | Records details of how it was called. | Verifying that an email was actually sent. |
| **Mock** | Pre-programmed with expectations. | Complex behavioral verification. |
| **Fake** | Working implementation with a shortcut. | **In-memory Database** (H2, SQLite). |

---

## 3. Database Strategy: Testcontainers

Do not shared a "Test Database" between developers. It leads to race conditions and dirty state.

**Standard**: Use **Testcontainers**.
*   The test suite launches a temporary Docker container (e.g., Postgres) for every test run (or suite).
*   **Isolation**: Every test gets a fresh, clean schema.
*   **Fidelity**: You test against the *actual* database engine used in production, not a different in-memory engine.

---

## 4. Production Data Management (Privacy)

**NEVER** use raw production data in non-production environments.

### 4.1 Data Masking (Obfuscation)
If you must use production snapshots for staging performance tests:
*   **Anonymization**: Replace `name` with "John Doe", `email` with `userN@example.com`.
*   **Irreversibility**: Ensure the original identity cannot be reconstructed (Hashing is not enough, use Synthesis).

### 4.2 Synthetic Data Generation
**Preferred Strategy**: Use tools (Faker, FactoryBot) to generate realistic but purely fake datasets.
*   *Advantage*: Zero risk of PII (Personally Identifiable Information) leakage. Infinite supply of data.

---

## 5. Golden Master / Snapshot Testing

For legacy systems or complex UI:
1. Run the system, record the output (The "Golden Master").
2. Subsequent runs compare the current output against the master.
3. If they differ, the test fails.

**Warning**: Use snapshots sparingly for UI. They are prone to "False Positives" (e.g., a 1px shift causing a full failure).
