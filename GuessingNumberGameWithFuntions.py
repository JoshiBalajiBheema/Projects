import random
import sys


def play_again():
    playAgain = input("Do you want to play again? (yes or no) : ").lower()
    if playAgain == "yes":
        game_start()
    else:
        print(f"Thanks for playing, {player_name}.")
        end_code()


def game_start():
    guesses = 1
    guess_limit = 10
    print(f"Game Starts Now! You have {guess_limit} guesses.")
    rand_num = random.randint(0, 20)
    while guesses <= guess_limit:
        if command == 'yes':
            player_guess = int(input(f'[#{guesses} Guess] : '))
            guesses = guesses + 1
            # print(rand_num)
            if player_guess == rand_num:
                print(f"Voila!!, You have guessed it right, within {guesses - 1} guesses.")
                play_again()
            elif player_guess < rand_num:
                print("Too Low, Guess again")
            elif player_guess > rand_num:
                print("Too High, Guess again")
            else:
                print(f"Thanks for playing, {player_name}.")
        else:
            print('Invalid Inputs')
    print(f"Out of guesses, The number was {rand_num}")
    play_again()


def end_code():
    sys.exit()


if __name__ == "__main__":
    print("Lets play a game. You have to guess the number that the computer thought of.")
    player_name = input("Enter your name : ").capitalize()
    command = input(f"Computer : Hello {player_name} : Lets play!!, Shall we? (yes/no) : ").lower()
    print(f'Okay {player_name}, I have thought of a 2-DIGIT number between (0-20), Lets see if you can guess it.')
    game_start()
