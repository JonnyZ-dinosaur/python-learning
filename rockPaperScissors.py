import random 

choices = ["rock","paper","scissors"]
player = 0 
comp = 0 

def computerChoice():
    intChoice = random.randint(0,2)
    compChoice = 0
    if intChoice == 0: 
        compChoice = "rock"
    elif intChoice == 1:
        compChoice = "paper" 
    else:
        compChoice = "scissors"
    return compChoice


def checkWin(playerC, compC):
    if playerC == compC:
        return "Tie"
    if playerC == "rock":
        if compC == "paper":
            return "Computer"
        elif compC == "scissors":
            return "Player"
    elif playerC == "scissors":
        if compC == "paper":
            return "Player"
        else:
            return "Computer"
    elif playerC == "paper":
        if compC == "scissors":
            return "Computer"
        else:
            return "Player"

round = 1

while comp < 3 and player < 3: 
    while True: 
        choice = input("Please choose an option: rock, paper or scissors.\n")
        choice = choice.lower()
        if choice in choices:
            print("Your choice is", choice)
            break
        else:
            print("No available option, please try again")
    print("Round", round)
    round += 1 

    computer_input = computerChoice()
    print("Computer selected:", computer_input)

    if checkWin(choice, computer_input) == "Computer":
        comp += 1 
    elif checkWin(choice, computer_input) == "Player":
        player += 1 

    print("computer - player: ", comp,  "-", player)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

if comp == 3:
    print(f"Computer Won, You lose \n Final Score: computer: {comp} : player: {player}")
else:
    print(f"You Win, Computer lost \n Final Score: computer: {comp} : player: {player}")


        



    
















 
        
