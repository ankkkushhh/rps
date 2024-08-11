import random

# options and exit
player_options = ("rock", "paper", "scissor", "exit")
computer_options = ("rock", "paper", "scissor")

# assign variables
player = None
computer= random.choice(computer_options)

player_points = 0
computer_points = 0

#  game start
print("WELCOME TO RPS\nto exit type: exit")


print("choose \n - rock \n - papers \n - scissors")

while player not in player_options:
    player = (input ("enter a choice: "))
    
print(f"player : {player}")
print(f"Computer : {computer}")

while player != "exit":    
    if player == computer:
        player_points += 0
        computer_points += 0
        print("It's a tie!")
        print(f"player points: {player_points}")
        print(f"computer points: {computer_points}")
        print("--------------------")
    elif player == "rock" and computer == "scissor":
        player_points += 1
        print("player wins!")
        print(f"player points: {player_points}")
        print(f"computer points: {computer_points}")
        print("--------------------")
    elif player == "paper" and computer == "rock":
        player_points += 1
        print("player wins!")
        print(f"player points: {player_points}")
        print(f"computer points: {computer_points}")
        print("--------------------")
    elif player == "scissor" and computer == "paper":
        player_points += 1
        print("player wins!")
        print(f"player points: {player_points}")
        print(f"computer points: {computer_points}")
        print("--------------------")
    else:
        computer_points += 1
        print("Computer wins!") 
        print(f"player points: {player_points}")
        print(f"computer points: {computer_points}")
        print("--------------------")
        
    player = None
    
    while player not in player_options:
        player = (input ("enter a choice: "))
    
    computer = random.choice(computer_options)
    
    print(f"player : {player}")
    print(f"Computer : {computer}")

print("Thanks for playing!")
print(f"player points: {player_points}")
print(f"computer points: {computer_points}")
if (player_points > computer_points):
    print("player wins!")
elif (player_points < computer_points):
    print("computer wins!")
else:
    print("It's a tie!")
   
    
    
        