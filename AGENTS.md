# AGENTS.md — Operational Constitution & Harness Rules

## 1. Environment & Deterministic Sensors
- **Package Manager:** `uv` (or `pip` inside active `.venv`)
- **Test Sensor:** `pytest -v`
- **Lint & Type Sensor:** `ruff check . && mypy app/`
- Run sensors after every logical code change. Never claim a task is complete without green sensor output.

## 2. Architecture & Bounded Contexts
- **Strict Decoupling:** Keep API request/response contracts (`app/schemas.py`) strictly separate from internal business logic and database models.
- **Configuration:** Never hardcode secrets, ports, or host URLs. Load all environment state via `pydantic-settings`.
- **Shell Safety:** All shell scripts must begin with `set -euo pipefail`. Never execute destructive commands (`rm -rf`, `git reset --hard`, `dropdb`) without explicit human confirmation.

## 3. Anti-Reward-Hacking (Immutable Boundaries)
- **Never Game the Grader:** When a test fails, fix the implementation—NEVER weaken, delete, or mock out test assertions in `tests/` just to force a passing exit code.
- **No Silent Suppression:** Never wrap failing logic in broad `try/except: pass` blocks, `# type: ignore`, or `# noqa` to silence sensors without fixing the root cause.
- **No Unvetted Dependencies:** Do not install new external packages without asking first.

## 4. Machine Sympathy: Bounded Autonomy & Escalation Protocol
You are permitted—and expected—to halt and ask for human help rather than forcing hacky workarounds, subject to this calibration rule:

- **Prevent Laziness (The 2-Attempt Floor):** Do not escalate trivial syntax, import, or type errors on the first failure. Read the traceback, inspect the local file context, and attempt up to **2 grounded fixes**.
- **Prevent Error Spirals (The 3-Strike Ceiling):** If the same test or build error persists after **2 repair/fix attempts**, or if fixing it requires violating an architectural boundary in Section 2, **STOP IMMEDIATELY**. Do not guess a 3rd time.
- **Ambiguity Gate:** If a prompt has missing requirements affecting data schemas, security boundaries, or public APIs, ask before writing implementation code.

### Required Escalation Format
When halting for human-in-the-loop intervention, output a concise **Blocker Report**:
1. **Root Cause / Collision:** The exact error or architectural constraint blocking progress.
2. **Attempted Fixes:** What was tried in the 1–2 attempts and why it failed.
3. **Decision Options:** 2 concrete paths forward with their trade-offs for the human to choose from.