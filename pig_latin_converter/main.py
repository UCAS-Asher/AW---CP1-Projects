#Asher Wangia, Pig Latin Converter
word = str(input("What is your word you want to convert: "))

word = word.lower

def covert(word):
    if word[0] == ("a","e","o","u","i"):
        print(word,"ay")
    else:
        print((word - word[0])+"ay")