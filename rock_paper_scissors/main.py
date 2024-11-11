#Asher Wangia, Rock, Paper, Scissors

import random


play = True
player_score = 0
cpu_score = 0
cpu_choices = ["rock","paper","scissors"]

def cpu():
    global cpu_choice
    cpu_choice = random.choice(cpu_choices)
while play == True:
    print(cpu())
print(cpu_choice)