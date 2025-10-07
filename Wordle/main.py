import random
import ui
import os
from collections import Counter
from util import Color, Score


def load_words(filepath: str) -> list:
    with open(filepath, "r") as poss_file:
        content = poss_file.readlines()
        return [item.rstrip() for item in content]


def load_valid(filepath: str) -> set:
    with open(filepath, "r") as valid_file:
        content = valid_file.readlines()
        return set([item.rstrip() for item in content])

def validate_guess(guess: str, valid: set) -> bool:
    if len(guess) != 5:
        print("Please enter a 5-letter word")
        return False
    if guess not in valid:
        print(f"{guess} is an unknown word")
        return False
    return True


def check_letters(word: str, guess: str) -> list:
    # To handle duplicates
    occur = Counter(word)

    # Check guess by letter
    result = [None] * len(word)
    for i in range(len(guess)):
        if guess[i] == word[i]:  # If guess at current position
            result[i] = (guess[i], Color.GREEN)  # Green
            occur[guess[i]] -= 1

    for i in range(len(guess)):
        if result[i]: continue

        if guess[i] != word[i] and occur[guess[i]] > 0:  # If guess in word and not at current position
            result[i] = (guess[i], Color.YELLOW)  # Yellow
            occur[guess[i]] -= 1
        else:
            result[i] = (guess[i], Color.GRAY)  # Else guess not present, gray

    return result


valid_guesses = load_valid("data/valid_guesses.txt") # all valid 5 letter guesses
possible_words = load_words("data/possible_words.txt") # possible wordles


while True:
    user_score = Score("data/score.txt")
    op = ui.start_menu(user_score)
    if op == 1:
        # Initialise game variables
        rand_word = random.choice(possible_words)
        guesses = 6
        past_guesses = []
        while guesses >= 0:
            os.system('cls')
            ui.display_guesses(past_guesses)
            if guesses == 0:
                print("You've run of guesses!")
                print("The correct answer was:", rand_word)
                input()
                break

            user_guess = input("Enter your guess: ").lower()
            if not validate_guess(user_guess, valid_guesses):
                input()
                continue

            guess_result = check_letters(rand_word, user_guess)
            past_guesses.append(guess_result)

            is_correct = all(result[1] == Color.GREEN for result in guess_result)
            if is_correct:
                os.system('cls')
                ui.display_guesses(past_guesses)
                user_score.increment()
                print("Correct!")
                input()
                break

            guesses -= 1

    elif op == 3:
        print("Exiting...")
        break
