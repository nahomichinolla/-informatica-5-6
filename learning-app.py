import random
def main():
    #App Name
    print("Addition App⭐")
    print("Welcome! Here you will learn math")
    print("Select your operation type")
    problem = input("(+)")
    streak = 0

    if problem == "+":
        while streak < 3:
            num1 = random.randint(10,90)
            num2 = random.randint(10,90)
            print("Solve: ")
            correct = num1 + num2
            answer = int(input(f"{num1} + {num2}: "))
            if answer != correct:
                streak = 0
                print(f"correct asnwer:{correct}")
                print(f"Streak:{streak}")
            elif answer == correct:
                print("Good job!")
                streak += 1
                print(f"streak:{streak}")

if __name__ == "__main__":
    main()
