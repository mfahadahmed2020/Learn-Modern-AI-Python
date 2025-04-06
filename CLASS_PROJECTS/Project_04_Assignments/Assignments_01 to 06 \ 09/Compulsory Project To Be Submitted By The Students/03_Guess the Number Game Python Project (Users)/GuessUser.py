import random

def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    print("Respond with:")
    print("'h' if my guess is too high,")
    print("'l' if my guess is too low,")
    print("'c' if my guess is correct.")
    
    # Step 1: Define the range for guessing
    low = 1
    high = 100
    attempts = 0
    
    while True:
        # Step 2: Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1
        
        # Step 3: Show the guess to the user
        print(f"My guess is: {guess}")
        feedback = input("Is it too high (h), too low (l), or correct (c)? ").lower()
        
        # Step 4: Process the user's feedback
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number in {attempts} attempts.")
            break
        else:
            print("Invalid input. Please respond with 'h', 'l', or 'c'.")

# Run the game
guess_the_number()