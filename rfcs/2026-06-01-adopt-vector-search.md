# RFC-015: Semantic Search Capability (Vector Database)

**Status**: Draft  
**Author**: Lead ML Engineer  
**Date**: 2026-06-01  
**Stakeholders**: Product, Search Team

---

## 1. Executive Summary
We propose augmenting our existing Lucene-based search (Elasticsearch) with a **Vector Database** (Weaviate). This enables "Semantic Search" (matching intent) rather than just "Lexical Search" (matching keywords), increasing conversion rates by an estimated 15%.

## 2. Problem Statement
*   **The "Synonym" Problem**: Users searching for "Running Shoes" do not find products labeled "Sneakers".
*   **Zero Results**: 20% of user queries return 0 results because of typos or mismatched terminology.

## 3. Proposed Solution
Adopt **Weaviate** as a dedicated Semantic Search Engine.

### 3.1 Architecture
1.  **Ingestion**: An ETL pipeline reads products from the Data Lake.
2.  **Embedding**: An OpenAI model (`text-embedding-3-small`) converts product descriptions into 1536-dimensional vectors.
3.  **Indexing**: Vectors are stored in Weaviate using HNSW index.
4.  **Query**: User text is embedded on-the-fly and compared using Cosine Similarity.

### 3.2 Hybrid Search (Best of Both Worlds)
We will not replace keyword search. We will combine them (Reciprocal Rank Fusion).
*   *Score* = $Weight_{keyword} \times Score_{BM25} + Weight_{vector} \times Score_{Cosine}$

## 4. Cost Analysis

| Component | Cost | Notes |
| :--- | :--- | :--- |
| **Weaviate Cloud** | $500/mo | Managed Index hosting. |
| **OpenAI API** | $200/mo | Embedding generation cost ($0.00002/1k tokens). |
| **Total** | **$700/mo** | Negligible compared to conversion uplift. |

## 5. Alternatives

| Option | Pros | Cons |
| :--- | :--- | :--- |
| **pgvector** (Postgres) | Free (existing infrastructure). | Performance degrades > 10M vectors. No Hybrid Search native. |
| **Pinecone** | Market Leader. | Expensive at scale. Closed source. |
| **Weaviate** | Open Source. Good Hybrid Search. | Complex Kubernetes deployment (if self-hosted). |

## 6. Decision
**APPROVED**. We adopt Weaviate in the Cloud. The move to Hybrid Search is the industry standard for 2026 e-commerce.
