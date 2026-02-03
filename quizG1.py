
# improved
def quiz_game():
    asking = input("Hey, would you like to play? (yes/no): ").strip().lower()
    if asking not in ["yes", "y"]:
        print("Game stopped. Goodbye!")
        return

    print("Let's play! 🎉")
    count = 0

    # List of questions and answers
    questions = [
        ("What does CPU stand for?", "central processing unit"),
        ("Full form of NASA?", "national aeronautics and space administration"),
        ("What does IDE stand for?", "integrated development environment"),
        ("What does VCS stand for?", "version control system"),
    ]

    # Loop through questions
    for q, ans in questions:
        print(q)
        user_answer = input().strip().lower()
        if user_answer == ans:
            print("✅ Correct!")
            count += 1
        else:
            print("❌ Incorrect")

    # Final score
    print("\n--- Results ---")
    print(f"You got {count} out of {len(questions)} correct answers.")
    score = (count / len(questions)) * 100
    print(f"Your score: {score:.2f}%")

    if count == len(questions):
        print("🎉 Congrats! You nailed all the answers!")
    elif count >= len(questions)//2:
        print("👍 Good job, keep practicing!")
    else:
        print("💡 Keep learning, you'll get better next time!")

quiz_game()

'''asking = input("hey would you like to play? ").lower()
count = 0
 
if asking=="yes":
    print("lets play.")
else:
    print("game stopped")
    quit()

print("what does cpu stands for ? ")

Q1 = input().lower()
if Q1 == "central processing unit":
    print ("correct!")
    count+=1
else:
    print("incorrect")

print("full form of NASA ? ")

Q2 = input().lower()
if Q2== "national aeronautics and space administration":
    print("correct!")
    count+=1 
else:
    print("incorrect")

print("what does ide stands for ? ")

Q3 = input().lower()
if Q3== "integrated development environment":
    print("correct!")
    count+=1 
else:
    print("incorrect")

print("what does vcs stands for ?")

Q4 = input().lower()
if Q4== "version control system":
    print("correct!")
    count+=1  
else:
    print("incorrect")  

if count==4:
    print("congrats! for getting all correct answers")

print (f'You got {count} correct answers, thanks for playing') 
print(f'You scored {(count/4)*100}%')'''