import os
import uuid
import sqlite3
from fastapi import FastAPI, Request, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import init_db, get_db_connection
from ai_engine import generate_alternate_storyline

app = FastAPI(title="Story Alternator Standalone Backend (Non-GCP)")

# Enable CORS for local React dev server (vite port 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

class ChatRequest(BaseModel):
    message: str
    book_id: str = "pride_and_prejudice"

@app.get("/api/books")
def list_books():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = [dict(row) for row in cursor.fetchall()]

    for book in books:
        cursor.execute("SELECT * FROM branches WHERE book_id = ?", (book["id"],))
        branches = [dict(row) for row in cursor.fetchall()]
        book["branches"] = branches
        book["coverGradient"] = book.get("cover_gradient", "linear-gradient(135deg, #4f46e5, #7c3aed)")
        book["activeBranchId"] = branches[0]["id"] if branches else ""

    conn.close()
    return {"books": books}

@app.post("/api/chat")
async def process_chat(req: ChatRequest):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title FROM books WHERE id = ?", (req.book_id,))
    book_row = cursor.fetchone()
    book_title = book_row["title"] if book_row else "Pride and Prejudice"

    # Generate alternate storyline via Ollama / Groq / Fallback AI
    alternate_text = await generate_alternate_storyline(req.message, book_title)

    branch_id = f"branch_{uuid.uuid4().hex[:8]}"
    branch_title = req.message[:30] + "..." if len(req.message) > 30 else req.message

    cursor.execute(
        "INSERT INTO branches (id, book_id, title, chapter, img, text) VALUES (?, ?, ?, ?, ?, ?)",
        (
            branch_id,
            req.book_id,
            branch_title,
            f"{book_title} Alternate",
            "https://storage.googleapis.com/story-alternator-media-qwiklabs-gcp-02-f255a355adec/scene_e94e0ab1.jpg",
            alternate_text
        )
    )
    conn.commit()
    conn.close()

    return {
        "branch_id": branch_id,
        "title": branch_title,
        "text": alternate_text,
        "img": "https://storage.googleapis.com/story-alternator-media-qwiklabs-gcp-02-f255a355adec/scene_e94e0ab1.jpg"
    }

@app.post("/api/upload")
async def upload_book(
    file: UploadFile = File(...),
    title: str = Form("Custom E-Book"),
    author: str = Form("Anonymous")
):
    content_bytes = await file.read()
    try:
        text = content_bytes.decode("utf-8")
    except Exception:
        text = content_bytes.decode("latin-1", errors="ignore")

    book_id = f"upload_{uuid.uuid4().hex[:8]}"
    branch_id = f"{book_id}_orig"

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)",
        (
            book_id,
            title,
            author,
            "linear-gradient(135deg, #ec4899, #8b5cf6)",
            "Custom Upload",
            f"Uploaded e-book: {title}"
        )
    )

    cursor.execute(
        "INSERT INTO branches VALUES (?, ?, ?, ?, ?, ?)",
        (
            branch_id,
            book_id,
            "Original Chapter 1",
            "Chapter 1",
            "",
            text[:5000]
        )
    )
    conn.commit()
    conn.close()

    return {"book_id": book_id, "title": title, "author": author}

@app.get("/api/export/{book_id}/{branch_id}")
def export_ebook(book_id: str, branch_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title, author FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    cursor.execute("SELECT title, chapter, text FROM branches WHERE id = ?", (branch_id,))
    branch = cursor.fetchone()
    conn.close()

    if not book or not branch:
        raise HTTPException(status_code=404, detail="Book or branch not found")

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{book['title']} - {branch['title']}</title>
        <style>
            body {{ font-family: Georgia, serif; margin: 40px; line-height: 1.8; color: #1e293b; background: #fcfbf7; }}
            h1 {{ text-align: center; color: #0f172a; }}
            h2 {{ text-align: center; color: #6d28d9; font-style: italic; }}
            p {{ text-align: justify; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <h1>{book['title']}</h1>
        <h2>By {book['author']} — {branch['chapter']}: {branch['title']}</h2>
        <hr/>
        {"".join(f"<p>{p}</p>" for p in branch['text'].split('\n\n'))}
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, headers={"Content-Disposition": f"attachment; filename={branch_id}.html"})

# Serve React static frontend if built in frontend-react/dist
static_dist = os.path.join(os.path.dirname(__file__), "..", "frontend-react", "dist")
if os.path.exists(static_dist):
    app.mount("/", StaticFiles(directory=static_dist, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
