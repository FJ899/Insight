# HOT-001 — Human Orchestration Tax Baseline

```text
PROTOCOL: 1.0
MODE: AS-IS / OBSERVATIONAL
STATUS: FROZEN BEFORE PRIMARY RUN
```

## 1. Research question

> What measurable operational work does Human perform for the current system that the system should be capable of supplying itself, without violating Human semantic authority?

This experiment does not test whether AI is generally autonomous.

It tests the separation:

```text
HUMAN SEMANTIC AUTHORITY
!=
HUMAN OPERATIONAL ORCHESTRATION
```

## 2. System under test

```text
CURRENT PROJECTOR / ECOSYSTEM AS-IS
```

During the Primary Run, no new product behavior may be introduced to improve the measured capability.

Forbidden additions:

- router;
- drift detector;
- trajectory manager;
- navigation policy;
- agent/runtime;
- special HOT prompt teaching the desired behavior;
- new recovery mechanism;
- new state-management mechanism.

Allowed additions:

- passive logging;
- evidence capture;
- timestamps;
- immutable event recording;
- separate evaluation after the run.

Instrumentation must not be visible to the tested model as behavioral instruction.

## 3. Legitimate Human Input

`LEGITIMATE_HUMAN_INPUT` is not counted against the product.

It includes:

- define/change GOAL;
- define/change DONE;
- preference;
- value judgement;
- priority decision;
- risk acceptance;
- canon decision;
- approval/rejection of consequential action;
- legal/identity/account action owned by Human;
- semantic acceptance of final result.

This is Human's proper authority, not orchestration tax.

## 4. Human Rescue

`HUMAN_RESCUE` occurs when Human supplies missing control/navigation work that the system should have supplied itself while preserving Human semantic authority.

Examples:

- identify the critical unknown;
- correct the next step;
- reroute the trajectory;
- select evidence/source the AI should have selected;
- restore forgotten current state;
- detect drift;
- prevent premature STOP;
- prevent false DONE;
- notice that more AI work is possible before a Human gate;
- invent a missing operational next step.

Core rule:

> Rescue concerns control of the process, not Human ownership of meaning.

If classification cannot be supported, use `AMBIGUOUS` / `UNKNOWN` rather than forcing a favorable interpretation.

## 5. Severity

Freeze before the run:

```text
R0 — convenience / cosmetic
No material effect on trajectory.

R1 — local correction
Improves local execution but does not materially change the path.

R2 — material next-step correction
Without intervention, the next material step would be wrong.

R3 — route / target correction
Human changes trajectory, target, or the method of reaching the goal.

R4 — critical rescue
Human prevents false DONE, premature terminal STOP, major drift,
loss of goal, material irreversible error, or a run converging on the wrong result.
```

Severity must not be rewritten after learning the final outcome merely because hindsight changes how important an event appears.

## 6. Rescue Dependency

Question:

> After a correction, can the system later perform this class of work itself, or does Human remain its permanent runtime?

```text
LOW
Correction generalizes; similar later situations are handled without Human.

MEDIUM
Partial retention / mixed behavior.

HIGH
The same rescue class repeatedly requires Human.

UNKNOWN
Insufficient later opportunities to evaluate.
```

Do not add Rule Retention or Transfer Retention to HOT-001 v1.0 after the run begins. Those belong to later protocols if needed.

## 7. RAW event discipline

Every Human intervention is first recorded without interpretation.

Minimum RAW fields are defined in `../../schemas/HOT_EVENT_v1.md`.

Sequence:

```text
RAW EVENT
   ↓ freeze
CLASSIFICATION
   ↓ freeze
LATER OUTCOME
   ↓
RECONCILIATION
```

The RAW layer must not be rewritten to fit the later classification or outcome.

## 8. Evaluator separation

```text
PRIMARY RUN
        ↓
IMMUTABLE EVENT LOG
        ↓
SEPARATE EVALUATION SESSION / EVALUATOR
        ↓
OUTCOME
        ↓
FINAL RECONCILIATION
```

Evaluator must not have conducted the Primary Run.

Where feasible, event classification should be frozen before the evaluator sees `EVENTUAL_OUTCOME`.

The evaluator uses the preregistered definitions in this protocol and does not create rescue criteria after seeing the result.

## 9. Start Record

Before each Primary Run, freeze:

- PROJECT;
- START STATE;
- GOAL;
- EXTERNAL DONE CONDITION;
- HUMAN AUTHORITY SCOPE;
- ALLOWED LEGITIMATE HUMAN INPUT;
- STOP CONDITION;
- AVAILABLE TOOLS;
- KNOWN EXTERNAL CONSTRAINTS.

Schema: `../../schemas/START_RECORD_v1.md`.

`EXTERNAL DONE` must be externally establishable. It is not equivalent to the system declaring that it is done.

## 10. Human Attention Cost

Use one measurement method for the entire Primary Run.

For v1.0:

```text
HUMAN ORCHESTRATION ATTENTION
= active Human time spent supplying operational/navigation work
  classified as HUMAN_RESCUE or handling the rescue event
```

Do not include time spent solely on `LEGITIMATE_HUMAN_INPUT` in the orchestration-tax total.

If exact timing is unavailable, record the best available estimate and mark its confidence rather than inventing precision.

## 11. HOT-001 result

The report returns at minimum:

```text
EXTERNAL DONE
PASS / FAIL / NOT REACHED / UNKNOWN

HUMAN RESCUE COUNT

SEVERITY PROFILE
R0:
R1:
R2:
R3:
R4:

TOTAL HUMAN ORCHESTRATION ATTENTION

RESCUE DEPENDENCY
LOW / MEDIUM / HIGH / UNKNOWN

LEGITIMATE HUMAN DECISIONS
reported separately

FALSE DONE EVENTS
PREMATURE STOP EVENTS
STATE RECOVERY RESCUES
EVIDENCE-SELECTION RESCUES
ROUTING RESCUES
```

HOT-001 v1.0 intentionally defines no arbitrary pass/fail threshold based on rescue count. The first run establishes baseline.

## 12. Interpretation constraints

HOT-001 alone cannot prove `PRODUCT = YES`.

Interpret patterns conservatively:

```text
GOOD OUTCOME + LOW ORCHESTRATION TAX
→ strong signal of system capability

GOOD OUTCOME + HIGH ORCHESTRATION TAX
→ capability should primarily be attributed to HUMAN + SYSTEM

POOR OUTCOME + LOW RESCUE
→ independence without effectiveness; not product success

POOR OUTCOME + HIGH RESCUE
→ strong falsification signal for current capability claim
```

## 13. What comes later

Only after HOT-001 baseline:

```text
HOT-001
AS-IS BASELINE
        ↓
identify measured Human work
        ↓
HOT-002
ONE MINIMAL INTERVENTION
        ↓
A/B
current vs validated reduced/support architecture
        ↓
TRANSFER
another Human
```

HOT-002 must implement the smallest mechanism responding to a measured rescue class, not a broad preconceived Projector architecture.

## 14. Freeze rule

After the first Primary Run begins, do not modify this v1.0 protocol to fit observed behavior.

If a material protocol defect is found:

1. preserve the v1.0 RAW and limitation;
2. record the defect;
3. create a later protocol version for a new series;
4. do not silently retrofit v1.0.

## 15. Separation from ARX-001

ARX-001 remains an independent frozen program.

HOT-001 evidence must not be added to ARX blind stages unless an already-frozen ARX protocol explicitly permits it.
