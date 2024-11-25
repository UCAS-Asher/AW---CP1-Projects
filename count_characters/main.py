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
f = 0
g = 0

for x in grid:
    for y in x:
        if y == "A":
            a +=1

print(num_char)