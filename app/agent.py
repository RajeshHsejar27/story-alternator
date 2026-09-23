import datetime
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.apps import App
from google.adk.code_executors import AgentEngineSandboxCodeExecutor
from google.adk.models import Gemini
from google.adk.tools import preload_memory
from google.genai import types

from a2ui.schema.manager import A2uiSchemaManager
from a2ui.basic_catalog import BasicCatalog
from app.a2ui_utils import a2ui_callback
from app.tools.firestore_tools import save_story_branch, get_story_branches
from app.tools.public_book_tool import search_public_books
from app.tools.image_tool import generate_scene_illustration
from app.tools.export_tool import export_story_ebook
from app.tools.upload_tool import analyze_uploaded_book

# Memory Bank callback to commit conversation sessions into Vertex AI Memory Bank
async def generate_memories_callback(callback_context: CallbackContext) -> None:
    """Callback to automatically add the current session's conversation to Vertex AI Memory Bank."""
    try:
        await callback_context.add_session_to_memory()
    except Exception as e:
        print(f"Memory bank commit skipped: {e}")

# Build system instructions with A2UI schema manager v0.8
schema_manager = A2uiSchemaManager(
    version="0.8",
    catalogs=[BasicCatalog.get_config("0.8")],
)

base_a2ui_prompt = schema_manager.generate_system_prompt(
    "Interactive Story Alternator & Enterprise Reading Assistant"
)

instruction_prompt = f"""{base_a2ui_prompt}

CRITICAL MANDATES FOR STORY ALTERATION & ENTERPRISE READER PLATFORM:
1. **FULL CHAPTER NARRATIVE REWRITES**: Whenever the user asks for a story pivot or alternate path (e.g. "What if Elizabeth stops Mr. Darcy before he leaves the room?"), you MUST write out the FULL, COMPLETE modified chapter text (at least 4 to 8 long, rich, vivid paragraphs in the authentic literary voice and style of the original author). Never provide just a short summary, commentary, or raw `<a2ui-json>` tags!
2. **AUTOMATIC SCENE ILLUSTRATION**: Always execute `generate_scene_illustration` to generate high-resolution visual scene artwork for the pivotal moment of the new storyline.
3. **SAVE STORY BRANCH**: Always call `save_story_branch` with the full modified chapter text, book title, branch title, and generated illustration URL so it appears in the user's Story Reader dropdown.
4. **E-BOOK EXPORT**: Use `export_story_ebook` when users request to download or export an altered book version.
5. **CUSTOM BOOK UPLOADS**: Use `analyze_uploaded_book` when parsing custom uploaded e-books.

Write with extraordinary literary depth, rich dialog, and complete chapter pages that can be read in full from start to finish.
"""

root_agent = Agent(
    name="story_alternator_agent",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=instruction_prompt,
    tools=[
        search_public_books,
        generate_scene_illustration,
        save_story_branch,
        get_story_branches,
        export_story_ebook,
        analyze_uploaded_book,
        preload_memory,
    ],
    after_agent_callback=generate_memories_callback,
    after_model_callback=a2ui_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)
