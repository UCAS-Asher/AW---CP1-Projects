#Asher Wangia, Password Validator
pass_good = False
spec_char = "!@#$%^&*()_-+=?/><"
length = False
num = False
char = False
while pass_good == False:
    password = input("Type a Password: ")
    
    
    if len(password) >= 8:
        length = True
    
    for character in password:
        if(character.isdigit()):
            num = True  
        if(not character.isalnum()):
            char = True

        char = True
    else:
        char = False
   
    # prints changes needed to be done
    if length == False:
        print("Password needs to be 8 Characters Long")
    if num == False:
        print("Password needs a Number")
    if char == False:
        print("Password needs a Special Character")
    
    # checks what is true 
    if length == True and num == True and char == True: 
        print("Password has met all of the Requirements")
        pass_good == True  