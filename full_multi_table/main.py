#Asher Wangia, Full Multiplication Table

num = 12

for row in range(1,13): 
    for collum in range(1,13): 
        print(f"{row * collum:4}", end =" ") 
    print() 