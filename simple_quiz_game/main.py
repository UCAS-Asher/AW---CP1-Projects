#Asher Wangia, Simple Quiz Game
import random

print("This is a Math Quiz For Multiplication")

quiz = True
user_score = 0
quiz_total = 5

while quiz == True:
    
    print("""Q1. 21 times 34
      A. 712
      B. 714
      C. 672
      D. 724""")
    
    user_answer = input("Choose from one of the Choices: ")
    
    if user_answer == "B":
        ("Correct Answer")
        user_score +=1
    else:
        print("Wrong Answer")
        
        print("""Q2. 12 times 11
        A. 132
        B. 112
        C. 121
        D. 143""")
        
        user_answer = input("Choose from one of the Choices: ")
        if user_answer == "A":
            user_score +=1

    print("""Q. 12 times 11
    A. 132
    B. 112
    C. 121
    D. 143""")
        
    user_answer = input("Choose from one of the Choices: ")




print("Your Score was", (user_score/quiz_total)*100,"% or", user_score,"out of 5")