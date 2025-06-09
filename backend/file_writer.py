import os
from typing import List, Tuple

def save_files(file_tuples: List[Tuple[str, str]], base_dir: str = "generated_apps/session_1"):
    """
    Saves each (filename, content) pair into the specified directory structure.

    Args:
        file_tuples (List[Tuple[str, str]]): List of (filename, code) tuples.
        base_dir (str): Base directory to write files to.
    """
    for relative_path, content in file_tuples:
        full_path = os.path.join(base_dir, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"[✅] Saved: {full_path}")
