def main() :
    number = int(input("Enter an integer number: "))

    if number < 0:
        number = (number * -1)
    else:
        print(number)
    print(number)

if __name__ == "__main__":
    main()

