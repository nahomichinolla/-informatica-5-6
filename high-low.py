def main():
    def lower(a, b ,c):
        if a < b and a < c:
            lowest_num = a
        elif b < a and b < c:
            lowest_num = b
        else:
            lowest_num = c
    print(f"lowest number = {lowest_num}")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter a third number: "))
    lower(num1, num2, num3)


    def highest(a, b):
        if a > b:
            highest_num = a
        else:
            highest_num = b
        print("The highest number entered is", highest_num)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

   # highest(8,2)
    highest(num1, num2)


if __name__ == "__main__":
    main()

