# List to store tasks
tasks = []

# Functions for CRUD operations
#Add task
def add_task(tasks, task_name, description, priority, due_date):
    task = {
        'name': task_name,
        'description': description,
        'priority': priority,
        'due_date': due_date
    }
    tasks.append(task)
    print(f"Task '{task_name}' added successfully.")
    save_tasks_to_file(tasks, filename)  # Save tasks after adding

#view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    index = 1  
    for task in tasks:
        print(f"Task {index}:")
        print(f"  Name: {task['name']}")
        print(f"  Description: {task['description']}")
        print(f"  Priority: {task['priority']}")
        print(f"  Due Date: {task['due_date']}")
        print()
        index += 1  
#Update task
def update_task(tasks, task_index, new_task_name, new_description, new_priority, new_due_date):
    if 0 <= task_index < len(tasks):
        tasks[task_index].update({
            'name': new_task_name,
            'description': new_description,
            'priority': new_priority,
            'due_date': new_due_date
        })
        print(f"Task {task_index + 1} updated successfully.")
        save_tasks_to_file(tasks, filename)  # Save tasks after updating
    else:
        print("Invalid task index.")

#Delete a task
def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['name']}' deleted successfully.")
        save_tasks_to_file(tasks, filename)  # Save tasks after deleting
    else:
        print("Invalid task index.")

# File handling functions for loading and saving tasks
def load_tasks_from_file(filename, tasks):
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                name = parts[0].split(': ')[1]
                description = parts[1].split(': ')[1]
                priority = parts[2].split(': ')[1]
                due_date = parts[3].split(': ')[1]
                add_task(tasks, name, description, priority, due_date)
    except FileNotFoundError:
        # Create the file if it doesn't exist
        open(filename, 'w').close()  # Create an empty file

def save_tasks_to_file(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"Task Name: {task['name']}, Task Description: {task['description']}, Task Priority: {task['priority']}, Task Due Date: {task['due_date']}\n")

# Main program loop
filename = "tasks.txt"
load_tasks_from_file(filename, tasks)

while True:
    print("Task Management System")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    #User input
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        priority = input("Enter task priority (HIGH/MID/LOW): ")
        while priority != "HIGH" and priority != "MID" and priority != "LOW":
            priority = input("Invalid input. Enter task priority again (HIGH/MID/LOW): ")   
        due_date = input("Enter task due date (YYYY-MM-DD): ")
        while len(due_date) != 10:
            due_date = input("Invalid input. Enter due date again (YYYY-MM-DD): ")
        
        add_task(tasks, name, description, priority, due_date)

    elif choice == '2':
        view_tasks(tasks)

    elif choice == '3':
        #Error handling
        try:
            index = int(input("Enter task index to update (starting from 1): ")) - 1
            
            # Check if the index is valid
            if index < 0 or index >= len(tasks):
                print("Invalid task index. Please enter a number corresponding to an existing task.")
                continue 

            name = input("Enter new task name: ")
            description = input("Enter new task description: ")
            priority = input("Enter new task priority (HIGH/MID/LOW): ")
            while priority != "HIGH" and priority != "MID" and priority != "LOW":
                priority = input("Invalid input. Enter task priority again (HIGH/MID/LOW): ")
        
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            while len(due_date) != 10:
                due_date = input("Invalid input. Enter due date again (YYYY-MM-DD): ")
                
            update_task(tasks, index, name, description, priority, due_date)

        except ValueError:
            print("Invalid input. Please enter a valid integer for the task index.")

    elif choice == '4':
        #Error handling
        try:
            index = int(input("Enter task index to delete (starting from 1): ")) - 1
            delete_task(tasks, index)
        except ValueError:
            print("Invalid input. Please enter a valid integer for the task index.")

    elif choice == '5':
        print("Exiting the Task Management System.")
        break

    else:
        print("Invalid choice. Please try again.")