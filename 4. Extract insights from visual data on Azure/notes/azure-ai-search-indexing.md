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

[Microsoft Learn: Indexers](https://learn.microsoft.com/azure/search/search-indexer-overview) | [AI enrichment](https://learn.microsoft.com/azure/search/cognitive-search-concept-intro) | [OCR skill](https://learn.microsoft.com/azure/search/cognitive-search-skill-ocr) | [Text Merge skill](https://learn.microsoft.com/azure/search/cognitive-search-skill-textmerger)
