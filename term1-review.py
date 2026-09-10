from datetime import datetime
def main():
    day = day = datetime.now().weekday()
    print(day)
    if day < 4:
        print("Its a weekday")
        remaining =  5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("Its a Friday")
        print("Just a day left until the weekend")
    else:
        print("Its the weekend!")

if __name__ == "__main__":
    main()

