#Asher Wangia, Tic-Tac-Toe game
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
         ]
print("You are x")
game = True

while game == True:
    for x in row_1:
        print(x)
    for x in row_2:
        print(x)
    for x in row_3:
        print(x)
    break