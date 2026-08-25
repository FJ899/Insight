import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "tools" / "insight_check.py"
spec = importlib.util.spec_from_file_location("insight_check", MODULE_PATH)
insight_check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = insight_check
assert spec.loader is not None
spec.loader.exec_module(insight_check)


class InsightCheckTests(unittest.TestCase):
    def test_git_blob_sha_matches_known_git_hash(self):
        self.assertEqual(insight_check.git_blob_sha1(b"test content\n"), "d670460b4b4aece5915caf5c68d12f560a9fe3e4")

    def test_frozen_drift_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "control").mkdir()
            target = root / "frozen.txt"
            target.write_text("original\n", encoding="utf-8")
            manifest = {"version": 1, "artifacts": [{"path": "frozen.txt", "git_blob_sha1": insight_check.git_blob_sha1(target.read_bytes())}]}
            (root / "control/frozen_artifacts.json").write_text(json.dumps(manifest), encoding="utf-8")
            target.write_text("changed\n", encoding="utf-8")
            findings = list(insight_check.check_frozen_artifacts(root))
            self.assertTrue(any(f.code == "FROZEN_DRIFT" and f.severity == "ERROR" for f in findings))

    def test_open_limitations_are_warnings_but_must_be_surfaced(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "control").mkdir()
            (root / "STATUS.md").write_text("Known: LIM-001\n", encoding="utf-8")
            payload = {"version": 1, "limitations": [{"id": "LIM-001", "state": "OPEN", "summary": "known debt"}]}
            (root / "control/known_limitations.json").write_text(json.dumps(payload), encoding="utf-8")
            findings = list(insight_check.check_known_limitations(root))
            self.assertEqual([(f.severity, f.code) for f in findings], [("WARN", "LIM-001")])


if __name__ == "__main__":
    unittest.main()
