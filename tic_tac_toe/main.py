#Asher Wangia, Tic-Tac-Toe game
import random

slot1 = "1"
slot2 = "2"
slot3 = "3"
slot4 = "4"
slot5 = "5"
slot6 = "6"
slot7 = "7"
slot8 = "8"
slot9 = "9"

row_1 = [slot1,slot2,slot3]
row_2 = [slot4,slot5,slot6]
row_3 = [slot7,slot8,slot9]

board = [[row_1]
         ,[row_2]
         ,[row_3]]

choices = [1,2,3,4,5,6,7,8,9]

print("You are x")
game = True

while game == True:
    for x in board:
        print(x)
    
    user_choice = input("Choose a spot to place your mark: ")
	
    if user_choice != "X" or "O" and user_choice == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        if user_choice == slot1:
            slot1 == "X"
        elif user_choice == slot2:
            slot2 = "X"
        elif user_choice == slot3:
            slot3 = "X"
        elif user_choice == slot4:
            slot4 = "X"
        elif user_choice == slot5:
            slot5 = "X"
        elif user_choice == slot6:
            slot6 = "X"
        elif user_choice == slot7:
            slot7 = "X"
        elif user_choice == slot8:
            slot8 = "X"
        elif user_choice == slot9:
            slot9 = "X"
    else:
        print("User Choice Invalid")
        continue

    comp_choice = random.choice(choices)
    
    if comp_choice == 1:
        if slot1 != "X" or "O":
            slot1 == "O"
        else:
            comp_choice = random.choice(choices)
    elif comp_choice == 2:
        if slot2 != "X" or "O":
            slot2 == "O"
        else:
            comp_choice = random.choice(choices)
    elif comp_choice == 3:
        if slot3 != "X" or "O":
            slot3 == "O"
        else:
            comp_choice = random.choice(choices)
    elif comp_choice == 4:
        if slot4 != "X" or "O":
            slot4 == "O"
        else:
            comp_choice = random.choice(choices)
    elif comp_choice == 5:
        if slot5 != "X" or "O":
            slot5 == "O"
        else:
            comp_choice = random.choice(choices)
    elif comp_choice == 6:
        if slot6 != "X" or "O":
            slot6 == "O"
        else:
            comp_choice = random.choice(choices)
    elif comp_choice == 7:
        if slot7 != "X" or "O":
            slot7 == "O"
        else:
            comp_choice = random.choice(choices)
    elif comp_choice == 8:
        if slot8 != "X" or "O":
            slot8 == "O"
        else:
            comp_choice = random.choice(choices)
    elif comp_choice == 9:
        if slot9 != "X" or "O":
            slot9 == "O"
        else:
            comp_choice = random.choice(choices)