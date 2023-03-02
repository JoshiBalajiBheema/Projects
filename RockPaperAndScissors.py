import random

YOU = input("Select Rock, Paper, or Scissor :").lower()
Computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Computer Chose: ", Computer)
choice = 'rock, paper, scissor'
if YOU not in choice:
    print("Check what you typed, CHOICES ARE [ ROCK, PAPER, SCISSOR ]")

if YOU == "rock" and Computer == "paper" or YOU == "paper" and Computer == "scissor" or YOU == "scissor" and Computer == "rock":
    print("COMPUTER WON, YOU LOST.")
elif YOU == Computer:
    print("Tie")
else:
    print("YOU WON, COMPUTER LOST.")
