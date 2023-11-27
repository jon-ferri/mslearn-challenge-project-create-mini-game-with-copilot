
# Rock paper scissors game

# Importing random module
import random

# Welcome message
print("Welcome to the Rock Paper Scissors game!")

play_again = "y"
wins = 0
ties = 0
losses = 0

while play_again == "y":
    # Ask the player to choose between rock, paper and scissors
    player = input("Choose between rock, paper and scissors: ")

    # Checking if the player's choice is valid
    if player.lower() != "rock" and player.lower() != "paper" and player.lower() != "scissors":
        print("Invalid choice. Please choose among the options.")
        player = input("Choose between rock, paper and scissors: ")

    # Computer chooses between rock, paper and scissors
    computer = random.choice(["rock", "paper", "scissors"])

    # Checking who wins
    if player.lower() == computer:
        ties += 1
        print("It's a tie!")    
    elif player.lower() == "rock":
        if computer == "paper":
            losses += 1
            print("You lose!", computer, "covers", player)
        else:
            wins += 1
            print("You win!", player, "smashes", computer)
    elif player.lower() == "paper":
        if computer == "scissors":
            losses += 1
            print("You lose!", computer, "cuts", player)
        else:
            wins += 1
            print("You win!", player, "covers", computer)    
    elif player.lower() == "scissors":
        if computer == "rock":
            losses += 1
            print("You lose!", computer, "smashes", player)
        else:
            wins += 1
            print("You win!", player, "cuts", computer)
    # Asking the player if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    # Checking if the player's choice is valid
    if play_again.lower() != "y" and play_again.lower() != "n":
        print("Invalid choice. Please choose 'y' for 'yes' or 'n' for 'no'.")
        play_again = input("Do you want to play again? (y/n): ")

# Printing the final score
print("Your score:", wins)
print("Computer score:", losses)
print("Ties:", ties)