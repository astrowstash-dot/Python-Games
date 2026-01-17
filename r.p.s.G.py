import random

emojis = { "r": "🪨","s":"✂️","p":"📄"}
choices=("r","p","s")
while True:
 guess = input("Rock, Paper, Scissors? (r/p/s): ").lower()
 if guess not in choices:
    print("invalid input!")
    continue

 computer_choice = random.choice(choices)


 print (f'you chose {emojis[guess]}')
 print(f'computer chose {emojis[computer_choice]} ')

 if guess==computer_choice:
    print("tie!")
 elif (guess=="r" and computer_choice=="s") or (guess=="s" and computer_choice=="p") or (guess== "p" and computer_choice=="r"):
    print("you win")
 else:
    print("computer win!")
 
 to_continue = input("continue? (y/n): ").lower()
 if to_continue=="n":
    print("thanks for playing!")
    quit()
 
# modified r.p.s game.
'''import random

CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def get_player_choice():
    choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").strip().lower()
    if choice == "q":
        return None
    while choice not in CHOICES:
        print("Invalid choice. Try again.")
        choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").strip().lower()
        if choice == "q":
            return None
    return choice

def decide_winner(player, computer):
    if player == computer:
        return "draw"
    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    return "player" if wins_against[player] == computer else "computer"

def print_score(score):
    print(f"Score → You: {score['player']} | Computer: {score['computer']} | Draws: {score['draw']}")

def main():
    print("=== Rock Paper Scissors ===")
    score = {"player": 0, "computer": 0, "draw": 0}

    while True:
        player = get_player_choice()
        if player is None:
            print("Good game! Final results:")
            print_score(score)
            break

        computer = get_computer_choice()
        print(f"You chose: {player} | Computer chose: {computer}")

        result = decide_winner(player, computer)
        score[result] += 1

        if result == "draw":
            print("It's a draw.")
        elif result == "player":
            print("You win this round!")
        else:
            print("Computer wins this round!")

        print_score(score)
        print("-" * 30)

if __name__ == "__main__":
    main()    '''

