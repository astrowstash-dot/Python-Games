# Function design
def calculate_age(birth_year,current_year):
    if birth_year>current_year:
        return None
    return current_year-birth_year

# CLI input + output
while True:
 import datetime

 current_year = datetime.datetime.now().year

# birth year input

 birth_year_input = input("enter birth year (eg. 2000)")

 try:
     birth_year = int(birth_year_input)
     age = calculate_age(birth_year,current_year)
     if age is None:
         print ("oops! please enter a valid age.")
     else:
         print (f'you are {age} year old in {current_year}')
 except ValueError:
     print("enter a valid age.")

 to_continue = input("continue? (y/n)")
 if to_continue=="n":
     quit()


# improved version 

import datetime

def calculate_age(birth_year, current_year):
    if birth_year > current_year:
        return None
    return current_year - birth_year

while True:
    current_year = datetime.datetime.now().year

    # birth year input
    birth_year_input = input("Enter birth year (e.g. 2000): ")

    try:
        birth_year = int(birth_year_input)
        age = calculate_age(birth_year, current_year)
        if age is None:
            print("Oops! Please enter a valid birth year.")
        else:
            print(f"You are {age} years old in {current_year}.")
    except ValueError:
        print("Please enter a valid year (numbers only).")

    to_continue = input("Continue? (y/n): ").lower()
    if to_continue == "n":
        print("Goodbye!")
        break