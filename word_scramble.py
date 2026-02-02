import random

def scramble_word(word):
    """Return a scrambled version of the given word."""
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)


# List of words to scramble

def play_game():
    WORDS = ["python", "developer", "hangman", "heisenberg", "mike", "heyyo", "saulgoodman", "breakingbad"]
    score = 0
    print("Welcome to Word Scramble!")
    print("Unscramble the letters to form the correct word.\n")

    for word in words:
        scrambled = scramble_word(word)
        print(f"Scrambled word: {scrambled}")
        guess = input("Your guess: ").strip().lower()

        if guess == word:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. The word was: {word}\n")

    print(f"Game over! Your score: {score}/{len(words)}")






