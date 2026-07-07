from google import genai
from django.conf import settings

client=genai.client(
    api_key=settings.GEMINI_API_KEY
)


def generate_response(prompt):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()
