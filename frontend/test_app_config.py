"""Chat route checks with fake secrets and mocked network calls."""
import json
import os
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests
from streamlit.testing.v1 import AppTest


class ChatConfigTests(unittest.TestCase):
    def app(self, secrets=None):
        app = AppTest.from_file(str(Path(__file__).with_name("app.py")), default_timeout=20)
        if secrets:
            app.secrets.update(secrets)
        app.run().sidebar.radio(key="module").set_value("query").run()
        return app

    def submit(self, app):
        app.text_area[0].set_value("What does Q mean?")
        next(button for button in app.button if button.label == "Send").click().run()
        self.assertFalse(app.exception)
        return app.session_state["query_messages"][-1]["content"]

    @patch.dict(os.environ, {"API_BASE_URL": "", "LLM_API_KEY": ""})
    @patch("requests.post")
    @patch("requests.get")
    def test_missing_settings_never_request_localhost(self, get, post):
        reply = self.submit(self.app())
        get.assert_not_called()
        post.assert_not_called()
        self.assertIn("No LLM_API_KEY or API_BASE_URL", reply)

    @patch.dict(os.environ, {"API_BASE_URL": "", "LLM_API_KEY": ""})
    @patch("requests.post", side_effect=requests.ConnectionError("PRIVATE_INTERNAL_DETAILS"))
    @patch("requests.get", side_effect=requests.ConnectionError())
    def test_explicit_local_backend_failure_explains_cloud_localhost(self, get, post):
        reply = self.submit(self.app({"API_BASE_URL": "http://localhost:8000"}))
        self.assertIn("localhost refers to the cloud server", reply)
        self.assertNotIn("PRIVATE_INTERNAL_DETAILS", reply)
        self.assertEqual(post.call_args.args[0], "http://localhost:8000/chat")

    @patch.dict(os.environ, {"API_BASE_URL": "", "LLM_API_KEY": ""})
    @patch("requests.post")
    @patch("requests.get")
    def test_configured_deepseek_key_uses_direct_route_without_backend(self, get, post):
        post.return_value = Mock(json=lambda: {"choices": [{"message": {
            "content": json.dumps({"decision": "clarify"})}}]})
        reply = self.submit(self.app({"LLM_API_KEY": "offline-test-key",
                                     "LLM_BASE_URL": "https://api.deepseek.com",
                                     "LLM_MODEL": "deepseek-v4-flash"}))
        get.assert_not_called()
        self.assertEqual(post.call_count, 1)
        self.assertEqual(post.call_args.args[0], "https://api.deepseek.com/chat/completions")
        self.assertIn("specific question", reply)


if __name__ == "__main__":
    unittest.main()
