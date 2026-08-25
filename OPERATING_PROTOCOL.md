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

## 9. Insight preservation discipline

A material AI session may create valuable knowledge that is neither current state nor an implementation artifact.

Preserve it explicitly.

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
```

- `ARCHIVE_PROTOCOL.md` owns archive/harvest rules.
- `INSIGHTS.md` stores high-value conceptual material that must survive session boundaries.
- Material sessions should use `schemas/SESSION_HARVEST_v1.md` before closeout.
- Strong AI wording may be preserved verbatim when the wording itself carries useful conceptual compression.
- Do not promote an insight into state/TODO merely because it is compelling.
- Use `UNKNOWN`, `OPEN`, or `PARKED` rather than manufacturing certainty.

## 10. Insight-first communication, evidence-backed execution

Do **not** reduce technical rigor merely to make the conversation shorter.

Instead separate presentation layers.

Default visible order for material work:

```text
1. WHAT CHANGED / CONCLUSION
2. IMPORTANT INSIGHT / IMPLICATION
3. DECISION / STATUS
4. AKCJA → GDZIE → ODESŁAĆ
5. TECHNICAL TRACE only as much as needed
```

Technical detail should remain available in repositories, commits, tests, artifacts, or explicit trace sections.

The goal is to prevent implementation narration from consuming the attention needed for high-value reasoning and synthesis.

## 11. Material-session closeout

Before ending a material session, check:

```text
WHAT DID WE LEARN THAT IS NOT YET IN STATUS/TODO?
WHAT WOULD BE EXPENSIVE TO REDISCOVER?
WHICH AI FORMULATION SHOULD SURVIVE THIS CHAT?
WHAT REMAINS ONLY A HYPOTHESIS?
```

Persist the answer as a session harvest and/or insight entry when material.
