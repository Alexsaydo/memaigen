# generate_image.py (заглушка-версия)

import random

def generate_image(prompt: str) -> str:
    fallback_images = [
        "https://i.imgur.com/UYBDb5g.jpeg",
        "https://i.imgur.com/Jd4b9hW.jpeg",
        "https://i.imgur.com/Qv5v2ZV.jpeg",
        "https://i.imgur.com/9Wk4qXE.jpeg",
        "https://i.imgur.com/Zi6zr09.png"
    ]
    return random.choice(fallback_images)
