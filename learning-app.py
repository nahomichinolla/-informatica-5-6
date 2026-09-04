import random
def main():
    #App Name
    print("Addition App⭐")
    print("Welcome!")
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    correctanswer = num1 + num2

    print(f"What is {num1} + {num2}?")
    answer = int(input("Your answer: "))
    if answer == correctanswer:
        print("Correct!")
        streak += 1
        print("Streak:", "⭐"*streak)
    







if __name__ == "__main__":
    main()
