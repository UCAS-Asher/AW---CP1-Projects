#Asher Wangia, Graded Quiz

score = 0

question1 = int(input("What is 320 divided by 80: "))

question2 = int(input("What is 400 divided by 50: "))

question3 = int(input("What is 120 dived by 6: "))

question4 = int(input("What is 230 dived by 23: "))

question5 = int(input("What is 980 dived by 20: "))

correct1 = 4

correct2 = 8

correct3 = 20

correct4 = 10

correct5 = 49

if question1 == correct1:
    score += 1

if question2 == correct2:
        score += 1

if question3 == correct3:
      score += 1     

if question4 == correct4:
      score += 1

if question5 == correct5:
      score += 1

print("Your score was", score, "out of 5")