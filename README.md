## Project structure

- `backend/` contains the CrewAI + FastAPI app
- `frontend/` contains the Vite React UI

## Backend setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
pip install python-multipart
```

Run from the repo root `C:\bot`:

```powershell
uvicorn backend.app.main:app --reload
```

Or, if you `cd backend` first, use:

```powershell
uvicorn app.main:app --reload
```

Swagger UI: `http://127.0.0.1:8000/docs`

## Frontend setup

```powershell
Set-Location frontend
npm install
npm run dev
```

## Optional pip upgrade

```powershell
python.exe -m pip install --upgrade pip
```
