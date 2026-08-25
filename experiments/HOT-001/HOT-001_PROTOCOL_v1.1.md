# HOT-001 — Human Orchestration Tax Baseline v1.1

```text
PROTOCOL: 1.1
STATUS: NOT FROZEN / CANDIDATE
PURPOSE: corrective protocol for future runs only
```

This document does not rewrite or repair HOT-001 v1.0. It exists because the BPM160 run exposed protocol-design debt that must be corrected before the next baseline.

## 1. Preserve the original research question

Measure operational Human work required by the current system while preserving legitimate Human semantic authority.

The system under test remains AS-IS. No new router, agent/runtime, recovery mechanism, navigation policy, or HOT-specific behavior may be introduced to improve a baseline.

## 2. PRIMARY PROMPT HYGIENE

The studied model's primary prompt must not contain HOT methodology, rescue taxonomy, orchestration-tax language, evaluator expectations, or instructions whose purpose is to produce a favorable HOT measurement.

In particular, evaluator-only conditions such as "Human performs only semantic acceptance" must not be placed inside the model-visible task prompt. Those belong in the frozen evaluation contract.

The model-visible prompt may contain only information needed to perform the real task safely and correctly: task meaning, source identity, actual user constraints, and real-world completion requirements.

Before launch, record separately:

```text
MODEL_VISIBLE_TASK_BRIEF
EVALUATOR_ONLY_DONE_CONTRACT
```

If the same sentence is required only to score orchestration behavior rather than to perform the real task, it belongs in the evaluator-only contract.

## 3. Interaction-shape declaration

Before a run, freeze the intended interaction shape:

```text
SINGLE_TURN
MULTI_TURN
TOOL_DRIVEN
MIXED
```

A single-turn run can establish that no rescue was observed in that turn. It cannot establish retention, recovery behavior across turns, or low rescue dependency without later opportunities.

## 4. Transcript provenance

Prefer a native platform export or another directly captured transcript artifact whenever available.

If only Human copy/paste is available, record:

```text
NATIVE EXPORT: NO
BYTE-EXACT CLAIM: NO
TRANSCRIPT PROVENANCE: HUMAN PASTE
```

Do not upgrade confidence merely because the pasted content appears complete.

## 5. Evaluator separation

The evaluator must not conduct the primary run. Evaluation criteria must be frozen before the evaluator sees the eventual outcome where feasible.

Model-visible instructions and evaluator-only scoring criteria must remain separate artifacts.

## 6. Frozen artifact integrity

Every frozen protocol, start record, primary prompt, RAW transcript, evaluation, Human decision, and final reconciliation must be pinned in `control/frozen_artifacts.json` by Git blob identity.

A changed frozen artifact is a hard integrity failure. Correct by adding a new version or a separate defect record, never by silently editing history.

## 7. Known limitations

Material evidence or methodology defects must be registered in `control/known_limitations.json` and surfaced in root `STATUS.md` while open.

An open limitation does not automatically invalidate all evidence. It does prevent stronger claims than the remaining evidence supports.

## 8. Promotion gate

This v1.1 candidate may be frozen for a new run only after:

- model-visible task brief is reviewed for methodology leakage;
- evaluator-only DONE contract is separate;
- interaction shape is explicit;
- transcript capture method is explicit;
- frozen-artifact manifest is ready before launch;
- the real workload is selected by Human semantic authority.

Do not reuse BPM160 as proof that these safeguards already existed. They did not.
