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
total_health = defense*10 + 100
stat_points = 0
storage = []
areas = []

gold = 0
potion = 0
super_potion = 0
ultra_potion = 0

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

def user_move():
    print("Your location is", user_location)
    print("These are your available paths", areas)
    move = input("Choose the number of the location you want to go to: ")
    
    if move == "1" and one in areas:
        user_location = one
    elif move == "2" and two in areas:
        user_location = two
    elif move == "3" and three in areas:
        user_location = three
    elif move == "4" and four in areas:
        user_location = four
    elif move == "5" and five in areas:
        user_location = five
    elif move == "6" and six in areas:
        user_location = six
    elif move == "7" and seven in areas:
        user_location = seven
    elif move == "8" and eight in areas:
        user_location = eight
    elif move == "9" and nine in areas:
        user_location = nine
    else:
        print("Invalid Option")
        user_move()

def user_stats(strength,defense,agility,luck):
    print("Health:",user_health,"/",total_health)
    print("1. Strength:", strength)
    print("2. Defense:", defense)
    print("3. Agility:", agility)
    print("4. Luck:", luck)
    stat = input("Which Stat would you like to distribute to(Type The Number): ")
    
    if stat == "1" or "2" or "3" or "4":
        print("This is your amount of available stat points:", stat_points)
        distribute = int(input("How much points do you want to distribute: "))
        if distribute <= stat_points and distribute > 0:
            if stat == "1":
                strength += distribute
            elif stat == "2":
                defense += distribute
            elif stat == "3":
                agility += distribute
            elif stat == "4":
                luck += distribute
        else:
            print("You dont have enough Stat Points")
            user_stats()
    else:
        print("Invalid Option")
        user_stats()
            

def inventory():
    print("1. Gold:",gold)
    print("2. Heal Potions:",potion)
    print("3. Heal Potions V2:", super_potion)
    print("4. Heal Potions V3:", ultra_potion)
    print()
    print("1. Inspect")
    print("2. Go Back")
    inv_action = input("Choose a Number: ")

    if inv_action == "1":
        inspect = input("Choose the number of the item to inspect: ")
        if inspect == "1":
            print("Gold Can Be Used At The Kingdom")
        elif inspect == "2":
            print("This Potion Can Be Used to Heal 50 HP")
        elif inspect == '3':
            print("This Potion Can Be used to Heal 200 HP")
        elif inspect == "4":
            print("This Potion Can Be Used to Heal 600 HP")
    elif inv_action == "2":
        user_action()


def user_action():
    print("You are in the", user_location)
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
    elif action == "2":
        user_move()
    elif action == "3":
        user_stats()
    


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
                print("You gained 15 stat points!")

       

    elif user_area_action == "2":
        print()



def area2():
    print()



print("""
This is a game where you will have to travel, defeat monsters and gain stat points to defeat the destruction warlord.

You will gain an Amount of stat points to distribute to your character after defeating a monster.

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


