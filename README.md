<!-- to start the env and install dependencies: -->
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install python-multipart

<!-- to run the app -->
uvicorn app.main:app --reload

<!-- swagger ui at  -->
http://127.0.0.1:8000/docs

<!-- to install new upgrade version of pip -->
python.exe -m pip install --upgrade pip