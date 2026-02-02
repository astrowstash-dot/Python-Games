import random

def scramble_word(word):
    """Return a scrambled version of the given word."""
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)


# List of words to scramble
WORDS = ["python", "developer", "hangman", "heisenberg", "mike", "heyyo", "saulgoodman", "breakingbad"]
