# ARX-001 — Artifact Registry

This registry records known identities only. Missing values remain `UNKNOWN`; do not infer them.

## R1A-I

```text
ARTIFACT_ID: ARX-001-R1A-I-01_RAW
STATUS: ACCEPT / FROZEN
MODEL: GPT-5.6 Sol
DATE: 2026-08-25
WEB: OFF
SOURCE: READ-ONLY FROZEN LOCAL SNAPSHOT

SOURCE_MANIFEST_SHA256:
f7b31f866b8616d21acbc1c696974e57b0ce7a1759350141e88ad292c23fb1b4

SOURCE_BUNDLE_PORTABLE_SHA256:
62aef90a6bc5def8f39cb7586786d1f68806d9580762af55b411613e804506db

RAW_SHA256:
d65aaf2f11b5ea0731d25465310aa061dbc22e49f32d2a1df99793ed4c88344e

INTERNAL_RUN_ID: UNKNOWN
SOURCE_MANIFEST_ID: UNKNOWN
```

### Known source limitation

```text
ID: SL-001
ISSUE:
Executor GP001 referenced target SHA
3934a94a5eebf750079200589d6dc40e024d44a0
while supplied executor-pilot-target snapshot was
fc26df99f3896e15a09df2f1a627800f094903.

IMPACT:
Exact GP001 E2E target cannot be independently reproduced from R1A-I bundle.

ACTION IN v1.0:
NONE
```

## R1A-S

```text
ARTIFACT_ID: ARX-001-R1A-S-01_RAW
STATUS: ACCEPT / FROZEN
MODEL: GPT-5.6 Sol
DATE: 2026-08-25
WEB: OFF
SOURCE: READ-ONLY FROZEN LOCAL SNAPSHOT

SOURCE_MANIFEST_SHA256:
78207fd34027d0cb2e67a436dca707a02ba30c1321b8a08a704dc2b5320d6b04

SOURCE_BUNDLE_FINAL_SHA256:
d2f21636df4b8aad7a6f4937868a8eef08eb0b51947fae7dd33fed01fc6f67da

FROZEN_PROMPT_SHA256:
b1da332a467dee18dde0830434427e141703ff7ddb1755b32adc4212091ab3f7

RAW_SHA256: UNKNOWN
INTERNAL_RUN_ID: UNKNOWN
SOURCE_MANIFEST_ID: UNKNOWN
```

## Registry rules

- Frozen RAW content must not be edited to match later interpretation.
- This registry may add missing identities later only when independently recovered from evidence.
- Adding a recovered identifier does not authorize changing the underlying experiment result.
