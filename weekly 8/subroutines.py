def main():
    def calculate(a, b):
        answer = a + b
        print(f"{a} + {b} = {answer}")
    num1 = 10
    num2 = 15

    calculate(num1, num2)

    def average_value(a, b, c):
        answer = (a + b + c) / 3
        print(f"The average value is {round(answer , 1)}")

    num3 = float(input("Enter first nmber: "))
    num4 = float(input("Enter second nmber: "))
    num5 = float(input("Enter third nmber: "))

    average_value(num3, num4, num5)



if __name__ == "__main__":
    main()
