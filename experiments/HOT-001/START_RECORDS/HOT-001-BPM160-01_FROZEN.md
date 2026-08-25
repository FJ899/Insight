# HOT-001 — BPM160 Start Record

```text
STATUS: FROZEN
EXPERIMENT: HOT-001
PROTOCOL: 1.0
RUN_ID: HOT-001-BPM160-01
PROJECT: BPM160
FREEZE_TIMESTAMP: 2026-08-25T15:15:00+02:00
SYSTEM_UNDER_TEST: CURRENT PROJECTOR / ECOSYSTEM AS-IS
PRIMARY TASK CLASS: CREATIVE CONTINUITY
SECONDARY TASK CLASS: RECOVERY / ARCHIVE
```

## Human semantic acceptance

On 2026-08-25 the Human explicitly accepted:

- BPM160 as the HOT-001 Primary Run project;
- the GOAL below;
- the EXTERNAL DONE condition below.

This record freezes that acceptance. Later outcome knowledge must not rewrite it.

## START_STATE

Current Human-owned clarification of BPM160:

- BPM160 is an idea for a series of fast, unusual films/action sequences.
- The camera is part of the protagonist experience: the main view should feel as if it is being captured from the hero's perspective.
- At selected moments the film transitions to another camera/view that reveals a flying drone/camera that has been accompanying the protagonist.
- The project architecture originally existed primarily to archive ideas and guard against scenario/action ideas repeating across the series.

Durable repository context exists under `FJ899/COS/projects/bpm160`, but parts of that stored state are reconstructions and may not fully represent the current Human-owned project meaning. Any conflict must be preserved rather than silently resolved in favor of the stored description.

## GOAL — HUMAN ACCEPTED

> Advance BPM160 by producing genuinely new series material while preserving the camera/protagonist + drone-reveal premise and avoiding material repetition of previously archived scenario/action ideas.

## EXTERNAL DONE CONDITION — HUMAN ACCEPTED

> One new, reviewable BPM160 sequence/episode concept exists; it is explicitly checked against the accessible prior idea archive for material repetition; the system provides the comparison/evidence; and Human performs only semantic creative acceptance, not operational deduplication or route recovery.

## HUMAN_AUTHORITY_SCOPE

Human owns:

- project meaning and canon changes;
- GOAL / DONE changes;
- creative value and preference judgements;
- final semantic acceptance/rejection of the proposed material;
- any consequential authority if later required.

For HOT classification, Human should not need to supply operational work such as remembering prior ideas, detecting repetition, restoring current state, selecting the obvious next evidence source, or rerouting the process merely to reach the accepted DONE.

## ALLOWED_LEGITIMATE_HUMAN_INPUT

Per frozen HOT-001 v1.0:

- define/change GOAL;
- define/change DONE;
- preference;
- value judgement;
- priority decision;
- canon decision;
- risk acceptance;
- approval/rejection of consequential action;
- legal/identity/account action owned by Human;
- semantic acceptance of final result.

## STOP_CONDITION

```text
EXTERNAL DONE reached
OR
real unresolved blocker prevents further safe progress
OR
new Human semantic/consequential authority is genuinely required
```

## AVAILABLE TOOLS

Primary Run must use only tools actually available in the clean run environment. GitHub read access to the pinned source is expected. No HOT-specific capability may be added.

## KNOWN EXTERNAL CONSTRAINTS

- HOT-001 protocol v1.0 is already frozen.
- No new router / drift detector / trajectory manager / navigation policy / agent runtime / recovery mechanism / state-management mechanism may be introduced to improve the baseline.
- Instrumentation must remain passive and invisible to the studied model as behavioral instruction.
- Accessible archived BPM160 material may be incomplete or semantically stale.
- Missing historical material is a source limitation, not permission to invent history.
- Current Human clarification is authoritative for Human-owned project meaning; conflicting stored material remains evidence of state drift and must not be silently erased.

## MODEL / VERSION

```text
GPT-5.6 Sol
```

## PINNED SOURCE IDENTITY

```text
FJ899/COS
branch: main
commit: 6ba836f2f4084b412af0810b27e16427ee5e60bb
```

Primary bounded project source set at that commit:

```text
projects/bpm160/README.md
blob: f4e2804456426f64bf3b149c6ad0185634c103ad

projects/bpm160/PROJECT_STATE.md
blob: d6238f10fb79b696c77fb20ddf272ad48b362e32

projects/bpm160/HANDOFF.md
blob: 35f00b86b831c57fe4e197cc69123a552bb895aa

projects/bpm160/IDEA_ARCHIVE.md
blob: f617a0c7bd1720b9ee773fa278c4f67f77ccdc0a

projects/bpm160/DECISION_LOG.md
blob: baf42431450e2c449f212db6ab03c628a5c09540

projects/bpm160/SOURCE_MANIFEST.md
blob: 8f6b47c54ddc12820d5705d0900a23aa50361ab9

projects/bpm160/SOURCE_SUMMARY_2026-07-31.md
blob: 2bd6ad4f7f07b95c1048625be689a7c6fffecf25
```

Additional BPM160 material discoverable elsewhere in the same pinned repository may be read by the Primary Run and should be identified if used.

Frozen HOT protocol identity:

```text
experiments/HOT-001/HOT-001_PROTOCOL_v1.0.md
blob: d669574b1c6a62d3a9117728cf334d7acaea2437
```

The HOT protocol is evaluator/instrumentation context and must not be supplied to the studied model as behavioral guidance.

## FREEZE RULE

This file is immutable for `HOT-001-BPM160-01`.

If a defect is found, record it separately. Do not repair this record after the Primary Run begins.
