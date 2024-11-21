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

choices = [slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9]

print("You are X")
game = True

while game == True:
    
    valid = True
    board_row1 = [slot1,slot2,slot3]
    board_row2 = [slot4,slot5,slot6]
    board_row3 = [slot7,slot8,slot9]
    
    board = [board_row1,
            board_row2,
            board_row3]
    
    for x in board:
        print(x)

    
    user_choice = input("Choose a spot to place your mark: ")
	
    if user_choice == "1" and slot1 != "X" and slot1 != "O":
        slot1 = "X"
    elif user_choice == "2" and slot2 != "X" and slot2 != "O":
        slot2 = "X"
    elif user_choice == "3" and slot3 != "X" and slot3 != "O":
        slot3 = "X"
    elif user_choice == "4" and slot4 != "X" and slot4 != "O":
        slot4 = "X"
    elif user_choice == "5" and slot5 != "X" and slot5 != "O":
        slot5 = "X"
    elif user_choice == "6" and slot6 != "X" and slot6 != "O":
        slot6 = "X"
    elif user_choice == "7" and slot7 != "X" and slot7 != "O":
        slot7 = "X"
    elif user_choice == "8" and slot8 != "X" and slot8 != "O":
        slot8 = "X"
    elif user_choice == "9" and slot9 != "X" and slot9 != "O":
        slot9 = "X"
    else:
        print("Invalid Choice Try Again")
        valid = False
    
    
    for x in choices:
        if x == "X" or x == "O":
            choices.remove(x)


    
    comp_choice = random.choice(choices)
    
    if valid == True:
        if comp_choice == slot1:
            slot1 = "O"
        elif comp_choice == slot2:
            slot2 = "O"
        elif comp_choice == slot3:
            slot3 = "O"
        elif comp_choice == slot4:
            slot4 = "O"
        elif comp_choice == slot5:
            slot5 = "O"
        elif comp_choice == slot6:
            slot6 = "O"
        elif comp_choice == slot7:
            slot7 = "O"
        elif comp_choice == slot8:
            slot8 = "O"
        elif comp_choice == slot9:
            slot9 = "O"