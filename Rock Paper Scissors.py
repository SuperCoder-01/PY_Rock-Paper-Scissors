from random import randint
userWins = 0
compWins = 0
options = [
    {
        "name": "rock",
        "beats": "scissors",
        "beaten by": "paper"
    },
    {
        "name": "paper",
        "beats": "rock",
        "beaten by": "scissors"
    },
    {
        "name": "scissors",
        "beats": "paper",
        "beaten by": "rock"
    },
    "rock",
    "paper",
    "scissors"
]

# Main game loop
while True:
    userInput = input("Rock / Paper / Scissors? (Press 'q' to quit): ").lower()
    if userInput == 'q':
        break
    if userInput not in options:
        continue
    compChoice = options[randint(0, 2)]
    compChoiceName = compChoice["name"]
    print(f"Computer picked {compChoiceName}.")

    # Checks who win
    if userInput == compChoice["beaten by"]:
        print("You won!")
        userWins += 1
    elif userInput == compChoiceName:
        print("Its a draw!")
    else:
        print("You lost!")
        compWins += 1

print(f"You won {userWins} time(s) and the computer won {compWins} time(s).")
