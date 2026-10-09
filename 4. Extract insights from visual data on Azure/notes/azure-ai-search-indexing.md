# Azure AI Search: Indexing and Enrichment

**Source -> indexer -> document cracking -> skillset -> index.**

- **Index:** stores searchable content in fields defined by an index schema.
- **Data source:** holds original content, such as documents in Azure Blob Storage or records in a supported database.
- **Indexer:** automates data extraction and index population; can run on demand or on a schedule.
- **Document cracking:** opens source documents and extracts text, metadata, and, when configured, images.
- **Enrichment pipeline:** an attached skillset adds information to an in-memory hierarchical JSON **enriched document**. Field/output mappings select what is persisted to the index.

![Diagram of an indexer extracting documents from a source and creating an index.](https://learn.microsoft.com/en-us/training/wwl-data-ai/ai-knowldge-mining/media/indexer.png)

*Diagram: Microsoft Learn.*

## Enriched document: Including image text

Illustrative tree; actual nodes depend on the source, image extraction settings, and skill output names:

```text
document
|-- metadata_storage_name
|-- metadata_author
|-- content
|-- normalized_images
|   |-- image0
|   |   `-- Text
|   `-- image1
|       `-- Text
|-- language
`-- merged_content
```

| Node | Meaning |
|---|---|
| `metadata_storage_name` | Source blob/file name |
| `metadata_author` | Author metadata, when available |
| `content` | Text extracted during document cracking |
| `normalized_images` | Image collection produced when image extraction is configured |
| `Text` under each image | OCR skill output containing text recognized in that image |
| `language` | Language detection skill output |
| `merged_content` | Merge skill output combining document text and OCR text |

**Important:** `image0` and `image1` above represent collection elements, not literal field names. Skills commonly target `/document/normalized_images/*`; output names such as `Text` are configurable.

**Exam cue:** Cracking extracts content; OCR reads image text; Merge combines text; the index stores mapped searchable fields.

**Caveats:** Not all indexing needs an indexer: applications can push documents through APIs/SDKs. Defining an index schema is separate from populating it, and the enriched document is not automatically identical to the stored index document.

## Built-in skills

**Built-in = ready-made enrichment; custom = your own processing logic.**

Include skills in the indexer's **skillset**. Foundry Tools capabilities such as Azure Vision and Azure Language support:

- Language detection, entity recognition, and key phrase extraction.
- Text translation and PII detection/masking.
- OCR for image text, plus image captions and tags.

**Access and billing:**

- A small free allowance supports billable AI enrichments for **20 documents per indexer per day**; it is not a separate restricted Search resource or a maximum index size.
- For larger workloads, attach a billable **Foundry resource to the skillset**.
- Resource-key billing requires the Foundry resource and Search service to be in the **same region**. Supported keyless configurations can differ; check current regional requirements.
- Not every built-in skill calls Foundry Tools: utility skills such as Shaper are different.

## Custom skills

- Extend enrichment with your own code, exposed through a **Custom Web API skill**, for example an HTTPS endpoint hosted in **Azure Functions**.
- Follow the skill input/output contract and return per-record results, errors, and warnings; custom processing is part of indexing, not query-time execution.

[Built-in skills](https://learn.microsoft.com/azure/search/cognitive-search-predefined-skills) | [Attach a billable resource](https://learn.microsoft.com/azure/search/cognitive-search-attach-cognitive-services) | [Custom Web API skill](https://learn.microsoft.com/azure/search/cognitive-search-custom-skill-interface)

## Query filters: Important distinction

**`search` matches text; `$filter` applies exact field conditions.**

- An **OData filter works with both simple and full Lucene search syntax**; full syntax is not required.
- Use `$filter` in REST GET queries, or `filter` in REST POST bodies and SDK calls.
- Fields used for ordinary field comparisons must be marked **filterable** in the index schema.
- Text conditions in a `search` expression are search matching, not a substitute for an OData field filter. Boolean query operators narrow text matches, not numeric/date ranges or exact field equality.

Example REST POST body:

```json
{
  "search": "invoice",
  "queryType": "simple",
  "filter": "Category eq 'Finance'"
}
```

This matches the text `invoice` and restricts results to the filterable `Category` value `Finance`.

**Example: London text + author filter**

```text
search=London
$filter=author eq 'Reviewer'
queryType=full
```

- Search searchable text fields for `London`; return only documents whose filterable `author` field equals `Reviewer`.
- `queryType=full` selects the Lucene parser; use the documented lowercase value. This plain text search and filter also work with `queryType=simple`.
- This does not specifically filter a location field. URL-encode parameter values when constructing a REST GET URL.

[Microsoft Learn: Filters](https://learn.microsoft.com/azure/search/search-filters) | [Simple query examples](https://learn.microsoft.com/azure/search/search-query-simple-examples)

[Microsoft Learn: Indexers](https://learn.microsoft.com/azure/search/search-indexer-overview) | [AI enrichment](https://learn.microsoft.com/azure/search/cognitive-search-concept-intro) | [OCR skill](https://learn.microsoft.com/azure/search/cognitive-search-skill-ocr) | [Text Merge skill](https://learn.microsoft.com/azure/search/cognitive-search-skill-textmerger)
