slot1 = "e"
slot2 = "e"
three = "e"
four = "e"
five = "e"
six = "e"
seven = "e"
eight = "e"
nine = "e"
print("You are x")
def play(slot1,slot2,three,four,five,six,seven,eight,nine):
    global turn
    print(slot1, slot2, three)
    print(four, five ,six)
    print(seven , eight, nine) 
    print("""
          1
          2
          3
          4
          5
          6
          7
          8
          9
          """)
    turn = int(input("Where do you want to put your mark choose a spot on the 3x3 grid 'E' is an empty space:"))
    if turn == 1:
         slot1 = "x"
    elif turn == 2:
        slot2 = "x"
    play(slot1,slot2,three,four,five,six,seven,eight,nine)

