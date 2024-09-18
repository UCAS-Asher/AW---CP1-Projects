#Asher Wangia, Palandrom

word = input("Type Your Word: ")

word = word.lower().strip()

word2 = word[::-1]

if word == word2:
     print("This is a palindrome")
else:

     print("This word isn't a palindrome") 