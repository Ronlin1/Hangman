# Importing necessary modules that will help us in the game running
import random
from words import words
import string


# Getting Words that are valid from the words py file (module)
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


# Defining the game
def hangman():
    # from words get valid words
    word = get_valid_word(words)
    # get a set data type of that word per letter
    word_letters = set(word)
    # String formatting
    alphabet = set(string.ascii_uppercase)
    # a set for used letters by the guesser
    used_letters = set()
    # setting initial lives to 5 !
    lives = 5

    word_list = []
    # print(type(word))

    # A loop to keep us in the game if true;
    while len(word_letters) > 0 and lives > 0:
        # Initial display of the game at start
        print("You have ", lives, " lives left!! and used: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word list: ", '   '.join(word_list))

        # Get the input from user
        user_letter = input("Guess the letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # Remove letter if exists
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            # Otherwise deduct on their lives
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print("Oops! You have already used that letter! Try again!")
        else:
            print("Invalid Entry! Kindly Try Again with a letter!")

    # Loosing Side
    if lives == 0:
        print(f"Sorry You died! The Word was {word}")
    # Winning Side
    else:
        print(f'Yay Congs for guessing {word} correctly')


# calling the function

hangman()
