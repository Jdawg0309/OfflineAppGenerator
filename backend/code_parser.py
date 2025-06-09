import re
from typing import List, Tuple

def parse_code_blocks(text: str) -> List[Tuple[str, str]]:
    """
    Attempts to parse named code blocks. Falls back to single block if needed.
    Returns a list of (filename, code) tuples.
    """
    # Try structured format: # filename\n```<lang>\n<code>\n```
    pattern = re.compile(r"#\s*(.+\.(py|html|js|css))\n+```(?:\w+)?\n(.*?)```", re.DOTALL)
    matches = pattern.findall(text)

    if matches:
        return [(filename.strip(), code.strip()) for filename, _, code in matches]

    # Fallback: look for a single code block even if no filename
    code_fallback = re.search(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)
    if code_fallback:
        return [("main.py", code_fallback.group(1).strip())]

    # Last resort: return everything if there's no markdown formatting at all
    if "from flask" in text:
        return [("main.py", extract_likely_code(text))]

    return []  # Nothing usable

def extract_likely_code(text: str) -> str:
    """
    Naive extraction: returns the longest 'from ...' to 'app.run' block as a guess.
    """
    lines = text.splitlines()
    code_lines = []
    record = False
    for line in lines:
        if "from flask" in line:
            record = True
        if record:
            code_lines.append(line)
        if "app.run" in line:
            break
    return "\n".join(code_lines).strip()
