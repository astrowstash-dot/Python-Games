import random

count=0
number = random.randint(1,100)
while True:
 try:
   guess = int(input("guess the number: "))

   if guess > 100 or guess < 1:
    print("input is 1-100")
   if guess < number:
    print("guess higher")
    count+=1
   elif guess > number:
    print("guess lower")
    count+=1
   else:
    print ("correct guess!")
    count+=1
    print(f'number of guesses are {count}')
    quit()
    

 except ValueError:
   print("invalid input!")



   
 # -----Same but little modified.------  
 '''import random
number = random.randint(1,100)
guess = int (input("guess the number: "))
count=1
if guess not in range(1,101):
   print("invalid input!")
   
while guess!=number:
    if guess<number:
       print("guess higher")
    else:
       print("guess lower")
    guess = int (input("guess the number: "))
    count+=1
else:
   print("correct guess!")
   print(f'number of guesses are {count}')'''

        
   

    
   
    



   








