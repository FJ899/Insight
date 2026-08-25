# HOT Start Record Schema v1.1

Status: candidate schema for future HOT runs. Does not alter v1.0 records.

```text
EXPERIMENT:
HOT-001

PROTOCOL:
1.1

RUN_ID:
PROJECT:
START_TIMESTAMP:
SYSTEM_UNDER_TEST:
CURRENT PROJECTOR / ECOSYSTEM AS-IS

INTERACTION_SHAPE:
SINGLE_TURN / MULTI_TURN / TOOL_DRIVEN / MIXED

START_STATE:
GOAL:
REAL_WORLD_DONE_CONDITION:
HUMAN_AUTHORITY_SCOPE:
ALLOWED_LEGITIMATE_HUMAN_INPUT:
STOP_CONDITION:
AVAILABLE_TOOLS:
KNOWN_EXTERNAL_CONSTRAINTS:
MODEL / VERSION IF KNOWN:
SOURCE / STATE IDENTITY IF RELEVANT:

MODEL_VISIBLE_TASK_BRIEF_PATH:
EVALUATOR_ONLY_DONE_CONTRACT:

TRANSCRIPT_CAPTURE_METHOD:
NATIVE_EXPORT:
YES / NO / UNKNOWN
BYTE_EXACT_TRANSCRIPT_CLAIM:
YES / NO

KNOWN_LIMITATIONS_AT_START:
NOTES:
```

## Freeze rules

- Freeze GOAL and real-world DONE before launch.
- Keep evaluator-only HOT criteria out of the model-visible task brief.
- Freeze interaction shape and transcript capture method before launch.
- If only copy/paste provenance is possible, set `BYTE_EXACT_TRANSCRIPT_CLAIM: NO`.
- Do not add product/navigation behavior after freezing the record.
- After launch, defects are recorded separately; this record is not silently repaired.
