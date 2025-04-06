import random

# Introduction of Game
print("Welcome to the 'Guess the Number' game!")

# Step 1: The Computer Will Think of A Random Number
number_to_guess = random.randint(1, 100)  # A Number Between 1 and 100

# Step 2: Instructions to The User
print("I have chosen a number between 1 and 100.")
print("Can you guess what it is?")

# Step 3: Check The Alias Estimate
attempts = 0  # Calculation of Guesses
while True:
    try:
        # User Assessment
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increase The Count on Each Attempt

        # Check The Guess True or False
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
    except ValueError:
        # If User Has Given Wrong input
        print("Invalid input! Please enter a valid number.")