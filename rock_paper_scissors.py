import random

player_choice = input("Please choose [r]ock, [p]aper, or [s]cissors: ")
player_move = ""

choices = ["Rock", "Paper", "Scissors"]
random_choice = random.choice(choices)

print(f"Computer choose: {random_choice}")

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
    print("You Win!")
elif (player_move == "Rock" and random_choice == "Paper") or \
        (player_move == "Scissors" and random_choice == "Rock") or \
        (player_move == "Paper" and random_choice == "Scissors"):
    print("You Lose!")
elif (player_move == "Rock" and random_choice == "Rock") or \
        (player_move == "Scissors" and random_choice == "Scissors") or \
        (player_move == "Paper" and random_choice == "Paper"):
    print("Draw!")



