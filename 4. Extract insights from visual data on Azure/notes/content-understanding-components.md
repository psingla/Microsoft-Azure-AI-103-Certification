# Content Understanding: Components

**Input -> analyzer -> content extraction -> schema fields -> structured output.**

Azure Content Understanding in Foundry Tools turns unstructured content into usable content and structured fields.

| Component | Purpose |
|---|---|
| **Inputs** | Source documents, images, video, or audio |
| **Analyzer** | Defines processing settings and the field schema |
| **Content extraction** | Produces normalized text and metadata through capabilities such as OCR, speech transcription, and layout detection |
| **Field extraction** | Produces structured key-value pairs matching your schema |
| **Confidence scores** | Estimates field-value reliability on a **0-1** scale; higher means more confident, not guaranteed correct |
| **Grounding** | Links field values to supporting source regions, such as document pages and bounding boxes |
| **Structured output** | **Markdown** content for search/RAG; schema-aligned **JSON** for automation and analytics |

**Important:** For document field confidence and grounding, opt in with `estimateFieldSourceAndConfidence = true` in the analyzer, or `estimateSourceAndConfidence = true` for a specific field. Do not assume every modality or configuration returns both.

**Exam cue:** Confidence asks **"How reliable?"**; grounding asks **"Where is the evidence?"** Route low-confidence or insufficiently grounded values for human review.

[Microsoft Learn: Content Understanding components](https://learn.microsoft.com/azure/ai-services/content-understanding/overview#key-components-of-content-understanding) | [Document field extraction](https://learn.microsoft.com/azure/ai-services/content-understanding/document/overview#field-extraction)
