import random

def main():
    print("Hello! What is your name? ")
    name = input("")
    print(f"Well, {name}, I a thinking of a number beween 1 and 100.")

    number = random.randint(1, 100)
    guess = 0 # Initialize

    while guess != number:
        guess = int(input("Take a gues: "))
        if guess > number:
            print("Your guess is to high.")
        elif guess < number:
            print("Your guess is to low. ")
    print(f"Good job, {name}! You guessed my number!")




if __name__ == "__main__":
    main()
