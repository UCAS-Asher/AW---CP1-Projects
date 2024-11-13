slot1 = "1"
slot2 = "2"
slot3 = "3"
slot4 = "4"
slot5 = "5"
slot6 = "6"
slot7 = "7"
slot8 = "8"
slot9 = "9"
print("You are x")
def play():
    
    print(slot1, slot2, slot3)
    print(slot4, slot5 ,slot6)
    print(slot7 , slot8, slot9) 
    turn = int(input("Where do you want to put your mark choose a spot on the 3x3 grid 'E' is an empty space:"))
    if turn == 1:
         slot1 = "X"
    elif turn == 2:
        slot2 = "X"
    print(play())
turn = input("choose a spot:")
if turn == (slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot9):
     = "x"