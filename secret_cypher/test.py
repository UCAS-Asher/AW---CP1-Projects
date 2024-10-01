def convert(plaintext,n):
    ans = ""
    
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

plaintext = input("Type Your Message Here: ")
plaintext = plaintext.lower
shifts = int(input("Amount of Shifts You Want: "))
print("Original Message : " + str(plaintext))
print("Amount of Shift Were : " + str(shifts))
print("Secret Message Is : " + convert(plaintext,shifts))