#Asher Wangia, What are these numbers?

number = float(input("What is your Number?: "))

comma = "This car is {:,} years old."

float = "The answer is to the math problem is {:.4f}."

percent = "You scored {:.2%} on the test."

dollar = "You have ${:.2f} in your bank account."


print(comma.format(number))
print(float.format(number))
print(percent.format(number))
print(dollar.format(number))
