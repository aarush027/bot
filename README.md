-----------------------------
GENERAL PREREQUISITES CHECK
-----------------------------

python --version
pip --version


===================================================
BACKEND SETUP (FastAPI)
===================================================

1. Navigate to backend directory
cd backend

2. Create Python virtual environment
python -m venv .venv

3. Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

5. Upgrade pip (recommended)
python.exe -m pip install --upgrade pip


6. Install backend dependencies
pip install -r requirements.txt
pip install python-multipart


7. Start FastAPI backend server
uvicorn app.main:app --reload


8. Backend URLs

Base URL:
http://127.0.0.1:8000

Swagger API Docs:
http://127.0.0.1:8000/docs

===================================================
FRONTEND SETUP (react)
===================================================

1. Navigate to frontend directory
cd frontend


2. Install frontend dependencies
npm install


3. Start frontend development server
npm run dev


4. Frontend URL (default)
http://localhost:3000


===================================================
RUNNING FULL APPLICATION
===================================================

Terminal 1 (Backend):

cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload


Terminal 2 (Frontend):

cd frontend
npm run dev


===================================================
COMMON TROUBLESHOOTING COMMANDS
===================================================

Upgrade pip, setuptools, and wheel

pip install --upgrade pip setuptools wheel

Run backend on a different port if 8000 is busy
uvicorn app.main:app --reload --port 8001

