import random

print("Welcome to Rock-Paper-Scissors!")

while True:
    # Get player choice
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    # Check for valid input
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Get computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        break
