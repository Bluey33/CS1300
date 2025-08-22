import random 

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# This asks the user to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Check if the guess was correct depending on the answer it prints correct/sorry.
if guess == secret_number:
    print("Correct! You guessed it!")
else:
    print("Sorry, the number was", secret_number)

    # I want to add a loop here but ill keep it simple4
