#Asher Wangia, Counting characters

grid = [

['A', 'B', 'C', 'A', 'D'],

['C', 'A', 'B', 'D', 'E'],

['A', 'D', 'C', 'E', 'A'],

['B', 'A', 'C', 'A', 'D'],

['D', 'C', 'B', 'E', 'A'] ]

a = 0
b = 0
c = 0
d = 0
e = 0


for row in grid:
    for char in row:
        if char == "A":
            a +=1
        elif char == "B":
            b +=1
        elif char == "C":
            c +=1
        elif char == "D":
            d +=1
        elif char == "E":
            e +=1
        
print("A:", a)
print("B:", b)
print("C:", c)
print("D:", d)
print("E:", e)


        
    

