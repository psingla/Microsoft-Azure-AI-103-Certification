# Azure AI Search for RAG retrieval

**Search retrieves the evidence; the language model uses it to generate an answer.**

Azure AI Search can provide the retrieval layer for RAG in Microsoft Foundry.

![An Azure AI Search index supplies grounding data for a user question.](https://learn.microsoft.com/en-us/training/wwl-data-ai/optimize-generative-ai-model-performance/media/index.png)

*Diagram: Microsoft Learn.*

## Flow: ingest, index, retrieve, generate

1. **Ingest:** bring in documents from sources such as Blob Storage, ADLS Gen2, OneLake, or file uploads, depending on the supported connector and workflow.
2. **Index:** split content into chunks; for vector retrieval, create embeddings and store them alongside searchable text and metadata in Azure AI Search.
3. **Retrieve:** search for relevant chunks. Vector queries require a query embedding compatible with the indexed content's embedding model.
4. **Generate:** supply retrieved chunks with the question to the language model as grounding context.

## Search techniques

| Technique | What it does |
|-----------|--------------|
| **Keyword / full-text** | Matches analyzed terms and ranks results using BM25; useful for names, codes, and specific wording. Not limited to literal exact-string matches. |
| **Vector** | Compares embeddings to find similar meaning, even when wording differs. |
| **Hybrid** | Runs keyword and vector searches in parallel, then merges their rankings using reciprocal rank fusion (RRF). |
| **Semantic ranker** | Reranks an initial result set using language understanding; it is not a replacement for retrieval. |

**Remember: hybrid = keyword + vector; semantic ranking = optional reranking afterward.**

Hybrid search with semantic ranking is a strong starting point for RAG; evaluate relevance, latency, and cost on your own questions. Embeddings are not required for keyword-only search, and grounding reduces errors but does not guarantee correctness.

## Sources

- [Microsoft Learn: Hybrid search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview)
- [Microsoft Learn: Semantic ranking](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)

*Search definitions checked against Microsoft Learn on 2026-10-04.*
