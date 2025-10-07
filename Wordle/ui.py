from util import Color
from time import sleep
import os

PADDING = 5
TICK = 0.2
title_str = r'''
 _    _               _ _      
| |  | |             | | |     
| |  | | ___  _ __ __| | | ___ 
| |/\| |/ _ \| '__/ _` | |/ _ \
\  /\  / (_) | | | (_| | |  __/
 \/  \/ \___/|_|  \__,_|_|\___|

'''

help_str = "Guess the wordle in 6 tries. \n> Each guess must be a valid 5-letter word \n> The color of " \
    "your tiles will change to show how close your guess was to the word.\n" + \
    f"> {Color.background(Color.GREEN)} Green {Color.reset()} to show letter is in the word and in the correct spot\n" + \
    f"> {Color.background(Color.YELLOW)} Yellow {Color.reset()} to show letter is in the word\n" + \
    f"> {Color.background(Color.GRAY)} Gray {Color.reset()} to show letter is not in the word"

def start_menu(score):
    actions = ["1. Start Game", "2. How do I play?", "3. Exit"]
    while True:
        os.system('cls')
        print(title_str)
        print("\n".join(actions))
        print(f"You've solved {score.score} wordles")
        choice = input("What would you like to do? (1-3): ")
        if choice == '2':
            print(help_str)
            input()
        elif choice == '1' or choice == '3':
            return int(choice)
        else:
            print("Unknown command! Try again")



def display_guesses(guesses: list):
    print(title_str)
    for i, guess_result in enumerate(guesses):
        print(" " * PADDING, end="")
        for k, v in guess_result:
            print(f"{Color.background(v) + Color.color_text(Color.WHITE)} {k} {Color.reset()} ", end="", flush=True)
            if i == len(guesses) - 1: sleep(TICK)
        print("\n")

    rem_guesses = 6 - len(guesses)
    for i in range(rem_guesses):
        print(" " * PADDING, end="")
        for _ in range(5):
            print(f"{Color.background(Color.BLACK)} _ {Color.reset()} ", end="")
        print("\n")
