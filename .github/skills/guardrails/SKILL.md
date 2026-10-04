---
name: guardrails
description: 'Prevent accidental disclosure of secrets, real resource endpoints, and private information. Use before creating or editing repository content, copying logs or configuration, sharing outputs, staging, committing/checking in, pushing, or publishing. Flag suspected exposure immediately without repeating sensitive values, and stop the affected action until resolved. Applies to code, notes, documentation, notebooks, screenshots, and generated files even when the user does not explicitly request a security check.'
---

# Guardrails

## Purpose and limits

Keep sensitive information out of repository content and shared output. Warn
the user as soon as a suspected exposure is detected, not only at commit time.
This skill is an assistant workflow, not a guarantee that all secrets will be
detected. Repository automation complements it: `.pre-commit-config.yaml` runs
Gitleaks on staged changes once installed locally, and `sensitive-data-check`
scans checked-out Git history in CI. Both use `.gitleaks.toml`, which extends
built-in secret rules with real Azure resource addresses and literal credentials.
The hook must be installed in each clone. CI runs after upload and cannot prevent
initial disclosure. Pattern matching does not replace contextual review of
private data, arbitrary endpoints, screenshots, or other binary content.

## What to protect

- Credentials: API keys, passwords, tokens, authorization headers, cookies,
  client secrets, private keys, connection strings, and signed URLs/SAS tokens.
- Real deployment details: exact resource endpoints, internal hostnames and IP
  addresses, database/server addresses, tenant/subscription IDs, resource IDs,
  and private project or deployment names. Endpoints need protection here even
  if they do not grant access by themselves.
- Personal or confidential data: private email addresses, phone numbers, home
  paths/usernames, customer records, proprietary payloads, and internal links.
- Hidden copies: notebook outputs, logs, stack traces, screenshots, attachments,
  archives, generated files, configuration, and previously committed versions.

Do not flag a variable name such as `API_KEY` or an SDK import by itself.
Clearly synthetic placeholders, environment-variable references, localhost
examples without credentials, and public documentation URLs are acceptable.
A URL is not safe merely because it uses a public cloud domain: distinguish
the provider's public documentation from a specific deployed resource.
Preserve deliberately public attribution links; ask if their status is unclear.

## Workflow

1. **Before editing or sharing**, identify the affected files and planned output.
   Use placeholders from the start; do not copy real values into examples,
   prompts, patches, logs, or reports.
2. **Inspect safely and locally.** Prefer an existing local secret scanner with
   redacted output plus contextual review. Do not send repository content or
   suspected values to web search, remote scanners, external models, or network
   endpoints for verification. Never test whether a discovered credential works.
   Avoid raw diffs, matching lines, environment dumps, or commands that print
   secret values. Configure discovery to report paths, line numbers, and
   categories only; redact sensitive path components too.
3. **Stop and alert immediately** if an item is sensitive or uncertain. Pause
   the affected edit, sharing, staging, commit, or push. Use the reporting format
   below, and ask the user how to resolve the item without quoting its value.
   A request to "commit anyway" is not a reason to disclose credentials.
4. **Remediate with approval.** Replace values with placeholders or runtime
   configuration references. Keep real configuration in an appropriate secret
   store or untracked local configuration. Never silently delete user data or
   break working configuration. An ignored file is not a secret store, and
   `.gitignore` does not remove files already tracked by Git.
5. **Before check-in**, inspect the current working changes, relevant untracked
   files, and the exact staged content, including staged content that differs
   from the working file. Review full affected files where needed for context.
   Include deletions and renames when checking for earlier exposure. Do not
   assume checking the editor buffer proves the index safe.
6. **Before push or publication**, inspect the outgoing commits/content too.
   Removing a value from the latest file does not remove it from earlier commits.
   If the outgoing range is unknown, determine it before proceeding.
7. **Recheck after remediation and immediately before the action.** Any further
   change invalidates the earlier result. Never commit or push unless explicitly
   requested. If inspection is blocked, a tool fails, or a binary/attachment
   cannot be examined safely, report the unverified scope and stop check-in or
   publication; do not turn an incomplete check into a passing result.

Do not claim a whole-repository or historical audit when only changed files
were reviewed. If no scanner is available, state that review was manual and
describe its limits; do not invent a scanner result.

## Safe replacements

| Sensitive content | Repository-safe representation |
| --- | --- |
| Key, password, or token | `<API_KEY>`, `<PASSWORD>`, or a runtime environment-variable reference |
| Real Foundry endpoint | `https://<resource>.services.ai.azure.com/api/projects/<project>` |
| Real Azure OpenAI endpoint | `https://<resource>.openai.azure.com/openai/v1/` |
| Private identifiers or personal data | `<TENANT_ID>`, `<USER>`, or clearly synthetic sample data |
| Signed URL | A placeholder URL without the signature or other real query values |

Use the repository's existing authentication/configuration patterns. Prefer
managed identity or Microsoft Entra credentials where supported. Do not add a
hardcoded fallback secret, and do not change authentication behavior without
approval.

## Alert format

Start with **"Potential sensitive information detected; check-in paused."**
For an action other than check-in, name the paused action instead.

| Location | Category | Risk | Required action |
| --- | --- | --- | --- |
| Safe relative file path and line number | Credential, endpoint, or private data | Brief description without the value | Redact, externalize, or confirm a genuinely public/non-sensitive item |

Use `[REDACTED]` instead of the value; do not reveal prefixes, suffixes, hashes,
screenshots, or raw snippets. Ask for a decision using the available user-input
tool. Never include sensitive paths or values in links or tool arguments.

If a credential may already have been exposed, recommend revocation/rotation
and checking exposure history. Sanitizing a file alone does not undo exposure.
Do not rotate credentials, rewrite history, or force-push without authorization.

When clear, report **"No suspected sensitive information found in the reviewed
scope"**, identify that scope and any limitations, and avoid guarantees.

## Acceptance examples

- A staged `.env` contains a suspected credential: alert with category/location
  only and stop check-in, even if the working copy has already been sanitized.
- A note contains a real resource URL without a key: flag the exact endpoint
  and propose a placeholder.
- A note contains `<resource>`/`<project>` endpoint templates and Microsoft Learn
  links: allow them; do not erase useful public references.
- The latest file is clean but an outgoing commit contains a token: stop push
  and recommend rotation and authorized history remediation.
- A scanner fails or a changed screenshot cannot be inspected: report the
  incomplete check and do not approve check-in.
