import datetime
from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-02-f255a355adec"

def get_firestore_client():
    return firestore.Client(project=PROJECT_ID, database="(default)")

def save_story_branch(book_id: str, choice_prompt: str, alternate_text: str, author_style: str = "Classic Fiction") -> str:
    """Saves a new alternate story branch into the Firestore story_branches collection.
    
    Args:
        book_id: Identifier for the book (e.g. 'pride-and-prejudice').
        choice_prompt: The user choice or prompt that caused the story to pivot.
        alternate_text: The newly generated alternate story text.
        author_style: Description of the author's writing style and tone.
        
    Returns:
        Status message confirming the saved document ID.
    """
    db = get_firestore_client()
    doc_ref = db.collection("story_branches").document()
    doc_data = {
        "book_id": book_id,
        "choice_prompt": choice_prompt,
        "alternate_text": alternate_text,
        "author_style": author_style,
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    doc_ref.set(doc_data)
    return f"Successfully saved story branch with ID '{doc_ref.id}' for book '{book_id}'."

def get_story_branches(book_id: str) -> str:
    """Retrieves all saved alternate story branches for a given book from Firestore.
    
    Args:
        book_id: Identifier for the book (e.g. 'pride-and-prejudice').
        
    Returns:
        Formatted summary of saved alternate story branches.
    """
    db = get_firestore_client()
    docs = db.collection("story_branches").where("book_id", "==", book_id).get()
    
    if not docs:
        return f"No saved story branches found for book '{book_id}'."
        
    results = []
    for doc in docs:
        data = doc.to_dict()
        results.append(
            f"Branch ID: {doc.id}\nChoice: {data.get('choice_prompt')}\nAlternate Text Snippet: {data.get('alternate_text')[:150]}...\nStyle: {data.get('author_style')}\n"
        )
    return "\n---\n".join(results)
