from fastapi import FastAPI, UploadFile, File
import os
import json

from app.parser import extract_text
from app.crew_runner import run_agents

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/generate-testcases/")
async def generate_testcases(file: UploadFile = File(...)):

    # Save file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text
    frs_text = extract_text(file_path)

    # Run AI
    result = run_agents(frs_text)

    # Convert to JSON
    try:
        parsed = json.loads(result)
    except:
        parsed = {"raw_output": result}

    # Save to TXT
    output_path = os.path.join(OUTPUT_DIR, "test_cases.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2)

    return {
        "message": "Success",
        "file": output_path,
        "count": len(parsed) if isinstance(parsed, list) else 0
    }

    