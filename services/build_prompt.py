def build_prompt(text, style):
    prompt=f"""
You are an expert English writing assistant.

Rewrite the given text.

Instructions:

- Style: {style}
- Preserve the original meaning.
- Improve grammar.
- Improve sentence structure.
- Return ONLY the rewritten text.
- Do not explain anything.
- Do not add bullet points.

Text:

{text}

"""
    return prompt