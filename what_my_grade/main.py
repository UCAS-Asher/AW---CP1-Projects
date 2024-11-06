#Asher Wangia, What is My Grade
print("This is a grade checker")
grade_check = True

while grade_check == True:
    choice = input("Are you done checking your grades yes or no: ")
    if choice == "yes":
        print("Have a nice day!")
        break
    else:
        class_name = input("What is Your Class Name: ")
        grade = float(input("What is your Grade in This Class: "))

        if grade >= 95:
            print("You have an A")
        elif grade < 95 and grade >= 90:
            print("You have an A-")
        elif grade < 90 and grade >= 87:
            print("You have a B+")
        elif grade < 87 and grade >= 85:
            print("You have a B")
        elif grade < 85 and grade >= 80:
            print("You have a B-")
        elif grade < 80 and grade >= 77:
            print("You have a C+")
        elif grade < 77 and grade >= 75:
            print("You have a C")
        elif grade < 75 and grade >= 70:
            print("You have a C-")
        elif grade < 70 and grade >= 67:
            print("You have a D+")
        elif grade < 67 and grade >= 65:
            print("You have a D")
        elif grade < 65 and grade >= 60:
            print("You have a D-")
        else:
            print("You have an F")