# 🚀 Standalone Non-GCP Story Alternator Backend

A 100% self-contained Python FastAPI backend that runs **completely offline / locally without any Google Cloud dependencies** (No GCP credentials, no Firestore, no Vertex AI required).

---

## 🛠️ Features

- **Database**: Zero-config local **SQLite** database (`story_database.sqlite`) for storing books, branches, and memories.
- **AI Engine**: Pluggable inference layer supporting:
  - **Ollama** (`llama3`) for zero-cost local LLM inference.
  - **Groq API** (`GROQ_API_KEY`) for ultra-fast cloud inference.
  - **Smart Rule Fallback Engine** for running offline without any API keys or installed LLMs.
- **E-Book Exporter**: Generates downloadable HTML/EPUB formatted alternate storybooks.
- **Frontend Serving**: Automatically mounts and serves the compiled React application from `frontend-react/dist`.

---

## 🚀 Quick Start Guide

### 1. Install Dependencies

```bash
cd backend-standalone
pip install -r requirements.txt
```

### 2. (Optional) Configure Local AI / Groq API

- **For Local Ollama**: Start Ollama (`ollama run llama3`) on `http://localhost:11434`.
- **For Groq API**: `export GROQ_API_KEY="your-groq-api-key"`
- **For Standalone Offline Mode**: No configuration needed!

### 3. Run the Backend Server

```bash
python main.py
```

The server will launch at **`http://localhost:8000`**.

---

## 🔌 API Endpoints Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/books` | `GET` | List all classic & uploaded books with branches |
| `/api/chat` | `POST` | Pivot story branch using AI inference & save to SQLite |
| `/api/upload` | `POST` | Upload custom `.txt` or `.epub` file into SQLite catalog |
| `/api/export/{book_id}/{branch_id}` | `GET` | Download alternate chapter as styled e-book |
