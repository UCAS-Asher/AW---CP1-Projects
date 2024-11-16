#Asher Wangia, Countdown Timer

import time

user_time = int(input("How long do you want a timer to run for in Seconds: "))

not_done = True

while not_done == True:
    time.sleep(1)
    print(user_time)
    user_time = user_time - 1
    if user_time < 0:
        print("Countdown Finished")
        not_done == False
        break