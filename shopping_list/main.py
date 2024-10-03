#Asher Wangia, Shopping list manager
shoplist = ""

def add():
    global shoplist
    shoplist.append(input("Add To List: "))

def removelist():
    global shoplist
    delete = input("What do you want to remove: ")
    if delete in shoplist:
        shoplist.remove(shoplist)
    else:
        print("Not in Shopping List")



while True:

    action = input("""What would you like to do?

    Enter 1 to add item

    Enter 2 to remove an item
                   
    Enter 3 to finish the list:\n""")

    if action =="1":
        add()
        print((shoplist))
    

    elif action =="2":
        removelist()
        print((shoplist))

    else:
        print("Have a nice day!")
        print((shoplist))
        break