def main():
    tasks = [] # Empy list
    command = ""

    while True:
        print(f"Tasks to do: {len(tasks)}")
        command = input("What d you want to do? (add, complete, ext): ")
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif command == "complete":
            completed_tasks = input("Completed tasks: ")
            tasks.remove(completed_task)
            print("Task completed")





if __name__ == "__main__":
    main()
