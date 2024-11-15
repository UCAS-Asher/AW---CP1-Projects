#Asher Wangia, Rock, Paper, Scissors

import random

choices = ["rock","paper","scissors","exit"]
play = True
player_score = 0
comp_score = 0
comp_choices = ["rock","paper","scissors"]

while play == True:
    comp_choice = random.choice(comp_choices)
    user_choice = input("Pick rock, paper or scissors or exit to quit: ")
    print("Computer choose:",comp_choice)
    if user_choice == "rock" or "paper" or "scissors" or "exit":
        if user_choice == comp_choice:
            print("Its a Tie")
        elif user_choice == "rock" and comp_choice == "scissors":
            print("User Won")
            player_score +=1
        elif user_choice == "scissors" and comp_choice == "paper":
            print("User Won")
            player_score +=1
        elif user_choice == "paper" and comp_choice == "rock":
            print("User Won")
            player_score +=1
        elif user_choice == "exit":
            print("Player Score:", player_score)
            print("Computer Score:", comp_score)
            play = False
            break
        elif comp_choice == "rock" and user_choice == "scissors":
            print("Computer Won")
            comp_score +=1
        elif comp_choice == "scissors" and user_choice == "paper":
            print("Computer Won")
            comp_score +=1
        elif comp_choice == "paper" and user_choice == "rock":
            print("Computer Won")
            comp_score +=1
        else:
            print("Invalid Choice")
            continue

   