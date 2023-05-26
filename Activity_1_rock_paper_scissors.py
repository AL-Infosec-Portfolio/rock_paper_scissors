# start of game message
print("Welcome to the Rock-Paper-Scissors game!")
print()

# ask two players to enter name
playerOne = input("Enter Name Of Player One: ").upper()
playerTwo = input ("Enter Name Of Player Two: ").upper()
print()

# ask both to enter their choice
playerOneChoice = input("Player One enter your choice of rock, paper or scissors: ").lower()
playerTwoChoice = input("Player Two enter your choice of rock, paper or scissors: ").lower()
print()

# control structure, selection, to compare the two players choice to see who wins
if playerOneChoice == playerTwoChoice:
    print("Both players entered the same choice.")
elif playerOneChoice == "rock" and playerTwoChoice == "paper":
    print(playerTwo + " won that round!")
elif playerOneChoice == "rock" and playerTwoChoice == "scissors":
    print(playerOne + " won that round!")
elif playerOneChoice == "paper" and playerTwoChoice == "rock":
    print(playerOne + " won that round!")
elif playerOneChoice == "paper" and playerTwoChoice == "scissors":
    print(playerTwo + " won that round!")
elif playerOneChoice == "scissors" and playerTwoChoice == "rock":
    print(playerTwo + " won that round!")
elif playerOneChoice == "scissors" and playerTwoChoice == "paper":
    print(playerOne + " won that round!")
else:
    # an incorrect choice was entered
    print("An inappropriate choice was entered by a player.")
    print("Choices must be either rock, paper or scissors. Try again.")

print()
# end of game message
print("Thank You For Playing!")

