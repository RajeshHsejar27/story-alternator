# 📖 Story Alternator — Enterprise Book Reading & Plot Pivot Platform

An interactive enterprise e-book reading platform and agentic AI narrative alternator built with Google ADK (Agent Development Kit), Gemini 2.5 Flash, Vertex AI Memory Bank, Firestore, Google Cloud Storage, and A2UI.

![Story Alternator Demo](./demo.gif)

---

## 🌟 Overview

The **Story Alternator** allows readers to explore classic literature (*Pride & Prejudice*, *The Great Gatsby*, *Frankenstein*) or upload their own custom `.txt` or `.epub` books. Readers can engage with an AI literary agent to branch story paths at critical narrative nodes, generate multi-paragraph alternate chapter pages in the authentic tone of the original author, view visual scene illustrations, and export altered books into downloadable e-book formats.

---

## 🛠️ Implemented Architecture & Google Cloud Integration

Based on the codebase in `app/` and `agents-cli-manifest.yaml`, the following services and tools are fully implemented:

### 1. 🧠 Vertex AI Memory Bank
- **Session Memory Persistence**: Automatically commits conversation sessions into Vertex AI Memory Bank via an `after_agent_callback` (`generate_memories_callback`).
- **Contextual Recall**: Integrates `preload_memory` tool to retrieve past user decisions, plot preferences, and reading history across sessions.

### 2. 🗄️ Google Cloud Firestore
- **Story Branch Storage**: Implements `save_story_branch` and `get_story_branches` tools to persist alternate story branches, chapter titles, text bodies, and scene illustration metadata.

### 3. ☁️ Google Cloud Storage (GCS)
- **Public Media & E-Book Hosting**: Serves generated visual scene artwork and compiled e-book HTML files from a public GCS bucket (`story-alternator-media-qwiklabs-gcp-02-f255a355adec`).

### 4. 🎨 Imagen 3 Scene Illustration Generator
- **Visual Artwork Tool**: Implements `generate_scene_illustration` tool to automatically create visual scene artwork for pivotal narrative moments.

### 5. 📚 Project Gutenberg Public Book Search
- **Catalog Search Tool**: Implements `search_public_books` tool to search public domain books from the Project Gutenberg library catalog.

### 6. 📄 Custom E-Book Upload & Parser
- **File Parser Tool**: Implements `analyze_uploaded_book` tool and FastAPI `/upload` endpoint to parse user-uploaded `.txt` and `.epub` files into custom story branches.

### 7. 📤 E-Book Document Exporter
- **Export Tool**: Implements `export_story_ebook` tool to compile alternate story branches into styled e-book documents with download links.

### 8. 🖼️ A2UI Server-Driven UI (v0.8)
- **Interactive UI Cards**: Integrates `A2uiSchemaManager(version="0.8")` and `a2ui_callback` to format agent tools and recommendations into server-driven UI components.

---

## 📋 Planned Capabilities (Not Yet Implemented)

- **Speech Synthesis / Audiobooks**: Text-to-speech audio narration generation for alternate chapter pages (planned, not yet implemented).
- **Multi-Player Collaborative Branching**: Shared real-time branch editing among multiple readers (planned, not yet implemented).

---

## 🚀 Setup & Local Execution Guide

### Prerequisites
- Python 3.10+
- Google Cloud SDK (`gcloud`)
- Google Cloud Project with Firestore, Vertex AI, and Cloud Storage APIs enabled.

### 1. Environment Setup

Clone the repository and install dependencies:

```bash
# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install root dependencies
pip install -r requirements.txt

# Install frontend dependencies
pip install -r frontend/requirements.txt
```

### 2. Environment Variables

Create an environment configuration file:

```bash
export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
export GOOGLE_CLOUD_LOCATION="us-east1"
```

### 3. Seed Firestore Database

Seed initial classic story branches:

```bash
python scripts/seed_firestore.py
```

### 4. Run Locally

Start the FastAPI application server:

```bash
cd frontend
uvicorn main:app --host 0.0.0.0 --port 8080
```

Open your browser to the local server address shown in the terminal output to launch the Enterprise Story Reader platform.

---

## 📄 Project Structure

```
story-alternator/
├── app/
│   ├── agent.py                 # Root ADK Agent & system prompt configuration
│   ├── a2ui_utils.py            # A2UI callback transformer
│   └── tools/
│       ├── firestore_tools.py   # Firestore read/write branch tools
│       ├── image_tool.py       # Imagen 3 scene illustration tool
│       ├── export_tool.py      # E-Book export tool
│       ├── upload_tool.py      # E-Book upload parser tool
│       └── public_book_tool.py # Gutenberg search tool
├── frontend/
│   ├── main.py                  # FastAPI server & /chat, /upload endpoints
│   ├── requirements.txt         # Frontend service dependencies
│   └── static/
│       └── index.html           # Enterprise Light Mode 3-Tab UI
├── agents-cli-manifest.yaml     # Agent deployment manifest
├── pyproject.toml               # Project packaging configuration
├── demo.gif                     # Looping demo recording GIF
└── README.md                    # Project documentation
```
