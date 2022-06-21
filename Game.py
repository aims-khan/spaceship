import random

print("rock")
print("paper")
print("scissors")

player1 = input("Player 1 make your move: ")
#player2 = input("Player 2 make your move: ")

player2 = random.randint(0,2)

if player2 == 0:
    player2 = "rock"
elif player2 == 1:
    player2 = "paper"
elif player2 == 2:
    player2 = "scissors"
    
print("computer selected ==> " + player2)

if player1 == player2:
    print("it's a tie")
if player1=="rock": 
    if player2=="scissors":
        print("player 1 wins")
    elif player2 == "paper":
        print("player 2 wins")
elif player1 == "paper":
    if player2 == "scissors":
        print("player 2 wins")
    elif player2 == "rock":
        print("player 1 wins")

elif player1 == "scissors":
    if player2 == "paper":
        print("player 2 wins")
    elif player2 == "rock":
        print("player 1 wins")
else:
    print("something went wrong")
    
    
    
    #we have 3 concepts in programmin ahead:
    
        # 1. Statements
        # 2. Conditions
        # 3. Loops
        