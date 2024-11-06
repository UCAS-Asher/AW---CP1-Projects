#Asher Wangia, Authorized

reg_users =["Jake","Rob","Nate","Victor","Tate","Jim","Tim","Mike"]

users = ["Jake","Rob","Nate","Ray","Victor","Tate","Jim","Tim","Mike","Jay","Bart"]

admin = users[3]

while True:
    print("These are the users you can choose from.")
    print(users)
    choice_user = input("Type in a user from the list: ")
    
    if choice_user in admin:
        print("Hello Admin", choice_user, "Welcome to the Program")
    elif choice_user in reg_users:
        print("Nice to meet you User", choice_user)
    else:
        print("You are Not AUTHORIZED!", choice_user)