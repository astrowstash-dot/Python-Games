import random

def hangman():
    words = ["python", "chess", "automation", "neon", "gang"]
    word = random.choice(words)
    guessed = ["_"]* len(word)
    attempts = 6

    print("===Hangman===")
    while attempts > 0 and "_" in guessed:
        print ("word: "+" ".join(guessed))
        guess = input("Guess a letter: ").lower()

        



