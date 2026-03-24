from fastapi import FastAPI, UploadFile, File
import json
import os

from app.parser import extract_text
from app.crew_runner import run_agents

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


def _result_to_text(result) -> str:
    if hasattr(result, "raw") and result.raw:
        return result.raw
    return str(result)


def _count_test_cases(output_text: str) -> int:
    try:
        parsed = json.loads(output_text)
    except json.JSONDecodeError:
        return 1

    return len(parsed) if isinstance(parsed, list) else 1


@app.post("/generate-testcases/")
async def generate_testcases(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    frs_text = extract_text(file_path)
    result = run_agents(frs_text)

    output_text = _result_to_text(result)
    output_path = os.path.join(OUTPUT_DIR, "test_cases.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_text)

    return {
        "message": "Success",
        "file": output_path,
        "count": _count_test_cases(output_text),
        "output_preview": output_text[:500]
    }
