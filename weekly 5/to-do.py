def main():
    tasks = []
    answer = ""

    while answer != exit:
        print("Wat would you ike to do today?")
        answer = input("add, remove, complete, exit\n: ").strip().lower()

        if answer == "add":
            print(tasks)
            add = input("what would you like to add to your list? ")
            where = int(input("what position? "))
            where -= 1
            tasks.insert(where, add)
            print("Item added")
        elif answer == "remove":
            print(tasks)
            remove = input("What are you removing? ")
            tasks.remove(remove)
            print("Item Removed")
        elif answer == "complete":
            tasks.clear
            print("You have completed all items")
        elif answer == "exit":
            break

        print("tasks")




if __name__ == "__main__":
    main()
