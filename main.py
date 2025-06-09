from backend.ollama_interface import query_deepseek
from backend.code_parser import parse_code_blocks
from backend.file_writer import save_files

if __name__ == "__main__":
    prompt = "Build a Flask app with a homepage and a template"
    raw_output = query_deepseek(prompt)

    print("\n=== RAW OUTPUT ===\n")
    print(raw_output)

    parsed_files = parse_code_blocks(raw_output)

    if not parsed_files:
        print("[⚠️] No files parsed from LLM output.")
    else:
        for fname, content in parsed_files:
            print(f"\n--- {fname} ---\n{content}\n")
