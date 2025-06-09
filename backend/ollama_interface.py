# backend/ollama_interface.py

import subprocess

def query_deepseek(prompt: str) -> str:
    """
    Sends a prompt to the DeepSeek Coder model via Ollama CLI.
    
    Args:
        prompt (str): Natural language instruction
    
    Returns:
        str: LLM-generated response
    """
    try:
        process = subprocess.run(
            ['ollama', 'run', 'deepseek-coder'],
            input=prompt.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return process.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"[ERROR] Ollama failed: {e.stderr.decode('utf-8')}"

