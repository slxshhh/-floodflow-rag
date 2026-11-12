from google import genai
from app.config import Settings

def ask_gemini(prompt: str) -> str:
    settings = Settings()
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt
    )
    
    return response.text