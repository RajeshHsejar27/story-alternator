import requests

def search_public_books(query: str) -> str:
    """Searches public domain books using the free Gutendex API (Project Gutenberg catalog).
    
    Args:
        query: Search term for book title, author, or subject (e.g., 'Pride and Prejudice', 'Fitzgerald').
        
    Returns:
        Formatted summary of matching public domain books with Gutenberg IDs and download links.
    """
    url = f"https://gutendex.com/books/?search={requests.utils.quote(query)}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"Error fetching public books: HTTP status {response.status_code}"
            
        data = response.json()
        results = data.get("results", [])
        if not results:
            return f"No public domain books found matching '{query}'."
            
        formatted_books = []
        for book in results[:5]:  # Return top 5 matches
            title = book.get("title", "Unknown Title")
            authors = ", ".join([a.get("name", "") for a in book.get("authors", [])])
            languages = ", ".join(book.get("languages", []))
            download_count = book.get("download_count", 0)
            book_id = book.get("id")
            formatted_books.append(
                f"📖 Title: {title}\n   Author(s): {authors}\n   ID: {book_id} | Lang: {languages} | Downloads: {download_count}"
            )
            
        return "\n\n".join(formatted_books)
    except Exception as e:
        return f"Failed to query public book API: {str(e)}"
