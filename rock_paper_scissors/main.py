#Asher Wangia, Rock, Paper, Scissors

import random


play = True
player_score = 0
cpu_score = 0
comp_choices = ["rock","paper","scissors"]

def cpu():
    global comp_choice
    comp_choice = random.choice(comp_choices)

while play == True:
    cpu()
print(comp_choice)