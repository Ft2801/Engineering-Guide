# MLOps Standards (Machine Learning Operations)

## 1. Abstract
Machine Learning is Software Engineering with an extra variable: **Data**. A model that works today may fail tomorrow simply because the input distribution changed ("Drift").

> **Rule Zero**: "No Model in Production without a Training Pipeline." (Manual training notebooks are forbidden).

---

## 2. The Reproducibility Trinity

To reproduce a model artifact, you must effectively version three components simultaneously at the granularity of a specific commit hash.
1.  **Code** (Git): The architecture definition (PyTorch class).
2.  **Environment** (Docker): The libraries (CUDA version, Numpy version).
3.  **Data** (DVC/Delta Lake): The specific snapshot of the training set.

**Tooling Standard**:
*   **Tracking**: **MLflow** or Weights & Biases. Every experiment run must log `param`, `metric`, and `artifact`.

---

## 3. Training Infrastructure

GPU time is expensive.
*   **Interactive Dev**: Small instances (T4 GPUs) for debugging notebooks.
*   **Training Jobs**: Massive instances (A100s) launched via orchestration (Kubeflow/Ray).
*   **Cost Policy**: Use **Spot Instances** with checkpointing. If the node dies, resume from the last `.pt` checkpoint.

---

## 4. Serving Strategies

How does the user consume the prediction?

| Strategy | Latency | Cost | Use Case |
| :--- | :--- | :--- | :--- |
| **Real-time API** | Low (ms) | High (Always on) | Fraud Detection, Search Ranking. |
| **Batch Inference** | High (Hours) | Low (Spot) | Churn Prediction, Recommendations. |
| **Edge Inference** | Zero | Zero (User Device) | Face ID, Wake Word. (Requires Quantization `int8`). |

### 4.1 Model Formats
*   **Development**: `.pt` (PyTorch) / `.h5` (Keras).
*   **Production**: **ONNX** (Open Neural Network Exchange).
    *   *Rationale*: Optimized runtime (ONNX Runtime) that is lighter than the full PyTorch framework.

---

## 5. Monitoring (The 4th Pillar)

Observability for ML is different.
*   **Data Drift**: Input distribution relative to training set (e.g., User age shifted from 25 to 40).
*   **Concept Drift**: The relationship between X and Y changed (e.g., Inflation made $100 less valuable).
*   **Alert**: "Kolmogorov-Smirnov output test failed". Trigger **Retraining Pipeline**.

---

## See Also
*   **[GenAI Integration](./genai-integration.md)**: RAG architecture and Prompt Engineering.
*   **[Responsible AI Governance](../guides/responsible-ai-governance.md)**: Bias detection and Explainability.
*   **[Backend Selection (AI Exception)](./backend-selection-criteria.md)**: Python sidecar pattern for ML services.
*   **[RFC: Vector Search](../rfcs/2026-06-01-adopt-vector-search.md)**: Semantic search adoption proposal.

