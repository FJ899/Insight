# Insight — Program Status

This file is the authoritative program-level current state for Insight.

## ARX-001

```text
R1A-I-01 RAW                  ACCEPT / FROZEN
R1A-S-01 RAW                  ACCEPT / FROZEN
CROSS-RUN DOCUMENTATION LIFT  NOT YET FORMALLY SCORED
R1A SUBSTITUTE PASS           NEXT / EXECUTABLE v1.0 ARTIFACT NOT RECOVERED
R1B FRAMEWORK LIFT            PENDING
R2 ADVERSARIAL DEMOLITION     PENDING
R3 RECONCILIATION             PENDING
ARCHITECTURE CHANGE           NOT AUTHORIZED
```

Local owner: `experiments/ARX-001/STATUS.md`

## HOT-001

```text
PROTOCOL                       1.0
MODE                           AS-IS / OBSERVATIONAL
STATUS                         FROZEN BEFORE PRIMARY RUN
PRIMARY RUN                    NOT STARTED
PRODUCT CHANGE BEFORE BASELINE FORBIDDEN
INSTRUMENTATION                PASSIVE ONLY
```

Research question:

> What measurable operational work does Human perform for the current system that the system should be capable of supplying itself, without violating Human semantic authority?

Local owner: `experiments/HOT-001/STATUS.md`

## Program invariants

```text
PROPERTY != COMPONENT
CLAIM != EVIDENCE
RAW BEFORE INTERPRETATION
UNKNOWN IS A VALID RESULT
BASELINE BEFORE INTERVENTION
SUBSTITUTE BEFORE DELETION
HUMAN SEMANTIC AUTHORITY != HUMAN OPERATIONAL ORCHESTRATION
```

## Experiment separation

ARX-001 and HOT-001 are independent tracks.

HOT results must not be inserted into ARX blind stages unless an already-frozen ARX protocol explicitly allows them.

ARX results may motivate separate HOT hypotheses, but may not silently redefine HOT-001 after its freeze.
