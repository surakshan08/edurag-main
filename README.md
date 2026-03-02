# EduRAG - Setup & Run Instructions

This guide walks you through setting up and running the EduRAG application from scratch on a Windows system using VS Code.

---

## Prerequisites

### 1. Install Python (3.10 or higher)

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"**
3. Verify installation:
   ```powershell
   python --version
   ```

### 2. Install Node.js (18.x or higher)

1. Download Node.js LTS from [nodejs.org](https://nodejs.org/)
2. Run the installer (includes npm)
3. Verify installation:
   ```powershell
   node --version
   npm --version
   ```

### 3. Install VS Code

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install recommended extensions:
   - **Python** (by Microsoft)
   - **Pylance** (by Microsoft)
   - **ES7+ React/Redux/React-Native snippets**
   - **Tailwind CSS IntelliSense**

### 4. Install Git (Optional but recommended)

1. Download from [git-scm.com](https://git-scm.com/downloads)

---

## Project Setup

### Step 1: Open the Project in VS Code

1. Open VS Code
2. Go to **File > Open Folder**
3. Select the `rag` folder

---

## Backend Setup

### Step 2: Create a Python Virtual Environment

Open a new terminal in VS Code (`Ctrl + `` ` or **Terminal > New Terminal**):

```powershell
cd backend
python -m venv venv
```

### Step 3: Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate
```

You should see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install Backend Dependencies

```powershell
pip install -r requirements.txt
```

> **Note:** This will download machine learning models (~500MB+). First run may take several minutes depending on your internet speed.

### Step 5: Run the Backend Server

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process
```

> **First startup:** The server will download AI models (sentence-transformers & Flan-T5) on first run. This may take 5-10 minutes.

Leave this terminal running and open a **new terminal** for the frontend.

---

## Frontend Setup

### Step 6: Navigate to Frontend Directory

In a **new terminal**:

```powershell
cd frontend
```

### Step 7: Install Frontend Dependencies

```powershell
npm install
```

### Step 8: Run the Frontend Development Server

```powershell
npm run dev
```

You should see:
```
  VITE v7.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

---

## Access the Application

1. Open your browser
2. Navigate to **http://localhost:5173**
3. You should see the EduRAG chat interface
4. Try asking questions like:
   - "What courses are offered in AI?"
   - "Tell me about the college facilities"
   - "What are the admission requirements?"

---

## Quick Start Commands Summary

| Terminal 1 (Backend)                          | Terminal 2 (Frontend)      |
|-----------------------------------------------|----------------------------|
| `cd backend`                                  | `cd frontend`              |
| `python -m venv venv`                         | `npm install`              |
| `.\venv\Scripts\Activate`                     | `npm run dev`              |
| `pip install -r requirements.txt`             |                            |
| `uvicorn app.main:app --reload --port 8000`   |                            |

---

## Troubleshooting

### "python" is not recognized
- Reinstall Python and ensure "Add Python to PATH" is checked
- Or use `python3` instead of `python`

### "npm" is not recognized
- Reinstall Node.js
- Restart VS Code after installation

### Backend fails with CUDA/torch errors
- The project uses `faiss-cpu` and CPU-based inference
- GPU is not required; ensure you have `faiss-cpu` (not `faiss-gpu`)

### Port already in use
- Backend: Change port with `--port 8001`
- Frontend: Vite will auto-assign the next available port (5174, 5175, etc.)

### CORS errors in browser console
- Ensure backend is running on `http://127.0.0.1:8000`
- The frontend expects the API at this address

### Models download fails
- Check your internet connection
- Models are downloaded from Hugging Face; ensure it's not blocked

### Virtual environment not activating (PowerShell)
Run this command first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## API Endpoints

| Method | Endpoint | Description            |
|--------|----------|------------------------|
| POST   | `/chat`  | Send a chat query      |

### Example Request

```json
POST http://127.0.0.1:8000/chat
Content-Type: application/json

{
  "query": "What courses are offered in AI?"
}
```

---

## Project Structure

```
rag/
├── backend/                 # FastAPI backend
│   ├── app/                 # API routes and schemas
│   ├── rag/                 # RAG pipeline (chunker, vector store, generator)
│   ├── bootstrap.py         # Chatbot initialization
│   ├── main.py              # CLI entry point
│   └── requirements.txt     # Python dependencies
│
├── frontend/                # React + Vite frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   └── services/        # API service layer
│   └── package.json         # Node dependencies
│
└── instructions.md          # This file
```

---

## Stopping the Servers

- Press `Ctrl + C` in each terminal to stop the servers
- To deactivate the Python virtual environment: `deactivate`

---

## Next Steps

- Modify `backend/rag/data_manager.py` to add your own knowledge base
- Customize the UI in `frontend/src/components/`
- Deploy using Docker or cloud services
