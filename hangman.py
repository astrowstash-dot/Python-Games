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

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess

                else:
                    attempts -= 1
                    print(f'wrong! Attempts left: {attempts}')
    if "_" not in guessed:
        print(f'You guessed the word: {word}')
    else:
        print(f'you lost! The word was: {word}')

if __name__ == "__main__":
    hangman()     


        



