# Edge Computing and IoT Standards

## 1. Abstract
The speed of light is a hard constraint. A user in Sydney accessing a server in Virginia faces ~200ms of latency (RTT). We defeat physics by moving data and compute to the Edge (within 50ms of the user).

---

## 2. Content Delivery Strategy (CDN)

We do not just cache images. We cache **Logic**.

### 2.1 Caching Directives
*   `Cache-Control: public, max-age=31536000, immutable`: For versioned assets (JS/CSS).
*   `stale-while-revalidate`: Serve old data instantly, fetch new data in background.

### 2.2 Edge Compute (Serverless)
*   **Technology**: Cloudflare Workers / AWS Lambda@Edge / Vercel Edge.
*   **Use Cases**:
    *   **A/B Testing**: Assign variant based on Cookie *at the edge*.
    *   **Auth**: Verify JWT token validity *before* hitting the origin.
    *   **Geo-Routing**: Redirect user to the nearest regional database.

---

## 3. IoT Protocols (Internet of Things)

HTTP is too heavy (headers) and battery-hungry (TCP keep-alive) for sensors.

| Protocol | Transport | Overhead | Use Case |
| :--- | :--- | :--- | :--- |
| **MQTT** | TCP | Low (2 bytes header) | **Standard**. Smart Plugs, Telemetry. Pub/Sub model. |
| **CoAP** | UDP | Very Low | Constrained devices (Microcontrollers with < 64KB RAM). |
| **WebSockets** | TCP | High | Real-time dashboards (Browser-compatible). |

### 3.1 MQTT Architecture
We use a **Broker** architecture. Devices never talk to each other directly.
*   *Topic Design*: `home/{floor}/{room}/{device_id}/status`.
*   *QoS 1*: "At least once delivery" (Standard).

---

## 4. The "Fog" Architecture

Between the Cloud and the Device implies the "Fog".
*   **Local Processing**: The Gateway (e.g., a Raspberry Pi in a factory) aggregates 1000 sensor readings/sec and sends 1 summary/sec to the Cloud.
*   **Rule**: Never send raw high-frequency sensor data to the cloud (Bandwidth cost/Latency).
