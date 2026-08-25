# HOT-001 — Local Status

## Identity

```text
EXPERIMENT: HOT-001
NAME: HUMAN ORCHESTRATION TAX BASELINE
PROTOCOL: 1.0
MODE: AS-IS / OBSERVATIONAL
STATUS: FROZEN BEFORE PRIMARY RUN
```

## Research question

> What measurable operational work does Human perform for the current system that the system should be capable of supplying itself, without violating Human semantic authority?

## System under test

```text
CURRENT PROJECTOR / ECOSYSTEM AS-IS
```

## Forbidden before baseline

No new:

- router;
- drift detector;
- trajectory manager;
- navigation policy;
- agent/runtime;
- HOT-specific behavioral prompt teaching desired behavior;
- recovery mechanism;
- state-management mechanism;
- Projector v2 capability.

## Allowed

- passive logging;
- timestamps;
- evidence capture;
- immutable RAW event recording;
- separate evaluation after run.

## Primary distinction

```text
LEGITIMATE HUMAN INPUT
!=
HUMAN RESCUE
```

## Current execution state

```text
PRIMARY RUN: NOT STARTED
REAL PROJECT: NOT YET SELECTED
START RECORD: NOT YET FROZEN
RAW EVENT LOG: NOT YET CREATED
EVALUATION: PENDING
RECONCILIATION: PENDING
```

## Next

Select one real project, freeze its Start Record, then run current system AS-IS with passive observation only.
