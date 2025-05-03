#Rock , Paper and Scissor Game

import random

options = ["rock","paper","scissor"];
print("Welcome to rock,paper and scissor game!")

while True:
 computer = random.choice(options);
 player = None;

 while player not in options:
    player = input("Enter a choice (rock,paper and scissor):");
    print(f"Computer:{computer}");
    print(f"Player:{player}");
    if player==computer :
        print("Game Draw!!!");
    elif player=="rock" and computer=="scissor" :
        print("Player won!");
    elif player=="scissor" and computer=="paper" :
        print("Player won!");
    elif player=="paper" and computer=="rock" :
        print("Player won!");
    else:
        print("Computer won!");
 
 play = input("Play Again?(y/n): ");
 if play== 'n':
    break;

print("Thank you for playing!!!");

