"""Regression checks for deployment updates in a long-lived Streamlit process."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "frontend"))
import tutor_client


class TutorClientTests(unittest.TestCase):
    def tearDown(self):
        tutor_client._load_source.cache_clear()

    def call(self):
        return tutor_client.ask_tutor("问题", [], "query", {}, "test-key",
                                     "https://example.com", "test-model",
                                     learning_context={"content": "Q<K"}, language="zh")

    @patch("requests.post")
    def test_stale_global_tutor_is_ignored_and_scope_gate_still_runs(self, post):
        old = ModuleType("tutor")
        old.ask_tutor = Mock(side_effect=TypeError("Unexpected learning_context"))
        post.return_value = Mock(json=lambda: {"choices": [{"message": {
            "content": json.dumps({"decision": "off_topic"})}}]})
        with patch.dict(sys.modules, {"tutor": old}):
            result = self.call()
        old.ask_tutor.assert_not_called()
        self.assertEqual(result["scope_status"], "off_topic")
        self.assertEqual(post.call_count, 1)

    def test_changed_source_is_loaded_even_with_same_size_and_timestamp(self):
        source = "HARNESS_API_VERSION = 2\ndef ask_tutor(*args, **kwargs):\n    return {'reply': 'VERSION_A'}\n"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tutor.py"
            path.write_text(source, encoding="utf-8")
            stat = path.stat()
            with patch.object(tutor_client, "TUTOR_PATH", path):
                self.assertEqual(self.call()["reply"], "VERSION_A")
                path.write_text(source.replace("VERSION_A", "VERSION_B"), encoding="utf-8")
                os.utime(path, ns=(stat.st_atime_ns, stat.st_mtime_ns))
                self.assertEqual(self.call()["reply"], "VERSION_B")

    def test_old_interface_returns_safe_error_without_calling_it(self):
        sources = [
            "def ask_tutor(*args, **kwargs):\n    raise AssertionError('must not run')\n",
            "HARNESS_API_VERSION = 2\ndef ask_tutor(prompt):\n    raise AssertionError('must not run')\n",
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tutor.py"
            for source in sources:
                path.write_text(source, encoding="utf-8")
                with patch.object(tutor_client, "TUTOR_PATH", path):
                    result = self.call()
                self.assertTrue(result["error"])
                self.assertIn("重启", result["reply"])
                self.assertNotIn("must not run", result["reply"])

    def test_invocation_error_does_not_crash_or_leak_provider_data(self):
        source = "HARNESS_API_VERSION = 2\ndef ask_tutor(*args, **kwargs):\n    raise TypeError('SENSITIVE_PROVIDER_DETAIL')\n"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tutor.py"
            path.write_text(source, encoding="utf-8")
            with patch.object(tutor_client, "TUTOR_PATH", path):
                result = self.call()
            self.assertTrue(result["error"])
            self.assertNotIn("SENSITIVE_PROVIDER_DETAIL", result["reply"])


if __name__ == "__main__":
    unittest.main()
