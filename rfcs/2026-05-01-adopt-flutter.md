# RFC-012: Unification of Mobile Stacks (Adopt Flutter)

**Status**: Draft  
**Author**: Head of Mobile  
**Date**: 2026-05-01  
**Stakeholders**: iOS Team, Android Team, Product

---

## 1. Executive Summary
We propose unifying the separate iOS (Swift) and Android (Kotlin) teams into a single **Mobile Product Team** using **Flutter**. This will double our feature velocity and ensure UI consistency.

## 2. Problem Statement
*   **Feature Parity**: The Android app is currently 2 sprints behind iOS due to hiring difficulties.
*   **Duplicate Logic**: We implement the same business logic (e.g., Cart Validation) twice, leading to subtle bugs.
*   **Cost**: Maintaining two codebases requires 12 Engineers (6 iOS + 6 Android).

## 3. Proposed Solution
Adopt **Flutter** (Dart) for all new features and rewrite the core app over 12 months.

### 3.1 Why Flutter?
*   **Rendering**: Owns every pixel on the screen (Skia Engine). No reliance on OEM widgets (unlike React Native).
*   **Performance**: AOT (Ahead-of-Time) compilation to ARM binary implies near-native performance.
*   **Web Support**: Can export the same code to WASM for a Web Admin Panel.

## 4. Migration Strategy: "Add-to-App"

We will not rewrite the app overnight.
1.  **Phase 1**: Integrate Flutter Module into existing Native Apps as a dependency.
2.  **Phase 2**: Build new "Account Profile" screen in Flutter.
3.  **Phase 3**: Slowly cannabalize native screens until 100% coverage.

## 5. Risk Assessment

| Risk | Mitigation |
| :--- | :--- |
| **Non-Standard UI** | Flutter widgets emulate iOS Look & Feel but are not exact. | We will adopt a "Brand First" design system, ignoring platform conventions intentionally. |
| **Dart Language** | Developers hate learning new languages. | Dart is very similar to Kotlin/Swift. We will run a 2-week workshop. |
| **Binary Size** | Flutter adds ~10MB to the APK size. | Acceptable trade-off for 4G/5G markets. |

## 6. Financial Projection (ROI)

*   **Savings**: We can reduce the hiring plan from needed +4 devs to +0. The existing 12 devs effectively become "24 devs" of velocity.
*   **Total Savings**: ~$600,000/year in avoided headcount costs.

## 7. Decision
**APPROVED**. The unified codebase allows us to enforce "Offline-First" architecture once, instead of continuously debugging SQLite sync issues on two platforms.
