# Insight — Conversation & Insight Archive Protocol

## Purpose

Important AI conversations generate more than decisions and implementation details. They also generate hypotheses, reframings, warnings, mental models, and short formulations that can materially change later work.

Those items must not remain trapped in a single chat session.

The archive therefore separates **raw history**, **insight extraction**, **current state**, and **technical evidence**.

## Core rule

```text
RAW CONVERSATION
!=
SESSION HARVEST
!=
INSIGHT
!=
DECISION
!=
CURRENT STATE
!=
TECHNICAL EVIDENCE
```

Do not use one layer as a substitute for another.

## Archive layers

### L0 — RAW SOURCE

Preserve the original conversation when the session is material.

Preferred artifact:

```text
verbatim transcript / export
+ timestamp
+ source/session identity
+ material attachment bytes or durable references
+ hashes when useful
```

A share URL alone is not a durable archive.

A transport/archive tool that omits attachment bytes, ordering, relationships, or completeness guarantees is useful as source transport but not sufficient as a full evidence ledger.

RAW is immutable once captured.

### L1 — SESSION HARVEST

At the end of a material session, create a short structured harvest using `schemas/SESSION_HARVEST_v1.md`.

The harvest exists to preserve what a future session should not have to rediscover.

It is not a transcript summary. It should explicitly capture:

- what changed;
- the strongest insight sparks;
- decisions actually made;
- hypotheses that remain unproven;
- unresolved loops;
- the next handoff;
- minimal pointers to technical evidence.

### L2 — INSIGHT LEDGER

Promote high-value ideas to root `INSIGHTS.md`.

An insight may be valuable even when it is not accepted, implemented, or currently actionable.

Preserve unusually strong AI wording verbatim when the wording itself carries useful compression or conceptual value.

### L3 — CURRENT STATE / DECISIONS

Only accepted current state belongs in `STATUS.md`, experiment status files, or explicit decision records.

```text
INSIGHT != DECISION
IDEA != TODO
GOOD FORMULATION != AUTHORITY
```

### L4 — TECHNICAL TRACE

Technical implementation detail remains available as evidence, but it should not crowd out the insight layer.

Prefer pointers to:

- repository / branch / SHA;
- file paths;
- commits / PRs;
- tests / artifacts;
- exact technical findings.

Do not delete necessary technical detail merely to make conversation shorter.

## Presentation rule for AI sessions

Default user-facing communication should be **insight-first, evidence-backed**.

For material work, prefer this order:

```text
1. WHAT CHANGED / CONCLUSION
2. IMPORTANT INSIGHT OR SURPRISING IMPLICATION
3. DECISION / STATUS
4. AKCJA → GDZIE → ODESŁAĆ
5. TECHNICAL TRACE only as much as needed for correctness
```

The goal is not "less technical thinking".

The goal is:

> keep technical detail in the evidence layer while reserving visible attention for the conceptual compression that would otherwise disappear inside implementation noise.

## Live insight capture

Do not rely only on an end-of-session summary.

When a materially new idea appears during a session, capture it as an `INSIGHT CANDIDATE` before continuing if losing it would be costly.

This is especially important for:

- reframings;
- unexpected causal explanations;
- new falsification criteria;
- product hypotheses;
- architecture-independent principles;
- concise AI formulations that materially improve understanding;
- contradictions that change the direction of work.

## Session closeout rule

A material session should not end with only technical completion.

Before closeout, ask:

```text
WHAT DID WE LEARN THAT IS NOT YET IN STATE/TODO?
WHAT WOULD BE EXPENSIVE TO REDISCOVER?
WHAT STRONG AI FORMULATION SHOULD SURVIVE THIS CHAT?
WHAT REMAINS ONLY A HYPOTHESIS?
```

Then persist the relevant harvest/insights.

## Backfill rule

Do not attempt to summarize every historical chat immediately.

Backfill in descending value order:

1. sessions that changed the mental model;
2. sessions that created or killed important hypotheses;
3. sessions containing unresolved high-value ideas;
4. sessions needed to reconstruct current decisions;
5. routine technical sessions only when their evidence is still material.

This avoids creating a second "state archaeology" project merely to archive the first one.
