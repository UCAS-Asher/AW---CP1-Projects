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
    
    board_row1 = [slot1,slot2,slot3]
    board_row2 = [slot4,slot5,slot6]
    board_row3 = [slot7,slot8,slot9]
    
    board = [board_row1,
            board_row2,
            board_row3]
    
    for x in board:
        board = [board_row1,
                board_row2,
                board_row3]
    
        print(x)

    
    user_choice = input("Choose a spot to place your mark: ")
	
    comp_choice = random.choice(choices)

    if user_choice == "1" and slot1 != "X" or "O":
        slot1 = "X"
    else:
        print("Invalid Choice")
    if user_choice == "2" and slot2 != "X" or "O":
        slot2 = "X"
    else:
        print("Invalid Choice")