# Insight — TODO

This file answers only:

- what is DONE;
- what is NEXT;
- what is BLOCKED;
- what requires Human authority;
- what must not be changed yet.

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

## NEXT

- [ ] Select one real project for HOT-001 Primary Run. **HUMAN semantic selection required.**
- [ ] Freeze that project's HOT-001 Start Record before the run.
- [ ] Run HOT-001 with current system AS-IS and passive instrumentation only.
- [ ] Freeze immutable RAW event log.
- [ ] Evaluate RAW in a separate evaluation session using frozen criteria.

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
