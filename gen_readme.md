# 🛠️ Story Alternator — Generalized Tech Stack & Freeware Ecosystem Blueprint

This document presents a comprehensive guide to alternative **open-source, self-hosted, and free-tier tech stacks** for building, customizing, and hosting the **Story Alternator** platform across different technology ecosystems.

Whether you want a **100% offline local machine setup**, a **cloud-native zero-cost free-tier deployment**, or a **custom self-hosted serverless stack**, this blueprint outlines modular alternatives for every component of the system.

---

## 🏛️ System Architecture Components

The Story Alternator platform consists of 7 core functional layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        1. Frontend & Reader UI                         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                    2. Backend Server & API Gateway                     │
└─────┬─────────────────────────────┬──────────────────────────────┬─────┘
      │                             │                              │
┌─────▼───────────────┐   ┌─────────▼─────────────┐   ┌────────────▼─────┐
│ 3. Agent & LLM Engine│   │ 4. Database & State   │   │ 5. Memory & RAG  │
└─────┬───────────────┘   └───────────────────────┘   └──────────────────┘
      │
┌─────▼───────────────┐   ┌───────────────────────┐
│ 6. Image Generation │   │ 7. Storage & Export   │
└─────────────────────┘   └───────────────────────┘
```

---

## 🧩 Modular Component & Tech Stack Options

### 1. 🤖 Agent & LLM Engine (Narrative Rewriting & Pivots)

| Option | Technology | Cost / License | Description & Use Case |
| :--- | :--- | :--- | :--- |
| **Option A (Local)** | **Ollama** + Llama 3.3 / DeepSeek-R1 / Mistral NeMo | 100% Free (MIT/Apache) | Run LLMs locally on CPU/GPU without cloud costs or API limits. Ideal for privacy and offline usage. |
| **Option B (Free API)** | **Groq API** + Llama 3.3 70B / Mixtral | Free Tier (High RPS) | Ultra-fast inference with free API tier credits. Extremely responsive story generation. |
| **Option C (Free API)** | **Hugging Face Inference API** + Qwen 2.5 / DeepSeek | Free Tier | Access open weights models directly via standard REST API endpoints. |
| **Option D (Framework)** | **LangChain** / **LlamaIndex** / **CrewAI** | Open Source | Standard Python/TypeScript framework alternatives to ADK for multi-tool agent orchestration. |

---

### 2. 🗄️ Database & Branch State Management

| Option | Technology | Cost / License | Description & Use Case |
| :--- | :--- | :--- | :--- |
| **Option A (Cloud NoSQL)** | **Supabase** (PostgreSQL + JSONB) | Free Tier (500MB) | Built-in Auth, Realtime WebSocket updates, REST API, and PostgreSQL JSON document capabilities. |
| **Option B (Self-Hosted)** | **MongoDB Community Edition** | Free / AGPLv3 | Native NoSQL document storage for complex story branch trees and user reading histories. |
| **Option C (Embedded Local)**| **SQLite** + **SQLAlchemy** | 100% Free (Public Domain) | Zero-configuration single-file database. Ideal for standalone desktop or local server apps. |
| **Option D (Key-Value)** | **Redis** / **Valkey** | Free (BSD / Open Source) | In-memory key-value cache for lightning-fast session state management. |

---

### 3. 🧠 Memory Bank & Vector RAG Storage

| Option | Technology | Cost / License | Description & Use Case |
| :--- | :--- | :--- | :--- |
| **Option A (Self-Hosted)** | **Qdrant Community Edition** | Open Source (Apache 2.0) | High-performance vector database with filtering. Perfect for indexing e-book chapters and memories. |
| **Option B (Embedded Vector)**| **ChromaDB** / **LanceDB** | 100% Free (Apache 2.0) | Embedded vector store that runs in-process inside your Python app without external servers. |
| **Option C (Postgres Vector)**| **pgvector** (PostgreSQL Extension) | Open Source (PostgreSQL) | Native vector embeddings column inside standard Postgres (works natively in Supabase). |
| **Option D (Local Index)** | **FAISS** (Facebook AI Similarity Search) | Open Source (MIT) | Efficient similarity search library for dense vector recall. |

---

### 4. 🎨 Image Generation (Scene Artwork)

| Option | Technology | Cost / License | Description & Use Case |
| :--- | :--- | :--- | :--- |
| **Option A (Local Diffusion)**| **ComfyUI** / **Fooocus** + SDXL / FLUX.1 Schnell | 100% Free (Open Source) | Generate unlimited high-resolution scene artwork locally on NVIDIA/AMD/Apple Silicon GPUs. |
| **Option B (Free API)** | **Pollinations.ai API** | 100% Free (No API Key) | Instant, keyless image generation API using FLUX and Stable Diffusion models. |
| **Option C (Free Cloud API)**| **Hugging Face FLUX.1 Inference** | Free Tier | High-quality FLUX.1 image generation via Hugging Face serverless API. |

---

### 5. 💻 Enterprise UI & Reader Interface

| Option | Technology | Cost / License | Description & Use Case |
| :--- | :--- | :--- | :--- |
| **Option A (Lightweight)** | **Vanilla HTML5 + Alpine.js + CSS Variables** | 100% Free (MIT) | Current implementation. Zero-build step, ultrafast rendering, pristine light-mode parchment UI. |
| **Option B (Modern SPA)** | **React.js** / **Vue.js 3** + **Tailwind CSS** | Open Source (MIT) | Component-based modern frontend with interactive branch flowcharts and animated tab views. |
| **Option C (Pure Python)** | **Streamlit** / **Gradio** / **NiceGUI** | Open Source (Apache 2.0) | Build the complete UI in Python without writing HTML/JS. Great for rapid prototyping. |

---

### 6. 📦 Object Storage & E-Book Export

| Option | Technology | Cost / License | Description & Use Case |
| :--- | :--- | :--- | :--- |
| **Option A (Cloud Free)** | **Cloudflare R2** | Free Tier (10GB / mo) | S3-compatible object storage with **zero egress fees**. Perfect for serving public media and e-books. |
| **Option B (Self-Hosted)** | **MinIO Object Storage** | Open Source (AGPLv3) | High-performance, S3-compatible local object storage server. |
| **Option C (Local Disk)** | **Local Static Directory** + FastAPI | 100% Free | Serve media and e-books directly from local filesystem path mounted in container. |

---

### 7. 🚀 Hosting & Deployment Options

| Option | Technology | Cost / License | Description & Use Case |
| :--- | :--- | :--- | :--- |
| **Option A (Self-Hosted PaaS)**| **Coolify** / **CapRover** on $5/mo VPS | Open Source | Open-source alternative to Heroku/Render. Host frontend, DB, and containers on your own server. |
| **Option B (Container PaaS)** | **Render.com** / **Fly.io** | Free Tier | Deploy web services and databases directly from Dockerfiles or GitHub repos. |
| **Option C (Static + Serverless)**| **Vercel** / **Netlify** + **Supabase** | Free Tier | Host frontend statically on Vercel CDN and run backend logic via serverless edge functions. |

---

## 🎯 Preset Architecture Blueprints

### Blueprint 1: 100% Local / Offline Private Stack
> *For users who want zero cloud bills, total privacy, and full offline operation.*

- **LLM Engine**: Ollama (`llama3.3:70b` or `mistral-nemo`)
- **Agent Orchestrator**: LangChain Python
- **Database**: SQLite + SQLAlchemy
- **Vector / Memory Store**: ChromaDB (Embedded)
- **Image Generation**: Local ComfyUI (SDXL Turbo)
- **Object Storage**: Local Disk Storage
- **Frontend**: Streamlit or Alpine.js + FastAPI
- **Hosting**: Local Machine / Home Server

---

### Blueprint 2: Cloud-Native 100% Free-Tier Stack
> *For hosting a public web application without paying cloud subscription costs.*

- **LLM Engine**: Groq API (`llama-3.3-70b-versatile`)
- **Agent Orchestrator**: ADK (Agent Development Kit) or LangChain
- **Database**: Supabase PostgreSQL (Free Tier)
- **Vector / Memory Store**: Supabase `pgvector`
- **Image Generation**: Pollinations.ai REST API
- **Object Storage**: Cloudflare R2 (10GB Free S3 storage)
- **Frontend**: Vite + React + Tailwind CSS
- **Hosting**: Vercel (Frontend) + Render.com Free Tier (FastAPI Backend)

---

### Blueprint 3: Enterprise Self-Hosted Docker Compose Stack
> *For deploying a production-ready single-node server with open-source tools.*

- **LLM Engine**: Local vLLM container or Hugging Face TGI
- **Database**: MongoDB Community Container
- **Vector Store**: Qdrant Community Container
- **Image Generation**: Fooocus Docker Container
- **Object Storage**: MinIO Container
- **Frontend & Backend**: FastAPI + Alpine.js served via Nginx
- **Deployment Control Panel**: Coolify / Docker Compose

---

## 🔄 How to Convert Current Implementation to Freeware

To replace GCP Vertex AI and Cloud Run components in the current project:

1. **Replace Gemini 2.5 Flash**: Swap `google.adk.models.Gemini` in `app/agent.py` with `Ollama` or `Groq` model adapter.
2. **Replace Firestore**: Update `app/tools/firestore_tools.py` to use `sqlite3` or `supabase-py`.
3. **Replace Vertex Memory Bank**: Update `generate_memories_callback` in `app/agent.py` to store chat vectors in `ChromaDB` or `Qdrant`.
4. **Replace Imagen 3**: Update `app/tools/image_tool.py` to call Pollinations.ai endpoint: `https://image.pollinations.ai/prompt/{prompt}`.
5. **Replace Cloud Storage**: Update `app/tools/export_tool.py` to write e-books to local `./static/exports` or Cloudflare R2 bucket.
