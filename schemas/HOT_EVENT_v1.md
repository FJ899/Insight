# HOT Event Schema v1

## RAW layer — freeze first

```text
EVENT_ID:
TIMESTAMP:

CURRENT_GOAL:
CURRENT_STATE:

AI_PROPOSED_NEXT_STEP:

HUMAN_INPUT_RAW:

STATE_BEFORE:
EVIDENCE_AVAILABLE_BEFORE:

STATE_AFTER:
```

Do not add interpretation to the RAW fields.

## Classification layer — after RAW freeze

```text
CLASS:
LEGITIMATE_HUMAN_INPUT / HUMAN_RESCUE / AMBIGUOUS

RESCUE_TYPE:
SEVERITY:
R0 / R1 / R2 / R3 / R4 / N/A / UNKNOWN

COUNTERFACTUAL:
COUNTERFACTUAL_IMPACT:

HUMAN_ATTENTION_COST:
ATTENTION_COST_CONFIDENCE:

REPEATED_RESCUE_CLASS:
YES / NO / UNKNOWN

RESCUE_DEPENDENCY:
LOW / MEDIUM / HIGH / UNKNOWN / N/A
```

## Outcome layer — later

```text
EVENTUAL_OUTCOME:
OUTCOME_EVIDENCE:
```

## Reconciliation rule

Later outcome may inform reconciliation, but must not silently rewrite the original RAW event or preregistered severity definition.
