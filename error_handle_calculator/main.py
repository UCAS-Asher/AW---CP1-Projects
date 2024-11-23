#Asher Wangia,  Error Handling Calculator
num = False
is_num = False

while num == False:
    try:
        num1 = int(input("Type a number: "))
        operation = input(""" 
        + is for addition
        - is for subtraction
        * is for multiplication
        / is for division
        ** is for exponents
        // is for floor division
        % is for modulus
        What Operation Do you want to do: """)
    
        
        num2 = int(input("Type a 2nd number: "))
        is_num = True
    except:
        print("Try Again")
        continue
    
    if is_num == True:
        if num1 != 0 and num2 != 0:
            num = True
        else:
            print("Numbers cant be zero")
            continue
    else:
        continue


if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
elif operation == "**":
    print(num1**num2)
elif operation == "//":
    print(num1//num2)
elif operation == "%":
    print(num1%num2)
