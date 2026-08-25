# Insight — TODO

This file answers only:

- what is DONE;
- what is NEXT;
- what is BLOCKED;
- what requires Human authority;
- what must not be changed yet.

It is also the active work queue.

Rule:

```text
WHEN A STEP ENDS
AND ODESŁAĆ = NIC
→ reload this file
→ take the next actionable item
→ continue
```

Stop only at a real Human authority/semantic gate or an unresolved BLOCKED item.

## DONE

- [x] Create Insight as a separate experiment-control repository.
- [x] Establish `START.md` as entrypoint.
- [x] Establish root `STATUS.md` as authoritative program-level state.
- [x] Separate ARX-001 from HOT-001.
- [x] Persist `OPERATING_PROTOCOL.md`.
- [x] Persist ARX-001 local status.
- [x] Persist HOT-001 local status.
- [x] Freeze HOT-001 baseline protocol v1.0.
- [x] Persist `HANDOFF_v1`, `HOT_EVENT_v1`, and `START_RECORD_v1` schemas.
- [x] Adopt `AKCJA → GDZIE → ODESŁAĆ` as the working handoff format.
- [x] Adopt continue-until-authority rule: perform all safe, already-authorized work before asking Human.
- [x] Adopt TODO continuation rule: `ODESŁAĆ = NIC` means load the next actionable TODO item and keep working.
- [x] Simplify conversation capture to two commands: `W` → `W.md`, `Z` → `Z.md`.
- [x] Screen existing COS project directories for HOT-001 suitability.
- [x] Classify useful HOT task classes without changing the frozen protocol: CREATIVE CONTINUITY / OPERATIONAL DELIVERY / REVENUE-MARKET / RESEARCH-DISCOVERY / RECOVERY-ARCHIVE.
- [x] Reclassify BPM160 from generic execution project to `CREATIVE CONTINUITY` primary + `RECOVERY / ARCHIVE` secondary based on current Human clarification.
- [x] Prepare `experiments/HOT-001/START_RECORDS/BPM160_DRAFT.md` with all non-semantic fields that can be prepared before project selection.

## NEXT — HUMAN GATE

- [ ] Confirm or reject `BPM160` as the HOT-001 Primary Run project.
- [ ] If confirmed, accept or replace the candidate GOAL and EXTERNAL DONE in `BPM160_DRAFT.md`.

Candidate GOAL:

> Advance BPM160 by producing genuinely new series material while preserving the camera/protagonist + drone-reveal premise and avoiding material repetition of previously archived scenario/action ideas.

Candidate EXTERNAL DONE:

> One new, reviewable BPM160 sequence/episode concept exists; it is explicitly checked against the accessible prior idea archive for material repetition; the system provides the comparison/evidence; and Human performs only semantic creative acceptance, not operational deduplication or route recovery.

After Human resolves this gate, the next autonomous steps are:

- freeze the Start Record;
- begin the HOT-001 Primary Run with current system AS-IS;
- freeze RAW events;
- stop only at the next genuine Human authority/semantic gate or real blocker.

## BLOCKED

- [ ] ARX-001 R1A Substitute Pass as a formal v1.0 stage.
  - Exact standalone executable frozen prompt has not been recovered.
  - Methodology existed before R1A, but that is not equivalent to a frozen executable stage artifact.
  - Do not reconstruct it from known R1A results and call it frozen v1.0.

## HUMAN AUTHORITY REQUIRED

Human input is required only when the next step genuinely belongs to Human semantic or consequential authority, including:

- selecting/changing GOAL;
- defining/changing DONE;
- value/preference/priority decisions;
- canon decisions;
- risk acceptance;
- approval/rejection of consequential action;
- legal/account/identity actions owned by Human;
- semantic acceptance of a final result.

Operational work that can be done safely and within existing authority should continue without asking Human merely for permission to proceed.

## DO NOT

- [ ] Do not refactor COS from R1A conclusions.
- [ ] Do not delete or absorb Saddle yet.
- [ ] Do not redesign Executor yet.
- [ ] Do not build a Ginseng runtime.
- [ ] Do not replace ScriptOps yet.
- [ ] Do not build Projector v2 before HOT-001 baseline.
- [ ] Do not add router / drift detector / trajectory manager / new navigation policy before HOT-001 baseline.
- [ ] Do not contaminate ARX-001 with HOT evidence unless a frozen ARX stage explicitly permits it.
- [ ] Do not turn `W.md` or `Z.md` into authoritative state automatically.
