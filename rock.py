import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors!")
        print("Type 'rock', 'paper', or 'scissors' to play.")
        print("Type 'exit' to quit.")
        user_choice = input("Your choice: ").lower()

        if user_choice == "exit":
            print(f"\nFinal Scores - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

if __name__ == "__main__":
    play_game()
