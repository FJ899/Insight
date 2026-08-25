# Insight

Insight is the experiment-control repository for architecture and product-reality evaluation around the current ecosystem.

It is **not** a Projector runtime, router, agent layer, or replacement for COS / Saddle / Ginseng / Executor / ScriptOps.

## Read order

1. `STATUS.md` — authoritative program-level current state.
2. `TODO.md` — what is DONE / NEXT / BLOCKED / HUMAN-ONLY / DO NOT.
3. `INSIGHTS.md` — high-value conceptual material that must survive individual AI sessions; not automatically current state.
4. `OPERATING_PROTOCOL.md` — working rules, including `AKCJA → GDZIE → ODESŁAĆ`.
5. `ARCHIVE_PROTOCOL.md` — RAW / session-harvest / insight preservation rules.
6. Experiment-local status under `experiments/`.

## Authority rule

- Root `STATUS.md` owns only program-level state.
- Each experiment owns its local detail in its own `STATUS.md`.
- Root state should point to local owners rather than duplicate their full truth.
- Frozen RAW artifacts are immutable evidence, not editable summaries.
- `INSIGHTS.md` preserves valuable hypotheses/reframings but does not grant them decision authority.

## Conversation continuity rule

Conversation history alone is not treated as durable usable knowledge state.

Material sessions should preserve:

```text
RAW source when available
→ SESSION HARVEST
→ INSIGHT promotion when valuable
→ DECISION / STATUS only when actually authorized
```

Technical detail remains available as trace/evidence; it should not crowd out the conceptual synthesis that would be expensive to rediscover.

## Experiment separation

`ARX-001` and `HOT-001` are independent experimental tracks.

Results from one track must not silently rewrite the frozen protocol, source corpus, metrics, or RAW artifacts of the other.

## Current program boundary

```text
ARCHITECTURE CHANGE: NOT AUTHORIZED
PRODUCT CHANGE BEFORE HOT-001 BASELINE: FORBIDDEN
```

The repository may organize, record, measure, archive, and evaluate. It must not use that role as implicit authority to redesign the product.
