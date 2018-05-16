import random

player = input("Make your choice: (r)ock, (p)aper, or (s)cissors? ")
options = ['r','p','s']
computer = random.choice(options)

#Print player and computer selections
if(player == 'r'):
    print("Player chooses rock.")
elif(player == 'p'):
    print("Player chooses paper.")
elif(player == 's'):
    print("Player chooses scissors.")
else:
    print("Player chose invalid option.")

if(computer == 'r'):
    print("Computer chooses rock.")
elif(computer == 'p'):
    print("Computer chooses paper.")
elif(computer == 's'):
    print("Computer chooses scissors.")

#Determine winner
if((player in options) == False):
    print("Computer Wins!")
elif(player == computer):
    print("Stalemate!")
elif((player == 'r' and computer == 'p') or (player == 'p' and computer == 's') or (player == 's' and computer == 'r')):
    print("Computer Wins!")
else:
    print("Player Wins!")
