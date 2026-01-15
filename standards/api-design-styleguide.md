# API Design Styleguide

## 1. Introduction
APIs are the "User Interface" for developers. A confusing API breaks the integration ecosystem. We mandate a **Contract-First** approach.

## 2. Protocol Selection Matrix

Choosing the transport protocol dictates the performance and flexibility characteristics.

| Protocol | Format | Use Case | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| **REST (Level 2)** | JSON | **Public / Partner APIs** | Universally understood. Cacheable (HTTP). | Verbose "Chatty" interfaces. Over-fetching. |
| **gRPC** | Protobuf | **Internal Microservices** | Extreme Performance (binary). Typed contracts. | Browser support requires Proxy (gRPC-Web). Hard to debug (binary). |
| **GraphQL** | JSON | **Mobile / Frontend** | One request per view. No Over-fetching. | Security risk (DoS via deep query). Complex caching. |

---

## 3. The "Contract First" Rule

You **MUST NOT** write code until the Interface Definition Language (IDL) file is approved.

*   **REST**: Write the `openapi.yaml` (v3.1) spec first.
    *   *Tool*: Stoplight Studio / Swagger Editor.
*   **gRPC**: Write the `.proto` file first.
    *   *Tool*: Buf / Protoc.

### 3.1 Why?
*   **Parallel Dev**: Frontend developers can mock the API using the spec before the Backend exists.
*   **Generation**: Client SDKs (TypeScripts/Go/Python) are auto-generated from the spec. (No manual typing).

---

## 4. REST Standards (The Default)

### 4.1 Resource Naming
*   **Plural Nouns**: `/users`, `/orders`.
*   **Kebab-case URLs**: `/users/123/shipping-address` (Not `shippingAddress`).
*   **Nesting**: Max depth of 2. `/users/123/orders/99/items` is too deep. Use `/orders/99/items` instead.

### 4.2 Versioning
*   **Header Versioning**: `Accept: application/vnd.company.v1+json`.
*   *Rationale*: Keep URLs clean. Allows content negotiation.

### 4.3 Idempotency
*   **POST**: Not Idempotent (Create).
*   **PUT**: Idempotent (Replace).
*   **PATCH**: Idempotent (Update partial).
*   *Requirement*: Clients retrying a failed `PUT` must not duplicate data.

---

## 5. gRPC Standards

### 5.1 Backward Compatibility
Never delete a field index.
*   *Bad*: `string name = 1;` -> `// string name = 1;` -> `int32 age = 1;`. (Breaks wire compatibility).
*   *Good*: `string name = 1 [deprecated=true];` ... `int32 age = 2;`.

---

## 6. Error Handling Standard (RFC 7807)

All APIs must return standardized "Problem Details" JSON.


```json
{
  "type": "https://api.co/errors/insufficient-funds",
  "title": "Insufficient Funds",
  "status": 403,
  "detail": "Account 123 balance is $10.00, tx required $15.00",
  "instance": "/tx/999"
}
```

---

## 7. Mobile Optimization

Mobile networks are expensive (Data Caps) and high-latency.

### 7.1 Compression
*   **Brotli (`br`)**: Mandatory over Gzip. Provides ~20% better compression.
*   **Images**: Serve `WebP` or `AVIF`. **Never** serve raw PNG/JPEG.

### 7.2 Pagination
*   **Offset-based**: `page=2`. **Forbidden** for infinite scroll (Performance degradation on SQL `OFFSET`).
*   **Cursor-based**: `after=txn_123`. **Mandatory** for mobile feeds.
*   **Partial Response**: Clients should request only needed fields (`?fields=id,name,avatar`).

