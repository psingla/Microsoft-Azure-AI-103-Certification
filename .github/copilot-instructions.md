# Repository Instructions

## Privacy and security

Before creating or editing repository content, sharing output, staging,
committing/checking in, pushing, or publishing, invoke the `guardrails` skill
and follow [guardrails](skills/guardrails/SKILL.md). If skill discovery has not
refreshed yet, read that file directly and follow it.

Flag suspected secrets, exact resource endpoints, and private information
immediately without repeating their values. Pause the affected action until
resolved. Before check-in, review the exact staged content as well as working
changes; before pushing, include outgoing commits. Incomplete checks are not
approval to proceed. Install the repository's pre-commit hook for local
enforcement; the skill alone cannot block commits outside the assistant.
The `sensitive-data-check` workflow is a CI backstop, not prevention of the
initial push. Do not bypass a failed check or add broad allowlists to pass it.

## Study notes

Before creating, recording, or updating study notes in this repository, invoke
the `greatnotes` skill and follow [.github/skills/greatnotes/SKILL.md](skills/greatnotes/SKILL.md).
This applies even when the user does not name the skill.

Keep notes as concise as possible and easy to remember without sacrificing accuracy.
