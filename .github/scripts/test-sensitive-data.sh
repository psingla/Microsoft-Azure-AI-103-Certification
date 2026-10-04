#!/usr/bin/env bash
set -euo pipefail

config="$(pwd)/.gitleaks.toml"
temp="$(mktemp -d)"
trap 'rm -f -- "$temp/check.log" "$temp/repo/sample.txt"; rm -rf -- "$temp/repo/.git"; rmdir -- "$temp/repo" "$temp"' EXIT
mkdir "$temp/repo"
cd "$temp/repo"
git init -q
git config user.name "Guardrails test"
git config user.email "guardrails@example.invalid"
git config commit.gpgsign false
git config core.hooksPath "$temp/no-hooks"

expect_scan() {
    local label="$1" expected="$2" actual=0
    shift 2
    gitleaks git --config="$config" --redact=100 --no-banner --exit-code=42 "$@" . > "$temp/check.log" 2>&1 || actual=$?
    if [ "$actual" -ne "$expected" ]; then
        printf 'FAIL: %s (expected exit %s, received %s; raw output withheld)\n' "$label" "$expected" "$actual"
        exit 1
    fi
    printf 'PASS: %s\n' "$label"
}

printf '%s\n' 'https://<resource>.openai.azure.com/openai/v1/' \
    'https://<resource>.services.ai.azure.com/api/projects/<project>' \
    'https://learn.microsoft.com/en-us/azure/' > sample.txt
git add sample.txt
expect_scan "placeholders and public documentation allowed" 0 --pre-commit --staged
git commit -qm "Safe synthetic fixture"

printf 'https://guardrails-fixture.%s/openai/v1/\n' 'openai.azure.com' > sample.txt
git add sample.txt
expect_scan "staged real-shaped endpoint blocked" 42 --pre-commit --staged
printf '%s\n' 'https://<resource>.openai.azure.com/openai/v1/' > sample.txt
expect_scan "safe working copy cannot hide unsafe index" 42 --pre-commit --staged
git add sample.txt
expect_scan "sanitized staged endpoint allowed" 0 --pre-commit --staged

printf 'https://guardrails-fixture.%s/api/projects/fixture\n' 'services.ai.azure.com' > sample.txt
expect_scan "unstaged endpoint does not change scanned index" 0 --pre-commit --staged
git add sample.txt
expect_scan "Foundry endpoint blocked" 42 --pre-commit --staged
git commit -qm "Synthetic historical fixture"
printf '%s\n' 'https://<resource>.services.ai.azure.com/api/projects/<project>' > sample.txt
git add sample.txt
git commit -qm "Sanitize synthetic fixture"
expect_scan "history still detects removed endpoint" 42 --log-opts="--all --full-history"

printf '%s = "%s%s"\n' 'password' 'synthetic-' 'fixture-password' > sample.txt
git add sample.txt
expect_scan "literal password blocked" 42 --pre-commit --staged

printf '%s\n' 'safe fixture' > sample.txt
git add sample.txt
config="$temp/missing-config.toml"
actual=0
gitleaks git --config="$config" --pre-commit --staged --redact=100 --no-banner . > "$temp/check.log" 2>&1 || actual=$?
if [ "$actual" -eq 0 ]; then
    printf 'FAIL: missing configuration was accepted\n'
    exit 1
fi
printf 'PASS: missing configuration blocks the check\n'
