import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "story_database.sqlite")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        cover_gradient TEXT,
        badge TEXT,
        description TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS branches (
        id TEXT PRIMARY KEY,
        book_id TEXT NOT NULL,
        title TEXT NOT NULL,
        chapter TEXT NOT NULL,
        img TEXT,
        text TEXT NOT NULL,
        FOREIGN KEY (book_id) REFERENCES books (id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        memory_text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    # Seed default books if empty
    cursor.execute("SELECT COUNT(*) as count FROM books")
    if cursor.fetchone()["count"] == 0:
        seed_default_data(cursor)
        conn.commit()

    conn.close()

def seed_default_data(cursor):
    books = [
        (
            "pride_and_prejudice",
            "Pride and Prejudice",
            "Jane Austen",
            "linear-gradient(135deg, #4f46e5, #7c3aed)",
            "Classic Romance",
            "Elizabeth Bennet navigates issues of manners, upbringing, and marriage in Regency England."
        ),
        (
            "great_gatsby",
            "The Great Gatsby",
            "F. Scott Fitzgerald",
            "linear-gradient(135deg, #059669, #0d9488)",
            "Modernist Classic",
            "Jay Gatsby's obsessive pursuit of Daisy Buchanan amidst the roaring twenties."
        ),
        (
            "frankenstein",
            "Frankenstein",
            "Mary Shelley",
            "linear-gradient(135deg, #d97706, #b45309)",
            "Gothic Horror",
            "Victor Frankenstein creates a sentient creature with unforeseen catastrophic consequences."
        )
    ]

    cursor.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", books)

    branches = [
        (
            "pride_orig",
            "pride_and_prejudice",
            "Original Chapter 34",
            "Chapter 34",
            "https://storage.googleapis.com/story-alternator-media-qwiklabs-gcp-02-f255a355adec/scene_e94e0ab1.jpg",
            "Elizabeth was sitting by herself, reading Jane's letters again, and finding little in them to console her. She was suddenly disturbed by the sound of the door bell, and her surprise was great on finding it to be Mr. Darcy. He entered the room in a hurried manner, and inquired after her health, imputing his visit to a wish of hearing that she were better.\n\nHe sat down for a few moments, and then getting up, walked about the room. Elizabeth was surprised, but said not a word. After a silence of several minutes, he came towards her in an agitated manner, and thus began:\n\n\"In vain have I struggled. It will not do. My feelings will not be repressed. You must allow me to tell you how ardently I admire and love you.\" Elizabeth's astonishment was beyond expression."
        ),
        (
            "pride_apology",
            "pride_and_prejudice",
            "Darcy's Humble Apology",
            "Chapter 34 Alternate",
            "https://storage.googleapis.com/story-alternator-media-qwiklabs-gcp-02-f255a355adec/scene_e94e0ab1.jpg",
            "Mr. Darcy paused at the doorway, his posture softening as Elizabeth's sharp words hung in the air. Instead of leaving in wounded pride, he turned back to face her with quiet humility.\n\n\"Miss Bennet,\" he said softly, \"I realize now how deeply my pride has blinded me to the distress I have caused. I ask for your patience to let me explain my actions regarding your sister and Mr. Wickham before I take my leave forever.\" Elizabeth looked at him, surprised by the sudden vulnerability in his voice."
        ),
        (
            "gatsby_orig",
            "great_gatsby",
            "Original Chapter 5 (Reunion)",
            "Chapter 5",
            "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
            "Gatsby, his hands still in his pockets, was reclining against the mantelpiece in a strained counterfeit of perfect ease. His head leaned back so far that it rested against the face of an extinct mantelpiece clock.\n\n\"We've met before,\" muttered Gatsby. His eyes met Nick's, and a faint smile crossed his face."
        ),
        (
            "frankenstein_orig",
            "frankenstein",
            "Original Summit Encounter",
            "Chapter 10",
            "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=800&q=80",
            "It was nearly noon when I reached the summit of the Montanvert. I suddenly beheld the figure of a man, advancing towards me with superhuman speed. The stature of the man exceeded that of a man. It was the wretch whom I had created."
        )
    ]

    cursor.executemany("INSERT INTO branches VALUES (?, ?, ?, ?, ?, ?)", branches)
