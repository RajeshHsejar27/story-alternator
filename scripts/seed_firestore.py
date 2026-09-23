import datetime
from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-02-f255a355adec"

def seed_database():
    db = firestore.Client(project=PROJECT_ID, database="(default)")
    collection_ref = db.collection("story_branches")

    seed_items = [
        {
            "book_id": "pride-and-prejudice",
            "book_title": "Pride and Prejudice",
            "chapter_id": "chapter-34",
            "choice_prompt": "Elizabeth accepts Mr. Darcy's first proposal at Hunsford.",
            "divergence_node": "Hunsford Parsonage Proposal",
            "alternate_text": "Elizabeth paused, the sharpness of her intended rebuke melting into astonishment. Seeing the genuine agony in Mr. Darcy's eyes, she offered her hand, agreeing to a courtship built on mutual honesty.",
            "author_style": "19th-century Regency prose (Jane Austen style)",
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        },
        {
            "book_id": "the-great-gatsby",
            "book_title": "The Great Gatsby",
            "chapter_id": "chapter-7",
            "choice_prompt": "Gatsby tells Tom Buchanan the full truth calmly and leaves New York before the accident.",
            "divergence_node": "Plaza Hotel Confrontation",
            "alternate_text": "Gatsby adjusted his coat, looked Tom in the eye with quiet dignity, and walked out into the cool evening air, choosing to build a legacy unburdened by past illusions.",
            "author_style": "Roaring Twenties modernist prose (F. Scott Fitzgerald style)",
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
    ]

    for item in seed_items:
        doc_id = f"{item['book_id']}_{item['chapter_id']}"
        collection_ref.document(doc_id).set(item)
        print(f"Seeded document: {doc_id}")

if __name__ == "__main__":
    seed_database()
