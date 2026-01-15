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
 yn= ("y", "n")
 to_continue = input("continue? (y/n): ").lower()
 if to_continue=="n":
    print("thanks for playing!")
    quit()
 elif to_continue not in yn:
    print ("invalid input")
    print (to_continue)