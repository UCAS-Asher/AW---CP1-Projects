#Asher Wangia, Simple Histogram

num_done = False

num_list = []

while num_done == False:

    number = input("Type a number: ")

    num_list.append((number))

    num_length = len(num_list)
    
    if num_list[5:]:
        choice = input("Do you want to stop Yes or No: ")
        if choice == "Yes":
            num_done = True


for num in num_list:
        print(num,"=","*"*int(num))