def main() :
    print("Welcome to Froyo!")

    rating = int(input("Rank our service: "))

    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("Poor")

    print("Thank You!")

if __name__ == "__main__":
    main()
