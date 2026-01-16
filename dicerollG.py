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
    
   
      


    
    

    


