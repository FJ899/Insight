# Insight — Program Status

This file is the authoritative program-level current state for Insight.

## ARX-001

```text
R1A-I-01 RAW                  ACCEPT / FROZEN
R1A-S-01 RAW                  ACCEPT / FROZEN
CROSS-RUN DOCUMENTATION LIFT  NOT YET FORMALLY SCORED
R1A SUBSTITUTE PASS           BLOCKED / EXECUTABLE v1.0 ARTIFACT NOT RECOVERED
R1B FRAMEWORK LIFT            PENDING
R2 ADVERSARIAL DEMOLITION     PENDING
R3 RECONCILIATION             PENDING
ARCHITECTURE CHANGE           NOT AUTHORIZED
```

Local owner: `experiments/ARX-001/STATUS.md`

## HOT-001

```text
PROTOCOL                       1.0 frozen historical / 1.1 corrective candidate NOT FROZEN
MODE                           AS-IS / OBSERVATIONAL
BASELINE RUN                   HOT-001-BPM160-01 COMPLETE / RECONCILED
EXTERNAL DONE                  PASS
HUMAN RESCUES                  0 observed
HUMAN ORCHESTRATION ATTENTION  0 minutes observed
RESCUE DEPENDENCY              UNKNOWN
HUMAN SEMANTIC DECISION        SUNFOLD ACCEPT
HOT-002 INTERVENTION           NOT JUSTIFIED BY THIS RUN
PRODUCT CHANGE                 NOT AUTHORIZED
```

The BPM160 result is scoped to creative continuity / recovery-archive under the accessible pinned corpus. It does not justify claims about all workloads.

The run also carries open methodological limitations listed below. In particular, it must not be described as a clean measurement of unprompted orchestration behavior while `HOT-LIM-001` remains open.

Because no Human Rescue class was observed, no HOT-002 mechanism is selected from this run. The next useful baseline should use a materially different real workload class before broader product conclusions.

Local owner: `experiments/HOT-001/STATUS.md`

## Evidence health / open limitations

Machine-readable owner: `control/known_limitations.json`.

```text
HOT-LIM-001  OPEN  BPM160 primary prompt embedded a HOT-relevant orchestration condition inside DONE; AS-IS measurement is methodologically contaminated.
HOT-LIM-002  OPEN  BPM160 RAW came from Human copy/paste; native platform export and byte-exact transcript provenance are unavailable.
ARX-LIM-001  OPEN  ARX evidence is not self-contained in this repo; RAW artifacts are absent here and R1A-S RAW_SHA256 is UNKNOWN.
```

Open limitations constrain claims; they are not silently upgraded to PASS.

Frozen HOT-001 BPM160 artifacts are pinned by Git blob identity in `control/frozen_artifacts.json`. CI must fail if any pinned artifact drifts.

## Current program gate

```text
SELECT NEXT REAL AS-IS WORKLOAD
PREFERRED CLASS: OPERATIONAL DELIVERY or REVENUE / MARKET
OWNER: HUMAN SEMANTIC AUTHORITY
```

Before the next HOT run, use the v1.1 corrective candidate only after it is explicitly frozen for that new run. Do not retrofit v1.1 into BPM160 history.

## Program invariants

```text
PROPERTY != COMPONENT
CLAIM != EVIDENCE
RAW BEFORE INTERPRETATION
UNKNOWN IS A VALID RESULT
BASELINE BEFORE INTERVENTION
SUBSTITUTE BEFORE DELETION
HUMAN SEMANTIC AUTHORITY != HUMAN OPERATIONAL ORCHESTRATION
DECLARED FROZEN != MECHANICALLY IMMUTABLE
```

## Experiment separation

ARX-001 and HOT-001 are independent tracks.

HOT results must not be inserted into ARX blind stages unless an already-frozen ARX protocol explicitly allows them.

ARX results may motivate separate HOT hypotheses, but may not silently redefine HOT-001 after its freeze.
