#Asher Wangia, Area Calculator

area = ""

def square():
    global area
    width = float(input("What is your Width: "))
    length = float(input("What is your Length: "))
    area = width*length

def rectangle():
    global area
    width = float(input("What is your Width: "))
    length = float(input("What is your Length: "))
    area = width*length

def triangle():
    global area
    height = float(input("What is your Height: "))
    base = float(input("What is your Base: "))
    area = height*base/2

def circle():
    global area
    radius = float(input("What is your Radius: "))
    area = 3.14*radius**2.0

def trapezoid():
    global area
    base1 = float(input("What is your First Base: "))
    base2 = float(input("What is your Second Base: "))
    height = float(input("What is your Height: "))
    area = ((base1+base2)/2)*height

while True:

    action = input("""What would you like to calculate area of?

    Enter 1 for square

    Enter 2 for rectangle
                   
    Enter 3 for triangle
                   
    Enter 4 for circle
                
    Enter 5 for trapezoid
                   
    Enter 6 To End:\n""")

    if action =="1":
        square()
        print((area))
    

    elif action =="2":
        rectangle()
        print((area))

    elif action =="3":
        triangle()
        print((area))

    elif action =="4":
        circle()
        print((area))

    elif action =="5":
        trapezoid()
        print((area))

    else:
        print("Program End!")
        break