"""Normalize model math delimiters to Streamlit Markdown without changing math."""
import re


def format_chat_math(content):
    # Keep code examples literal. Never unicode-decode text: that would turn
    # LaTeX commands such as \frac and \theta into control characters.
    parts = re.split(r"(```[\s\S]*?```|~~~[\s\S]*?~~~|`[^`\n]*`)", content)
    for index in range(0, len(parts), 2):
        text = re.sub(r"\\\[(.*?)\\\]", lambda m: "\n\n$$\n" + m[1].strip() + "\n$$\n\n",
                      parts[index], flags=re.DOTALL)
        text = re.sub(r"\\\((.*?)\\\)", lambda m: "$" + m[1].strip() + "$", text, flags=re.DOTALL)
        parts[index] = text
    return "".join(parts)
