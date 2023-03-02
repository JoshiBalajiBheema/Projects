import random

game_on = True

print("Lets play a game."
      "You have to guess the number that the computer thought of.")
player_name = input("Enter your name : ").capitalize()
comp_number = input(f"Computer : Hello {player_name} : Lets play!!, Shall we? (yes/no) : ")
rand_num = random.randint(0, 20)

guesses = 0
print(f"Okay {player_name}, I have thought of a number, Lets see if you can guess it Correctly. ")
while game_on:
    if comp_number == 'yes':
        player_guess = int(input('Guess : '))
        guesses = guesses + 1

        if player_guess == rand_num:
            print("Voila!!, You have guessed it right.")
            playAgain = input("Do you want to play again? (yes or no) : ")
            if playAgain == "yes":
                rand_new = random.randint(0,20)
                print(rand_new)
            else:
                game_on = False
        elif player_guess < rand_num:
            print("Too Low, Guess again")
        elif player_guess > rand_num:
            print("Too High, Guess again")
    else:
        print(f"Thanks for playing, {player_name}.")
        game_on = False
