import random # Import the random library
answer = random.randint(1, 100) # Get a random number from 1-100


def check_isdigit(user_input):
    return user_input.isdigit() # Function only returns True or False as isdigit() returns a boolean value

while True: # Infinite loop as we dont know when the user will guess the number, so we iterate until the user guesses right and then break
    user_answer = input("Guess a number from 1-100: ") # Input() always returns input as a string
    if not check_isdigit(user_answer): # If the check_isdigit returns false...
        print("Enter a valid number.") # We notify the user that he needs to enter a valid number
        continue # We use continue which skips everything after it and we enter a new loop
    
    user_answer = int(user_answer) # We reassign the user_answer variable as an integer

# Logic to notify user how close he is to guess the number
    if user_answer > answer:
        print("Lower")
    elif user_answer < answer:
        print("Higher")
    else:
        print(f"Correct the number was {answer}!")
        break # When the user guesses it right, we break the loop and end the script
    
