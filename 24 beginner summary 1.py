# 1. Variables and Data Types
tasks = []  # List to store tasks
task_status = {}  # Dictionary to store task status (e.g., "pending", "done")

# 2. Numbers (for task indexing)
next_task_id = 1

# 3. Strings (for task descriptions and user input)
def add_task(description):
    global next_task_id
    task_id = next_task_id
    tasks.append(description)
    task_status[task_id] = "pending"
    next_task_id += 1
    print(f"Task {task_id} added: '{description}'")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    print("\n--- Task List ---")
    for i, task in enumerate(tasks):
        task_id = i + 1
        status = task_status.get(task_id, "unknown")
        print(f"{task_id}. [{status.upper()}] {task}")
    print("-------------------\n")

# 12. Functions (Defining and Calling), 13. Function Arguments and Return Values
def mark_task_done(task_id_str):
    # 2. Numbers, 3. Strings, 10. Conditional Statements
    if not task_id_str.isdigit():
        print("Invalid task ID. Please enter a number.")
        return
    task_id = int(task_id_str)
    # 4. Lists (indexing), 6. Dictionaries (key access)
    if 1 <= task_id <= len(tasks):
        if task_id in task_status:
            task_status[task_id] = "done"
            print(f"Task {task_id} marked as done.")
        else:
            print(f"Task {task_id} not found in status.")
    else:
        print(f"Task with ID {task_id} does not exist.")

# 10. Loops (while loop), 19. String Formatting (f-strings), 9. Input and Output
while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # 09. Conditional Statements (if, elif, else)
    if choice == '1':
        # 8. Input and Output
        task_description = input("Enter the task description: ")
        add_task(task_description)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_id_input = input("Enter the ID of the task to mark as done: ")
        mark_task_done(task_id_input)
    elif choice == '4':
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        # 3. Strings
        print("Invalid choice. Please enter a number between 1 and 4.")

# 3. Tuples (not directly used in core logic, but could be used for menu options if desired)
menu_options = ("Add Task", "View Tasks", "Mark Done", "Exit")