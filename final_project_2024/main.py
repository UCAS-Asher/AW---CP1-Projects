#Asher Wangia, FINAL: Implementation

one = "Isle of Dragons(1)"
two = "Salamander Mountain(2)"
three = "Dark Goblin Forest(3)"
four = "Enchanted Forest(4)"
five = "Kingdom of Abal(5)"
six = "Goblin Forest(6)"
seven = "Demon Wasteland(7)"
eight = "Destruction Warlord(8)"
nine = "Ancient Forest(9)"

game_won = False 

user_location = one

user_health = 100
defense = 0
agility = 0
strength = 0
luck = 0

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
    
def area1():
    print("""
    Choose One of the Actions
        1. Fight the Dragon
        2. Go Back
        """)
    user_area_action = input("Choose a Number: ")


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
    break


