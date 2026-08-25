# HOT Start Record Schema v1

Freeze this record before each HOT-001 Primary Run.

```text
EXPERIMENT:
HOT-001

PROTOCOL:
1.0

RUN_ID:

PROJECT:

START_TIMESTAMP:

SYSTEM_UNDER_TEST:
CURRENT PROJECTOR / ECOSYSTEM AS-IS

START_STATE:

GOAL:

EXTERNAL_DONE_CONDITION:

HUMAN_AUTHORITY_SCOPE:

ALLOWED_LEGITIMATE_HUMAN_INPUT:

STOP_CONDITION:

AVAILABLE_TOOLS:

KNOWN_EXTERNAL_CONSTRAINTS:

MODEL / VERSION IF KNOWN:

SOURCE / STATE IDENTITY IF RELEVANT:

NOTES:
```

## Freeze rules

- `GOAL` and `EXTERNAL_DONE_CONDITION` must be explicit before the run.
- `EXTERNAL_DONE_CONDITION` must be externally establishable and must not depend only on the system saying it is done.
- If Human legitimately changes GOAL, DONE, priority, or another semantic decision during the run, record that as a new legitimate Human input event rather than silently rewriting this Start Record.
- Do not add new product/navigation behavior after freezing the Start Record.
