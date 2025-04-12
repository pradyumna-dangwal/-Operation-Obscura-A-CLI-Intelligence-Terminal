import time
import random

def glitch_text(text):
    glitched = ''.join(c if random.random() > 0.1 else "#" for c in text)
    print("\n".join([glitched for _ in range(2)]))
    return f"~[{text}]~"