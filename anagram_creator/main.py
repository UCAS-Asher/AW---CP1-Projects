#Asher Wangia, Anagram Creator

import random

word = input("What is your word: ")

def anagram(word):
    random_word = list(word)
    random.shuffle(random_word)
    newword = ''.join(random_word)
    return newword

newword = anagram(word)
print("This is your original word:", word)
print("These next word are your anagrams")
print(newword)
print(newword)
print(newword)
print(newword)
print(newword)
  