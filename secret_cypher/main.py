#Asher Wangia, Secret Cypher

print("This Will Translate Your Message To A Secret Code")

string = input("What is your message: ").lower

shifts = int(input("How many places will you shift:"))
def char(string, firstletter):
    if string.isalpha():
        firstletter = "a"
        old = ord(string) - ord(firstletter)
        new = (old + shifts)
        return chr(new + ord(firstletter))
    return string


def cypher(string, shifts):
    cipher = " "
    cipher+= char(string, shifts)
    return cipher
cipher = cypher(string, shifts)
print(f"Cipher: {cipher}")