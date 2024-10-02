#Asher Wangia, Secret Cypher

message = input("What Is The Message You Want To Encode: ")
shifts = int(input("How Many Places Do you Want To Shift: "))

def convert(message,shifts):
    converted = ""
   
    for a in range(len(message)):
        char = message[a]

        if char==" ":
            converted+=" "
        elif (char.isupper()):
            converted += chr((ord(char) + shifts-65) + 65)
        else:
            converted += chr((ord(char) + shifts-97) + 97)
    
    return converted

print("Original Message : " + message)
print("Amount Of Shifts : " + str(shifts))
print("Secret Message : " + convert(message,shifts))
print("Your Message Has Been Encoded")