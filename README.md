# 📖 Story Alternator — Enterprise Book Reading & Plot Pivot Platform

An interactive enterprise e-book reading platform and agentic AI narrative alternator built with **React 19**, **React Flow**, **FastAPI**, **Gemini 2.5 Flash**, **Ollama**, and **SQLite**.

![Story Alternator Demo](./demo.gif)

---

## 🌟 Overview

The **Story Alternator** allows readers to explore classic literature (*Pride & Prejudice*, *The Great Gatsby*, *Frankenstein*) or upload their own custom `.txt` or `.epub` books. Readers can engage with an AI literary agent to branch story paths at critical narrative nodes, view interactive decision tree flowcharts, generate multi-paragraph alternate chapter pages in the authentic tone of the original author, view visual scene illustrations, and export altered books into downloadable e-book formats.

---

## 🚀 How to Run the App (Choose Your Stack)

You can run this project in two modes: **100% Standalone Freeware Mode** (no Google Cloud needed) or **Google Cloud Agent Engine Mode**.

---

### Option A: 100% Standalone Freeware Mode (No Google Cloud Required)

Run the full application locally using SQLite, React 19, and Ollama/Groq without any GCP credentials or cloud setup.

```bash
# 1. Clone the repository & enter directory
git clone https://github.com/RajeshHsejar27/story-alternator.git
cd story-alternator

# 2. Build the React Frontend
cd frontend-react
npm install
npm run build
cd ..

# 3. Launch the Standalone FastAPI Backend
cd backend-standalone
pip install -r requirements.txt
python main.py
```

Open **`http://localhost:8000`** in your browser to launch the full standalone application!

> **AI Engine Options for Standalone Mode**:
> - **Offline Fallback (Default)**: Runs automatically out-of-the-box without setup.
> - **Ollama (Zero-Cost Local LLM)**: Start Ollama (`ollama run llama3`) on `http://localhost:11434`.
> - **Groq API**: `export GROQ_API_KEY="your_groq_api_key"` before running `python main.py`.

---

### Option B: Google Cloud Agent Engine Mode (Production ADK)

Run with Google Cloud Platform integrations (Vertex AI Memory Bank, Firestore, Imagen 3, GCS).

```bash
# 1. Environment Configuration
export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
export GOOGLE_CLOUD_LOCATION="us-east1"

# 2. Install Root Dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r frontend/requirements.txt

# 3. Seed Firestore Database
python scripts/seed_firestore.py

# 4. Run Cloud Backend Proxy
cd frontend
python main.py
```

Open **`http://localhost:8080`** in your browser.

---

## 🎨 Modern Tech Stack Features

- **📖 Story Reader Parchment System**: High-contrast Light Mode reader UI with drop-cap typography, scene artwork banners, and dual **Book & Branch** toolbar selectors.
- **🕸️ Interactive Story Decision Tree Flowchart (`React Flow`)**: Interactive visual node graph (`@xyflow/react`) mapping canonical story trunks to alternate plot branches with clickable node selection.
- **💬 AI Narrative Copilot Chatbot**: Real-time story pivot scenario chips, chat message history, and direct *"Read Alternate Storyline Pages in Story Reader Tab"* action triggers.
- **📚 Enterprise Catalog & Custom E-Book Upload Modal**: Grid view for classic prebuilt books and modal for custom e-book additions.
- **📤 E-Book Exporter**: Generate and download styled `.epub` and `.html` alternate storybooks.

---

## 🛠️ Architecture & Tools

| Component | Freeware Standalone Stack | Google Cloud Stack |
| :--- | :--- | :--- |
| **Frontend UI** | React 19 + TypeScript + Vite | React 19 + TypeScript + Vite |
| **Visual Flowchart** | React Flow (`@xyflow/react`) | React Flow (`@xyflow/react`) |
| **AI Inference Engine**| Ollama (`llama3`) / Groq / Fallback | Gemini 2.5 Flash + ADK Agent |
| **Database** | SQLite (`story_database.sqlite`) | Google Cloud Firestore |
| **Memory Persistence** | SQLite Memory Store | Vertex AI Memory Bank |
| **Artwork Gen** | Pre-rendered / ComfyUI | Imagen 3 (`generate_scene_illustration`) |
| **E-Book Export** | Local HTML Exporter | GCS E-Book Exporter (`export_story_ebook`) |

---

## 📄 License & Usage

Created for interactive literature exploration and agentic story generation. Open source and customizable.
