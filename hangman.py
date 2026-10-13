# Define the main Function
# Create a txt file for the bank of words
# Create and define a function called start_game
# Open the txt in the start_game function
# Welcome the user
# Ask for the first letter
import random
def main():
    start_game("words.txt")
def start_game(file):
    with open(file) as word_file:
        word = word_file.read().splitlines()
    print(random.choice(word))


if __name__ == "__main__":
    main()
