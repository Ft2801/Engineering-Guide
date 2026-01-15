# Responsible AI Governance

## 1. Abstract
AI models affect human lives (Loans, Hiring, Content Moderation). "It was the algorithm" is not a legal defense. We enforce Ethical AI principles.

---

## 2. Fairness and Bias
Bias enters via the training data.
*   **Representation Bias**: Dataset has 90% men, 10% women. Model fails on women.
*   **Historical Bias**: Training on historic hiring data replicates historic racism.

**Mitigation**:
*   **Dataset Audits**: Balance checks before training.
*   **Slicing Metrics**: Measurement of accuracy *per subgroup* (Accuracy for Men vs Accuracy for Women), not just global accuracy.

---

## 3. Explainability (XAI)

Black-box models are dangerous. We use "Post-hoc Interpretability".
*   **SHAP (SHapley Additive exPlanations)**: Game theory approach.
    *   *Result*: "Loan Denied because: Income (-50), Debt (+20), Age (+10)".
*   **LIME**: Local approximation.

**Rule**: Any High-Impact decision model MUST provide SHAP values for every inference.

---

## 4. Human-in-the-Loop (HITL)

Automation is not binary.
1.  **Full Auto**: Low Risk (Recommendation System).
2.  **Human Audit**: Model acts, human reviews 10% sample daily.
3.  **Human Decision**: Model provides score, Human clicks the button (Hiring/Firing).

---

## 5. Model Cards
Every model released to production must have a `MODEL_CARD.md`.
*   **Intended Use**: What is this for?
*   **Limitations**: Where does it fail? ("Do not use on children under 13").
*   **Training Data**: Source and cut-off date.
