#Asher Wangia, Password Validator
pass_good = False
numbers = ["1","2","3","4","5","6","7","8","9","0"]
spec_char = ["@","#","$","%","*","&","!","?"]
while pass_good == False:
    password = input("Type a Password: ")
    
    if password != password[8:]:
        print("Password needs to be 8 characters Long")
        length = False
    else:
        length = True
        continue
    
    for x in numbers:
        num = True
        continue
    else:
         print("Password needs to have a Number")
        num = False

    if spec_char not in password:
        print("Password needs a Special Character")
        char = False
    else:
        char = True
        continue

    if length == True and num == True and char ==True:
        print("Your Password has been Accepted")
    else:
        password = input("Try a Diffrent Password: ")