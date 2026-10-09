def main():
    def welcome():
        menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]

        print("Welcome to Fast Food!")
        print("Heres the menu: ")

        for i in range(len(menu)):
            print(f"{i + 1}. {menu[i]}")

    def get_item(item):
        if item == "1":
            print("🍔")
        elif item == "2":
            print("🍟")
        elif item == "3":
            print("🥤")
        elif item == "4":
            print("🍦")
        elif item == "5"





if __name__ == "__main__":
    main()
