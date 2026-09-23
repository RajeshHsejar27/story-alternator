"""Upload tool for custom e-books and text parsing."""

import datetime
from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-02-f255a355adec"
COLLECTION_NAME = "story_branches"


def analyze_uploaded_book(
    book_title: str, author: str, text_content: str, chapter_name: str = "Chapter 1"
) -> str:
    """Parses custom uploaded e-book text content and stores it as an initial story branch in Firestore for alteration.

    Args:
        book_title: Title of the uploaded book.
        author: Author of the book.
        text_content: The text or excerpt of the uploaded book.
        chapter_name: Name of the initial chapter or section.

    Returns:
        Status message with confirmation and branch details.
    """
    branch_id = f"custom_{book_title.lower().replace(' ', '-')}_{chapter_name.lower().replace(' ', '-')}"
    doc_data = {
        "book_title": book_title,
        "author": author,
        "chapter_name": chapter_name,
        "branch_id": branch_id,
        "content": text_content,
        "summary": f"Uploaded custom text from '{book_title}' by {author}.",
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "choices": [
            "What if the protagonist takes a completely different path?",
            "What if the secret is revealed immediately?",
            "What if a key event fails?",
        ],
    }

    try:
        db = firestore.Client(project=PROJECT_ID, database="(default)")
        db.collection(COLLECTION_NAME).document(branch_id).set(doc_data)
        return (
            f"📚 Custom book '{book_title}' successfully uploaded and parsed into Firestore!\n"
            f"Branch ID: {branch_id}\n"
            f"Preview: {text_content[:150]}...\n\n"
            f"Available Alternate Paths:\n"
            + "\n".join(f"- {c}" for c in doc_data["choices"])
        )
    except Exception as e:
        return f"Parsed custom book '{book_title}' ({len(text_content)} chars). Notice: {e}"
