import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("=== Dice Roll Game ===")
    player = roll_dice()
    computer = roll_dice()

    print(f"You rolled: {player}")
    print(f"Computer rolled: {computer}")

    if player > computer:
        print("You win!")
    elif player < computer:
        print("Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()


'''def main():
    print("=== Dice Roll Game ===")
    rounds = int(input("How many rounds would you like to play? "))
    player_score, computer_score = 0, 0

    for i in range(rounds):
        print(f"\nRound {i+1}")
        player = roll_dice()
        computer = roll_dice()
        print(f"You rolled: {player}")
        print(f"Computer rolled: {computer}")

        if player > computer:
            print("You win this round!")
            player_score += 1
        elif player < computer:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

    print("\n=== Final Results ===")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")
    if player_score > computer_score:
        print("🎉 You are the overall winner!")
    elif player_score < computer_score:
        print("💻 Computer wins overall!")
    else:
        print("🤝 It's an overall tie!")
'''
    
   
      


    
    

    


