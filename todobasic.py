quit = 0
tasks = []

def viewtask():
    print(f"List of tasks ({len(tasks)}): {tasks}")

def addTask(newtask):
    tasks.append(newtask)

def deletetask(i): 
    if 0 <= i < len(tasks):
        tasks.pop(i)
    else:
        print("Invalid task index!")

def edittask(i, edited):
    if 0 <= i < len(tasks):
        tasks[i] = edited
    else:
        print("Invalid task index!")

def deletelist():
    tasks.clear()

while quit == 0:
    print("\nWhat do you wish to do?")
    choice = input("1. Add task \t 2. Delete task \t 3. Edit task \t 4. List all \t 5. Delete all \t 6. Exit\n")
    
    if choice == '1':
        newtask = input("Enter the task you wish to add: ")
        addTask(newtask)
    elif choice == '2':
        try:
            taskno = int(input("Enter the task number (index) you wish to delete: "))
            deletetask(taskno)
        except ValueError:
            print("Please enter a valid number!")
    elif choice == '3':
        try:
            taskno = int(input("Enter the task number (index) you wish to edit: "))
            newtask = input("Enter the new task: ")
            edittask(taskno, newtask)
        except ValueError:
            print("Please enter a valid number!")
    elif choice == '4':
        viewtask()
    elif choice == '5':
        deletelist()
        print("All tasks deleted!")
    elif choice == '6':
        quit = 1
        print("Exiting...")
    else:
        print("Invalid choice! Please try again.")
