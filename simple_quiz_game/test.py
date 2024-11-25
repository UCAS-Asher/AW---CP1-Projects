import random

quiz_a = True
question_num = 0

while quiz_a == True:
    num1 = random.choice(range(20,30,2))
    num2 = random.choice(range(25,35))
    question_num =+1
    answ1 = (num1*num2)-11
    answ2 = num1*num2
    answ3 = (num1*num2)-5
    answ4 = (num1*num2)+7
    questions = [answ1,answ2,answ3,answ4]
    a = random.choice(questions)
    b = random.choice(questions)
    c = random.choice(questions)
    d = random.choice(questions)
    
    print("Question",question_num, "What is", num1, "times", num2,"?")
    
    print("A.", a)
    print("B.", b)
    print("C.", c)
    print("D", d)
