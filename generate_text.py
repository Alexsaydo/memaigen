# generate_text.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_meme_caption(user_prompt: str) -> str:
    system_prompt = "Ты мемный гений. На вход получаешь идею, на выходе — короткую, чёткую подпись для мема, максимум 1–2 строки, с юмором или иронией."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.9,
        max_tokens=60
    )

    return response["choices"][0]["message"]["content"].strip()
