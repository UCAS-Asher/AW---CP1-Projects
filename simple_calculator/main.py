#Asher Wangia, Simple Calculator

num1 = float(input("Type your first number: "))

operation = (input("Type your operation: "))

num2 = float(input("Type your second number(0 if only one number): "))

if operation == "add":
    print(num1+num2)
 
if operation == "subtract":
    print(num1-num2)

if operation == "multiply":
    print(num1*num2)

if operation == "division":
    print(num1/num2)

if operation == "exponent":
    print(num1**num2)

if operation == "floor division":
    print(num1//num2)

if operation == "modulus":
    print(num1%num2)

if operation == "equal to":
    print(num1==num2)

if operation == "not equal to":
    print(num1!=num2)

if operation == "greater than":
    print(num1>num2)

if operation == "less than":
    print(num1<num2)

if operation == "greater than or equal to":
    print(num1>=num2)

if operation == "less than or equal to":
    print(num1<=num2)

if operation == "absolute value":
    print(abs(num1))

if operation == "round":
    print(round(num1,int(num2)))

if operation == "modulus":
    print(num1%num2)