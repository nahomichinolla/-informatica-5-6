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
    attempts = 10
    with open(file) as f:
        word_bank = f.read().splitlines()
    word = random.choice(word_bank)
    hint = ["_"] * len(word)
    incorrect_letters = []
    while attempts > 0:
        print("Current word:", " ".join(hint))
        while True:
            guess = input("Guess a leter: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess. Try again.")
        if guess in word and guess not in hint:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))
        else:
            attempts -=1
            print("Wrong guess! Attempts left:", str(attempts))
            if guess in word and guess not in hint:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")
        if "_" not in hint:
                print("Congratulations! 🥳 You guessed the word:", word)
                break
        if attempts == 0 and "_" in hint:
            print("No attempts left 💀 The word was:", word)
if __name__ == "__main__":
    main()
