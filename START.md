# Insight

Insight is the experiment-control repository for architecture and product-reality evaluation around the current ecosystem.

It is **not** a Projector runtime, router, agent layer, or replacement for COS / Saddle / Ginseng / Executor / ScriptOps.

## Read order

1. `STATUS.md` — authoritative program-level current state.
2. `TODO.md` — what is DONE / NEXT / BLOCKED / HUMAN-ONLY / DO NOT.
3. `OPERATING_PROTOCOL.md` — working rules, including `AKCJA → GDZIE → ODESŁAĆ` and `W / Z` capture commands.
4. Experiment-local status under `experiments/`.

## Quick capture

```text
W → save the immediately preceding Assistant response to W.md
Z → save the immediately preceding Assistant response to Z.md
```

No summarization or reinterpretation unless Human explicitly asks for it.

`W.md` and `Z.md` are capture files, not authoritative current state.

## Authority rule

- Root `STATUS.md` owns only program-level state.
- Each experiment owns its local detail in its own `STATUS.md`.
- Root state should point to local owners rather than duplicate their full truth.
- Frozen RAW artifacts are immutable evidence, not editable summaries.

## Experiment separation

`ARX-001` and `HOT-001` are independent experimental tracks.

Results from one track must not silently rewrite the frozen protocol, source corpus, metrics, or RAW artifacts of the other.

## Current program boundary

```text
ARCHITECTURE CHANGE: NOT AUTHORIZED
PRODUCT CHANGE BEFORE HOT-001 BASELINE: FORBIDDEN
```

The repository may organize, record, measure, and evaluate. It must not use that role as implicit authority to redesign the product.
