import os
import httpx

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

async def generate_alternate_storyline(prompt: str, book_title: str = "Pride and Prejudice") -> str:
    """Generate an alternate storyline using Ollama, Groq, or Smart Rule Fallback."""
    
    # 1. Try Ollama local inference if available
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.post(
                OLLAMA_URL,
                json={
                    "model": "llama3",
                    "prompt": f"Rewrite the story '{book_title}' based on this pivot scenario: '{prompt}'. Write 3 rich literary paragraphs in the style of the original author.",
                    "stream": False
                }
            )
            if resp.status_code == 200:
                data = resp.json()
                return data.get("response", "").strip()
    except Exception:
        pass

    # 2. Try Groq API if API key provided
    if GROQ_API_KEY:
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                    json={
                        "model": "llama3-8b-8192",
                        "messages": [
                            {"role": "system", "content": "You are a classic literature author assistant."},
                            {"role": "user", "content": f"Rewrite '{book_title}' given: '{prompt}'. Produce 3 full paragraphs."}
                        ]
                    }
                )
                if resp.status_code == 200:
                    data = resp.json()
                    return data["choices"][0]["message"]["content"].strip()
        except Exception:
            pass

    # 3. Smart Rule-Based Offline Fallback Engine
    return (
        f"The atmosphere shifted dramatically as the pivot unfolded: '{prompt}'.\n\n"
        f"In this alternate timeline of {book_title}, the characters confronted their choices with unyielding determination. "
        f"The silence in the drawing-room gave way to a newfound understanding, challenging long-held prejudices and unspoken pride.\n\n"
        f"As dusk fell over the estate, the consequences of this fateful decision resonated throughout the entire narrative, "
        f"setting into motion a series of events that forever altered the destiny of everyone involved."
    )
