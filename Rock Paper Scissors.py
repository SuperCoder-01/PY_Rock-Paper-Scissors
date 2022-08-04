from random import randint
userWins = 0
compWins = 0
options = ["rock", "paper", "scissors"]

# Main game loop
while True:
    userInput = input("Rock/Paper/Scissors? (Press 'q' to quit): ").lower()
    if userInput == 'q':
        break
    if userInput not in options:
        continue
    compInput = options[randint(0, 2)] # rock = 0; paper = 1; scissors = 2
    print(f"Computer picked {compInput}.")

    # Checks who win
    if userInput == "rock" and compInput == "scissors" or userInput == "paper" and compInput == "rock" or userInput == "scissors" and compInput == "paper":
        print("You won!")
        userWins += 1
    elif userInput == compInput:
        print("Its a draw!")
    else:
        print("You lost!")
        compWins += 1

print(f"You won {userWins} time(s) and the computer won {compWins} time(s).")
print("Goodbye!")