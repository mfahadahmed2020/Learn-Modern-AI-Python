import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: Rock, Paper, or Scissors. Type 'quit' to exit the game.")
    
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "quit":
            print("Thank you for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__": # type: ignore
    play_game()