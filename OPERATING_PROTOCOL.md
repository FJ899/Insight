# Insight — Operating Protocol

## 1. Default work format

Every material task or handoff uses:

```text
AKCJA
What is being done, its boundaries, and the completion condition.

GDZIE
Exact scope identity: repository / branch / SHA / file / experiment.
Use PINNED or LIVE when that distinction matters.

ODESŁAĆ
Exactly one next handoff required from the recipient, or NIC.
```

## 2. Continue-until-authority rule

Default behavior:

> Continue the work autonomously for as long as it can be performed safely, correctly, and within already granted authority.

Do not stop merely because a later step may require Human involvement.

Before asking Human, complete every available non-consequential and already-authorized step that materially advances the task.

Ask Human only at the actual boundary where one of the following is required:

- Human semantic decision;
- Human-owned goal / DONE / priority / canon decision;
- new consequential authority;
- legal, identity, account, financial, or other Human-owned action;
- scope expansion not already authorized;
- genuinely missing information that cannot be resolved from accessible authoritative sources.

## 3. No ceremonial confirmation

Do not ask Human to approve routine continuation when:

- the task is already authorized;
- the next step is read-only or non-consequential;
- the action stays inside the exact accepted scope;
- no new authority or semantic decision is created.

## 4. State discipline

- `STATUS.md` is authoritative for program-level current state.
- `TODO.md` records DONE / NEXT / BLOCKED / HUMAN AUTHORITY / DO NOT.
- Experiment-local truth belongs to that experiment's local `STATUS.md`.
- Root files point to local owners instead of duplicating detailed state.
- If two state surfaces conflict, preserve the conflict; do not silently choose the more convenient one.

## 5. Evidence discipline

```text
SOURCE != EVIDENCE
CLAIM != OBSERVATION
PROPOSAL != DECISION
DECISION != AUTHORITY
AUTHORITY != EFFECT
EFFECT CLAIM != OBSERVED EFFECT
STORED STATE != TRUTH
```

Use `UNKNOWN` when evidence is insufficient.

## 6. Frozen experiment discipline

For a frozen protocol:

- do not modify prompts, metrics, classifications, source selection, or evaluation rules after seeing a primary result;
- do not rewrite immutable RAW artifacts;
- if a protocol defect is discovered, record the defect and create a later protocol version rather than silently repairing the current one;
- keep exploratory/post-hoc work explicitly separate from preregistered evidence.

## 7. Architecture discipline

A discovered requirement does not automatically justify a component.

```text
REQUIRED PROPERTY
!=
CURRENT IMPLEMENTATION
!=
CURRENT COMPONENT BOUNDARY
!=
PROPOSED SUBSTITUTE
```

Before deleting or absorbing a mechanism, identify a concrete substitute for every real property it protects.

## 8. Experiment separation

ARX-001 asks what must exist architecturally.

HOT-001 asks how much Human operational orchestration the current system requires.

They may inform later synthesis only after their own frozen stages are complete. They must not silently alter each other's preregistered inputs.

## 9. Simple capture commands

Default capture is deliberately simple.

```text
W
→ append the immediately preceding Assistant response verbatim to W.md

Z
→ append the immediately preceding Assistant response verbatim to Z.md

W: <text>
→ append exactly that text to W.md

Z: <text>
→ append exactly that text to Z.md
```

Rules:

- append, do not summarize;
- preserve wording;
- add only timestamp and minimal source context;
- do not classify or reinterpret unless Human explicitly asks;
- `W.md` and `Z.md` are capture files, not authoritative current state.

The previous archive/harvest machinery is not the default workflow. Use it only if Human explicitly asks for a structured archive or retrospective reconstruction.
