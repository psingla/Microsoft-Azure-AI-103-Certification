# Azure Language: Text Analysis

**Remember: Language understands text; OCR reads images; Translator translates.**

- **Azure Language in Foundry Tools** provides ready-to-use NLP capabilities through REST APIs and SDKs for applications, and supported tools for agents.
- Choose the capability that matches the task:

| Need | Capability |
|---|---|
| Identify the language of incoming text | Language detection |
| Extract names, organizations, places, or dates | Prebuilt named entity recognition (NER) |
| Extract domain-specific entity categories | Custom NER |
| Detect sensitive personal information for redaction | PII detection |

**Example:** A support app detects a message's language, extracts relevant entities, and redacts detected PII before permitted downstream processing.

**Caveats:** Detection is not guaranteed to find every entity or sensitive value. Check feature-specific language support, limits, and lifecycle status; protect inputs and logs as well as outputs.

[Microsoft Learn: Azure Language overview](https://learn.microsoft.com/azure/ai-services/language-service/overview) | [Learning path](https://learn.microsoft.com/training/paths/develop-language-solutions-azure-ai/)
