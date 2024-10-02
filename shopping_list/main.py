#Asher Wangia, Shopping list manager

shoplist = []

def add(shoplist):
    shoplist = shoplist,input("Add to the list: ")
    return shoplist

def removelist(shoplist):
    delete = input("What do you want to remove: ")
    if delete in shoplist:
        shoplist.remove(shoplist)
    return shoplist



while True:

    action = input("""What would you like to do?

    Enter 1 to add item

    Enter 2 to remove an item
                   
    Enter 3 to finish the list:\n""")

    if action =="1":
        print(add(shoplist))

    elif action =="2":
        print(removelist(shoplist))

    else:
        print("Have a nice day!")
        print(shoplist)
        break