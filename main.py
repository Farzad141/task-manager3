print("Hello Task Manager")

tasks = []

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(i, t)

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid option")