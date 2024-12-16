#Asher Wangia, FINAL: Implementation

import random

one = "Isle of Dragons(1)"
two = "Salamander Mountain(2)"
three = "Dark Goblin Forest(3)"
four = "Enchanted Forest(4)"
five = "Kingdom of Abal(5)"
six = "Goblin Forest(6)"
seven = "Demon Wasteland(7)"
eight = "Destruction Castle(8)"
nine = "Ancient Forest(9)"

game_won = False 

user_location = one
user_health = 100
defense = 5
agility = 5
strength = 5
luck = 5

stat_points = 0
areas = []

def user_areas():
    global areas

    if user_location == one:
        areas = [two,five,four]
    elif user_location == two:
        areas = [one,three,five]
    elif user_location == three:
        areas = [two,six,five]
    elif user_location == four:
        areas = [one,five,seven]
    elif user_location == five:
        areas = [two,three,four,six]
    elif user_location == six:
        areas = [three,five]
    elif user_location == seven:
        areas = [four,eight]
    elif user_location == eight:
        areas = [seven,nine]
    elif user_location == nine:
        areas = [five,six,eight]

def user_action():
    print("""
Choose One of the Actions
    1. Explore the Area
    2. Go to a Diffrent Area      
    3. Stats
    4. Inventory 
          """)
    action = input("Choose a Number: ")

    if action == "1":
        if user_location == one:
            area1()

def area1(stat_points):
    print("""
Choose One of the Actions
    1. Fight the Dragon
    2. Go Back
        """)
    user_area_action = input("Choose a Number: ")

    if user_area_action == "1":
        dragon_hp = 1500
        combat_action = input("Choose 1 to attack or 2 to flee: ")
        if combat_action == "1":
            dragon_hp -= strength * 10
            print("The dragon is at", dragon_hp, "HP now")
            if dragon_hp <= 0:
                stat_points += 15
                print("The Dragon was Defeated!")
                print("You leveled up 3 times!")

       

    elif user_area_action == "2":
        print()



def area2():
    print()



print("""
This is a game where you will have to travel, defeat monsters and level up to defeat the destruction warlord.

You will have an Initial Amount of stat points to distribute to your character and will gain some for each level up.

You will need to defeat monsters to acquire XP to level up.

You can buy equipment from merchants with gold and it can be used to boost your stats.

Agility Stats boost your chances of dodging monster attacks, Strength boosts your damage output, Luck boost your deals on Equipment and your loot drops and Defense boosts your HP.
                        """)

while game_won == False:
    map_row1 = [one,two,three]
    map_row2 = [four,five,six]
    map_row3 = [seven,eight,nine]

    map = [map_row1,
           map_row2,
           map_row3]
    
    print("MAP")
    for row in map:
        print(row)
    user_action()
    break


