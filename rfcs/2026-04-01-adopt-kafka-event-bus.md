# RFC-009: Decoupling via Event-Driven Architecture (Apache Kafka)

**Status**: Draft  
**Author**: Principal Architect  
**Date**: 2026-04-01  
**Stakeholders**: App Team, Data Team

---

## 1. Executive Summary
We propose shifting our inter-service communication from Synchronous HTTP (REST) to Asynchronous Events (Kafka) for all non-blocking operations. This will eliminate temporal coupling and enable real-time analytics.

## 2. Problem Statement
Our "Microservices" are actually a "Distributed Monolith".
*   **Temporal Coupling**: If the `Inventory Service` is down, the `Order Service` cannot accept orders (because it calls Inventory synchronously).
*   **Data Silos**: The Data Team scrapes databases via read-replicas, causing load and schema fragility.

## 3. Proposed Solution
Adopt **Apache Kafka** as the central nervous system.

### 3.1 The Pattern: "Smart Endpoints, Dumb Pipes"
*   **Producer**: `Order Service` emits `OrderCreated` event to Kafka. It does not care who listens.
*   **Consumer A**: `Inventory Service` listens, reserves stock.
*   **Consumer B**: `Notification Service` listens, emails user.
*   **Consumer C**: `Data Lake Sinks` listens, dumps to Snowflake.

### 3.2 Schema Registry
We will enforce **Avro** schemas.
*   Producers cannot publish data that violates the schema.
*   Schema evolution rules (Backward Compatibility) prevent breaking consumers.

## 4. Technology Selection

| Tool | Throughput | Durability | Operations | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **RabbitMQ** | Medium | RAM-based (Risk) | Easy | Good for simple work queues. |
| **Apache Kafka** | Extreme | Disk-based (Safe) | Hard (ZooKeeper/KRaft) | **Chosen**. The industry standard for replayability. |
| **AWS SQS/SNS** | High | Cloud Native | Zero Ops | Vendor Lock-in. No "Replay" capability. |

## 5. Strategic Evaluation
*   **Replayability**: Kafka keeps data for X days. If we deploy a *new* service today, it can read events from last week to backfill its state. This is a superpower.
*   **Complexity**: High. We will use a Managed Service (Confluent Cloud / Amazon MSK) to avoid managing brokers.

## 6. Implementation Plan
1.  **Month 1**: Provision MSK Cluster. Set up Schema Registry.
2.  **Month 2**: Migrate "User Registration" flow (Low Risk).
3.  **Month 3**: Migrate "Checkout" flow (High Risk).

## 7. Decision
**APPROVED**. The ability to "Replay" history and decouple uptime makes Kafka essential for our scale.
