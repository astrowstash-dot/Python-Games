asking = input("hey would you like to play? ").lower()
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
print(f'You scored {(count/4)*100}%')