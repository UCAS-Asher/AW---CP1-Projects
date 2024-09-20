#Asher Wangia, Simple Calculator

#What to type for an opperation

print("Type these for the operations:")

print("+ is for addition")

print("- is for subtraction")

print("* is for multiplication")

print("/ is for division")

print("** is for exponents")

print("// is for floor division")

print("% is for modulus")

print("== is for equal to")

print("!= is for not equal to")

print("> is for greater than")

print("< is for less than")

print(">= is for grater than or equal to")

print("<= is for less than or equal to")

print("abs if for absolute value")

print("round is for rounding")


#Inputs

num1 = float(input("Type your first number: "))

operation = (input("Type your operation: "))

num2 = float(input("Type your second number(0 if only one number): "))

  
#Operations Functioning

if operation == "+":
    print(num1+num2)
 
if operation == "-":
    print(num1-num2)

if operation == "*":
    print(num1*num2)

if operation == "/":
    print(num1/num2)

if operation == "**":
    print(num1**num2)

if operation == "//":
    print(num1//num2)

if operation == "%":
    print(num1%num2)

if operation == "==":
    print(num1==num2)

if operation == "!=":
    print(num1!=num2)

if operation == ">":
    print(num1>num2)

if operation == "<":
    print(num1<num2)

if operation == ">=":
    print(num1>=num2)

if operation == "<=":
    print(num1<=num2)

if operation == "abs":
    print(abs(num1))

if operation == "round":
    print(round(num1,int(num2)))