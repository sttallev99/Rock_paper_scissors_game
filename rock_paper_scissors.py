import random
from colorama import Fore, Back, Style

player_score = 0
computer_score = 0

while True:
    player_choice = input("Please choose [r]ock, [p]aper, or [s]cissors: ")
    player_move = ""

    choices = ["Rock", "Paper", "Scissors"]
    random_choice = random.choice(choices)

    print(Fore.BLUE + f"Computer choose: {random_choice}")

    if player_choice == "r":
        player_move = "Rock"
    elif player_choice == "p":
        player_move = "Paper"
    elif player_choice == "s":
        player_move = "Scissors"
    else:
        raise SystemExit("Invalid input! Try again...")

    if (player_move == "Rock" and random_choice == "Scissors") or \
            (player_move == "Scissors" and random_choice == "Paper") or \
            (player_move == "Paper" and random_choice == "Rock"):
        print(Fore.GREEN + "You Win!")
        player_score += 1
    elif (player_move == "Rock" and random_choice == "Paper") or \
            (player_move == "Scissors" and random_choice == "Rock") or \
            (player_move == "Paper" and random_choice == "Scissors"):
        print(Fore.RED + "You Lose!")
        computer_score += 1
    elif (player_move == "Rock" and random_choice == "Rock") or \
            (player_move == "Scissors" and random_choice == "Scissors") or \
            (player_move == "Paper" and random_choice == "Paper"):
        print(Fore.YELLOW + "Draw!")

    print()
    print(Style.RESET_ALL + f"Current score:\n Computer - {computer_score}\n Player - {player_score}")

    restart = input(Style.RESET_ALL + "Type [yes] to Play Again or [no] to quit: ")

    if restart != 'yes':
        break




