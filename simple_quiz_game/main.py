#Asher Wangia, Simple Quiz Game
import random
quiz = True
quiz_a = True
quiz_b = False
quiz_c = False
quiz_d = False

question_num = 0
user_score = 0

while quiz == True:
  
    
    while quiz_a == True:
        if question_num >= 5:
            quiz_a = False
            print("Your Score was", (user_score/5)*100,"% or", user_score,"out of 5")
            break
        
        num1 = random.choice(range(20,30,2))
        num2 = random.choice(range(25,35))
        question_num +=1
    
        answ1 = (num1*num2)-11
        answ2 = num1*num2
        answ3 = (num1*num2)-5
        answ4 = (num1*num2)+7
    
        questions = [answ1,answ2,answ3,answ4]
    
        a = random.choice(questions)
        questions.remove(a)
    
        b = random.choice(questions)
        questions.remove(b)

        c = random.choice(questions)
        questions.remove(c)

        d = random.choice(questions)
        questions.remove(d)

        print("Question",question_num, "What is", num1, "times", num2,"?")
        
        print("A.", a)
        print("B.", b)
        print("C.", c)
        print("D", d)
        
        user_answer = input("Choose from the options: ")

        if user_answer == "A":
            if a == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_a = False
                quiz_b = True
        elif user_answer == "B":
            if b == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_a = False
                quiz_b = True
        elif user_answer == "C":
            if c == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_a = False
                quiz_b = True
        elif user_answer == "D":
            if d == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_a = False
                quiz_b = True
        


        
    while quiz_b == True:
        if question_num >= 5:
            quiz_b = False
            print("Your Score was", (user_score/5)*100,"% or", user_score,"out of 5")
            break
        
        num1 = random.choice(range(10,15,2))
        num2 = random.choice(range(15,20))
        question_num +=1
        
        answ1 = (num1*num2)-11
        answ2 = num1*num2
        answ3 = (num1*num2)-5
        answ4 = (num1*num2)+7
        
        questions = [answ1,answ2,answ3,answ4]
        
        a = random.choice(questions)
        questions.remove(a)

        b = random.choice(questions)
        questions.remove(b)

        c = random.choice(questions)
        questions.remove(c)

        d = random.choice(questions)
        questions.remove(d)

        print("Question",question_num, "What is", num1, "times", num2,"?")
        
        print("A.", a)
        print("B.", b)
        print("C.", c)
        print("D", d)
        
        user_answer = input("Choose from the options: ")

        if user_answer == "A":
            if a == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_b = False
                quiz_c = True
        elif user_answer == "B":
            if b == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_b = False
                quiz_c = True
        elif user_answer == "C":
            if c == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_b = False
                quiz_c = True
        elif user_answer == "D":
            if d == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_b = False
                quiz_c = True
        



    while quiz_c == True:
        if question_num >= 5:
            quiz_c = False
            print("Your Score was", (user_score/5)*100,"% or", user_score,"out of 5")
            break
        
        num1 = random.choice(range(5,10,2))
        num2 = random.choice(range(10,15))
        question_num +=1
        
        answ1 = (num1*num2)-11
        answ2 = num1*num2
        answ3 = (num1*num2)-5
        answ4 = (num1*num2)+7
        
        questions = [answ1,answ2,answ3,answ4]
        
        a = random.choice(questions)
        questions.remove(a)

        b = random.choice(questions)
        questions.remove(b)

        c = random.choice(questions)
        questions.remove(c)

        d = random.choice(questions)
        questions.remove(d)

        print("Question",question_num, "What is", num1, "times", num2,"?")
        
        print("A.", a)
        print("B.", b)
        print("C.", c)
        print("D", d)
        
        user_answer = input("Choose from the options: ")
        
        if user_answer == "A":
            if a == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_c = False
                quiz_d = True
        elif user_answer == "B":
            if b == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_c = False
                quiz_d = True
        elif user_answer == "C":
            if c == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_c = False
                quiz_d = True
        elif user_answer == "D":
            if d == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                quiz_c = False
                quiz_d = True


    while quiz_d == True:
        if question_num >= 5:
            quiz_d = False
            print("Your Score was", (user_score/5)*100,"% or", user_score,"out of 5")
            break
        
        num1 = random.choice(range(0,5))
        num2 = random.choice(range(5,10))
        question_num +=1
        
        answ1 = (num1*num2)-11
        answ2 = num1*num2
        answ3 = (num1*num2)-5
        answ4 = (num1*num2)+7
        
        questions = [answ1,answ2,answ3,answ4]
        
        a = random.choice(questions)
        questions.remove(a)

        b = random.choice(questions)
        questions.remove(b)

        c = random.choice(questions)
        questions.remove(c)

        d = random.choice(questions)
        questions.remove(d)

        print("Question",question_num, "What is", num1, "times", num2,"?")
        
        print("A.", a)
        print("B.", b)
        print("C.", c)
        print("D", d)
        
        user_answer = input("Choose from the options: ")

        if user_answer == "A":
            if a == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
        elif user_answer == "B":
            if b == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
        elif user_answer == "C":
            if c == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
        elif user_answer == "D":
            if d == num1*num2:
                user_score +=1
                print("Correct Answer")
            else:
                print("Wrong Answer")
        