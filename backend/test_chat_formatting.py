import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "frontend"))
from chat_formatting import format_chat_math


class ChatMathTests(unittest.TestCase):
    def test_display_and_inline_math_keep_latex_commands(self):
        content = r"变化率：\[\frac{d\ln K}{dT}=\frac{\Delta_r H^\circ}{RT^2}\]其中\(T\)为绝对温度。"
        result = format_chat_math(content)
        self.assertIn("\n\n$$\n" + r"\frac{d\ln K}{dT}=\frac{\Delta_r H^\circ}{RT^2}" + "\n$$\n\n", result)
        self.assertIn("其中$T$为绝对温度", result)
        self.assertNotIn("\f", result)
        self.assertEqual(format_chat_math(result), result)

    def test_code_examples_and_normal_markdown_are_not_rewritten(self):
        content = "```latex\n" + r"\[\frac{x}{y}\]" + "\n```\n" + r"`\(x\)` [教材](https://example.com) $K$"
        self.assertEqual(format_chat_math(content), content)


if __name__ == "__main__":
    unittest.main()
