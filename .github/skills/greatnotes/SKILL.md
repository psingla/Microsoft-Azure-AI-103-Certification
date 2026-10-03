---
name: greatnotes
description: 'Create and update concise, memorable study notes. Use before recording any notes in this repository, including mental notes, study summaries, comparisons, and revisions, even when the user does not explicitly name greatnotes.'
---

# Greatnotes

## Purpose

Turn learning material into the shortest accurate notes that are easy to recall.

## Note-Writing Style

- Make notes as concise as possible without losing essential meaning or accuracy.
- Make them easy to remember: lead with the key takeaway and use a short memory aid or contrast when helpful.
- Prefer plain language and short bullets over long paragraphs.
- Remove repetition, filler, and unnecessary background. Include examples or tables only when they clarify the idea more efficiently.
- Keep essential caveats; never simplify into a misleading rule.

## Inputs

Use the user's topic, source material, and requested destination. Reuse a known
destination from the conversation; ask only if the topic or location is unclear.

## Workflow

1. Read the relevant source material and any existing note before editing.
2. Identify the key takeaway, when to use it, and caveats needed to avoid misconceptions.
3. Verify new or uncertain technical claims against official documentation when available.
   Preserve existing references; state uncertainty rather than inventing facts or citations.
4. Write a compact Markdown note. Remove anything that does not improve understanding or recall.
5. Check accuracy, brevity, and the destination, then save and provide a short confirmation with a link.

## Output Format

- Use a descriptive title and lead with a one-line takeaway or memory aid.
- Add only essential bullets or a small comparison table; omit unnecessary sections.
- Include a short example or "when to use" rule only when it helps.
- Keep essential caveats and compact source links.
- Save new notes under `notes` in the requested topic folder, using descriptive kebab-case `.md` filenames.
- Update existing notes in place; preserve their paths and unique, relevant facts.
- Do not add a fixed word count or fill a template at the expense of concision.

## Quality Checklist

- Can the main idea be recalled from the opening line?
- Can anything be removed without losing useful meaning?
- Are important distinctions, caveats, and sources preserved?
- Is the note free of repetition, filler, and unsupported claims?

## Example

**User request:** "Make a mental note about two endpoint types and when to use each."

**Expected result:** A one-line distinction, a small comparison table, essential
caveats, and a source link in the requested notes folder, rather than a long tutorial.
