#Asher Wangia, Character Creator

print("""This is a Character Creator!
      You Will Be Able to Make Your Own Fantasy Character with Stats""")

races = ["demon","elf","human", "half-demon", "half-elf"]
classes = ["assasin", "dark-assasin", "swordsman", "sword-master", "wizard", "tank"]

health = 100

strength = 10

dexterity = 5

intelligence = 10

name = input("What do you want to Name your Character: ")

print(races)
race = input("Choose from the List Of Races: ")

print(classes)
char_class = input("Choose a Class from the list: ")

if race == "demon":
    health = health + 200
    stength = strength + 100
    dexterity = dexterity + 5
    intelligence = intelligence - 2
elif race == "elf":
    health = health + 50
    strength = strength + 50
    dexterity = dexterity + 20
    intelligence = intelligence + 100
elif race == "human":
    pass
elif race == "half-demon":
    health = health + 160
    strength = strength + 110
    dexterity = dexterity + 15
    intelligence = intelligence + 50
elif race == "half-elf":
    health = health + 75
    strength = strength + 75
    dexterity = dexterity + 25
    intelligence = intelligence + 110
else:
    print("Invalid Race!")


if char_class == "assasin":
    dexterity +=100
    intelligence +=50
    health -=20
    strength +=30
elif char_class == "dark-assasin":
    dexterity +=200
    intelligence +=150
    health -=75
    strength +=150
elif char_class == "swordsman":
    health += 50
    strength +=100
    dexterity += 30
    intelligence +=20
elif char_class == "sword-master":
    health +=75
    strength +=150
    dexterity += 75
    intelligence +=40
elif char_class == "wizard":
    health -=50
    strength -=20
    dexterity += 50
    intelligence += 300
elif char_class == "tank":
    health +=300
    strength +=200
    dexterity -=10
    intelligence -=10
else:
    print("Invalid Class!")





print("This is your Character")
print("Name: ",name,)
print("Race: ", race)
print("Class: ",char_class)
print("Health: ",health,)
print("Strength: ",strength,)
print("Dexterity: ",dexterity,)
print("Intelligence: ",intelligence)
