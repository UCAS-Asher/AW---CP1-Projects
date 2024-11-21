
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
    

while True:
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

    choices = [slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9]
    choices_copy = choices[:]
    
    for x in choices:
        if slot1 in choices and slot1 == "X" or slot1 == "O":
            choices.remove(slot1)
        elif slot2 in choices and slot2 == "X" or slot2 == "O":
            choices.remove(slot2)
        elif slot3 in choices and slot3 == "X" or slot3 == "O":
            choices.remove(slot3)
        elif slot4 in choices and slot4 == "X" or slot4 == "O":
            choices.remove(slot4)
        elif slot5 in choices and slot5 == "X" or slot5 == "O":
            choices.remove(slot5)
        elif slot6 in choices and slot6 == "X" or slot6 == "O":
            choices.remove(slot6)
        elif slot7 in choices and slot7 == "X" or slot7 == "O":
            choices.remove(slot7)
        elif slot8 in choices and slot8 == "X" or slot8 == "O":
            choices.remove(slot8)
        elif slot9 in choices and slot9 == "X" or slot9 == "O":
            choices.remove(slot9)
    
    print(choices)