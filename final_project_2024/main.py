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
game_over = False
user_location = one
user_health = 500
defense = 4
agility = 5
strength = 50
luck = 1
total_health = defense*10 + 100
stat_points = 0
areas = []

gold = 0
potion = 0
super_potion = 0
ultra_potion = 0



#Movement System
def user_move():
    global user_location
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



#Stats System
def user_stats():
    global strength
    global defense
    global agility
    global luck
    global stat_points
    
    print("STATS")
    print("Health:",user_health,"/",total_health)
    print("1. Strength:", strength)
    print("2. Defense:", defense)
    print("3. Agility:", agility)
    print("4. Luck:", luck)
    print("This is your amount of available stat points:", stat_points)
    
    stat_option = input("1 to distribute points or 2 to go back: ")
    
    if stat_option == "1":
        stat = input("Which Stat Do You Want To Distribute To?(Type The Number): ")
        
        if stat == "1" or stat == "2" or stat == "3" or stat == "4":
            distribute = int(input("How much points do you want to distribute: "))
            
            if distribute <= stat_points and distribute > 0:
                if stat == "1":
                    strength += distribute
                    stat_points -=distribute
                elif stat == "2":
                    defense += distribute
                    stat_points -= distribute
                elif stat == "3":
                    agility += distribute
                    stat_points -= distribute
                elif stat == "4":
                    luck += distribute
                    stat_points-= distribute
            else:
                print("You dont have enough Stat Points")
                user_stats()
        else:
            print("Invalid Choice")
            user_stats()
    elif stat_option == "2":
        user_action()
    else:
        print("Invalid Option")
        user_stats()



#Inventory System
def inventory():
    
    global user_health
    global potion
    global super_potion
    global ultra_potion
    
    
    print("INVENTORY")
    print("1. Gold:",gold)
    print("2. Heal Potions:",potion)
    print("3. Heal Potions V2:", super_potion)
    print("4. Heal Potions V3:", ultra_potion)
    print()
    print("Choices")
    print("1. Inspect")
    print("2. Go Back")
    print("3. Use Item")
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
        else:
            print("Invalid Item")
        inventory()
    elif inv_action == "2":
        user_action()
    elif inv_action == "3":
        use = input("Choose the number of the item to use: ")
        if use == "1":
            print("This item can only be used in the Kingdom")
        elif use == "2" and potion > 0:
            user_health += 50
            potion -=1
            if user_health > total_health:
                user_health = total_health
            print("You used a Potion")
        elif use == "3" and super_potion > 0:
            user_health += 200
            super_potion -=1
            if user_health > total_health:
                user_health = total_health
            print("You used a Potion V2")
        elif use == "4" and ultra_potion > 0:
            user_health += 600
            ultra_potion -=1
            if user_health > total_health:
                user_health = total_health
            print("You used a Potion V3")
        else:
            print("Invalid Option")
        inventory(user_health,potion,super_potion,ultra_potion)
    else:
        print("Invalid Action")
        inventory(user_health,potion,super_potion,ultra_potion)


#User Actions
def user_action():
    print("You are in the", user_location)
    print("You are at", user_health,"HP out of", total_health)
    print("""
Choose One of the Actions
    1. Explore the Area
    2. Go to a Diffrent Area      
    3. See Stats
    4. See Inventory 
          """)
    action = input("Choose a Number: ")

    if action == "1":
        if user_location == one:
            area1()
    elif action == "2":
        user_move()
    elif action == "3":
        user_stats()
    elif action == "4":
        inventory()


#Isle of Dragons
def area1():
    global stat_points
    global user_health
    global gold
    global super_potion
    print("""
Choose One of the Actions
    1. Fight the Dragon
    2. Go Back
        """)
    user_area_action = input("Choose a Number: ")

    if user_area_action == "1":
        dragon_hp = 1500
        while dragon_hp > 0:
            combat_action = input("Choose 1 to attack or 2 to flee: ")
            if combat_action == "1":
                dragon_hp -= strength * 10
                print("The dragon is at", dragon_hp, "HP now")
                monster_attack = random.choice(range(agility*2))
                if monster_attack == 1:
                    user_health -=100
                    print("The Dragon Landed An Attack")
                if user_health < 1:
                    game_over == True
                    print("Game Over You Died!")
                    break
            elif combat_action == "2":
                break
        if dragon_hp <= 0:    
            print("The Dragon was Defeated!")
            print("You gained 15 stat points and some Gold!")
            stat_points += 15
            gold += 500
            gold+= luck*100
            loot_drop = random.choice(range(100))
            if loot_drop >= 90:
                super_potion +=2
                print("You got 2 Heal Potions V2")
            elif loot_drop < 90:
                super_potion +=1
                print("You got a Heal Potion V2")
    elif user_area_action == "2":
        pass

#Game Running

print("""
      
This is a game where you will have to travel, defeat monsters and gain stat points to defeat the destruction warlord.

You will gain an Amount of stat points to distribute to your character after defeating a monster.

You can buy equipment from merchants with gold and it can be used to boost your stats.

Agility Stats boost your chances of dodging monster attacks, Strength boosts your damage output, Luck boost your loot drops and Defense boosts your Max HP.
                        """)


while game_won == False and game_over == False:

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

    if user_health < 1:
        game_over = True

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
            








