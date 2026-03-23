from PyPDF2 import PdfReader
import pandas as pd


def extract_text(file_path):

    # PDF
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"

        return text.strip()

    # TXT
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    # Excel
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        return df.to_string(index=False)

    return ""