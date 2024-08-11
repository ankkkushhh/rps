
import random

options = ("rock", "paper", "scissor")
player= None
computer= random.choice(options)

while player not in options:
    player = (input ("Enter a choice- "))

print(f"player : {player}")
print(f"Computer : {computer}")

if player==computer:
    print("Tie")
elif player == "rock" and computer == "scissor":
    print("You win")
elif player== "scissor" and computer== "paper":
    print("You win")
elif player== "paper" and computer== "rock":
    print("You win")
else:
    print("You LOSE")
