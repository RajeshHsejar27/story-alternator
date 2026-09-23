import uuid
from google import genai
from google.cloud import storage
from google.genai import types
from google.adk.tools import ToolContext

PROJECT_ID = "qwiklabs-gcp-02-f255a355adec"
BUCKET_NAME = "story-alternator-media-qwiklabs-gcp-02-f255a355adec"

async def generate_scene_illustration(prompt: str, tool_context: ToolContext = None) -> str:
    """Generates a visual scene illustration for an alternate story path using gemini-3.1-flash-lite-image.
    Saves the image artifact to the Playground and uploads it to public Cloud Storage.
    
    Args:
        prompt: Detailed visual prompt describing the story scene (e.g. 'Elizabeth Bennet and Mr. Darcy walking in Pemberley gardens, Regency oil painting style').
        tool_context: ADK ToolContext provided automatically by the runner.
        
    Returns:
        Public HTTPS URL of the uploaded image in Cloud Storage.
    """
    client = genai.Client(vertexai=True, project=PROJECT_ID, location="global")
    res = client.models.generate_content(
        model="gemini-3.1-flash-lite-image",
        contents=f"Generate a high-quality story scene illustration: {prompt}"
    )
    
    image_bytes = None
    mime_type = "image/jpeg"
    for part in res.candidates[0].content.parts:
        if part.inline_data:
            image_bytes = part.inline_data.data
            if part.inline_data.mime_type:
                mime_type = part.inline_data.mime_type
            break
            
    if not image_bytes:
        return "Failed to generate image bytes from model."
        
    filename = f"scene_{uuid.uuid4().hex[:8]}.jpg"
    
    # 1. Save artifact if tool_context is provided
    if tool_context:
        artifact = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
        await tool_context.save_artifact(filename=filename, artifact=artifact)
        
    # 2. Upload to public Cloud Storage bucket
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(filename)
    blob.upload_from_string(image_bytes, content_type=mime_type)
    
    public_url = f"https://storage.googleapis.com/{BUCKET_NAME}/{filename}"
    return f"Generated scene illustration successfully! Public Image URL: {public_url}"
