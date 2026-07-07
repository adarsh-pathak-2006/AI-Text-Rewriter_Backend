from services.build_prompt import build_prompt
from services.gemini_client import generate_response


def rewrite_text(text, style):
    prompt=build_prompt(text=text, style=style)

    output=generate_response(prompt=prompt)

    return output
