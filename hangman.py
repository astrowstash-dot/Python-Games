import random

def hangman():
    words = ["python", "chess", "automation", "neon", "storytelling"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
