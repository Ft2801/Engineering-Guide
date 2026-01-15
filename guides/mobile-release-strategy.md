# Mobile Release Strategy (DevOps)

## 1. Abstract
Releasing a web app takes 2 minutes. Releasing a mobile app takes 2 days (Apple Review). This friction creates a "Fear of Releasing". We mitigate this via absolute automation.

---

## 2. The "Fastlane" Pipeline

Manual clicking in Xcode/Android Studio is forbidden. We define the release process as code (`Fastfile`).

### 2.1 The Swimlanes
1.  **Test**: Run Unit Tests and Snapshot Tests.
2.  **Match**: Sync Code Signing Certificates (Keys) from an encrypted git repo.
3.  **Gym**: Build the `.ipa` / `.apk` binary.
4.  **Deliver**: Upload to TestFlight / Google Play Internal Track.
5.  **Frameit**: Automatically frame screenshots inside device bezels.

### 2.2 Versioning
*   **Marketing Version**: `1.2.0` (SemVer).
*   **Build Number**: `20260501.1` (Integer or Date). Must increment on *every* CI run.

---

## 3. Over-The-Air (OTA) Updates

For hybrid apps (React Native / Flutter), we can bypass the App Store for JS bundle updates.
*   **Tools**: **CodePush** (Microsoft) or **Shorebird** (Flutter).
*   **Policy**: Use OTA only for critical bug fixes (Hotfix).
*   **Compliance**: Do not change the "Primary Purpose" of the app (Apple Guideline 2.5.2).

---

## 4. Feature Flagging on Client
Because users do not upgrade immediately, you will have versions v1.0, v1.1, and v1.2 live simultaneously.
*   **Rule**: Never release a feature securely enabled by code. Release it behind a **Remote Config** flag (Firebase/LaunchDarkly).
*   **Kill Switch**: Every app must listen to a `/status` endpoint. If the version is deprecated, force a modal blocking the user: "Update Required".
