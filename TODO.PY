import os
import datetime
from tabulate import tabulate

# Function to validate priority input
def validate_priority(priority):
    priority = priority.lower()
    if priority not in ["h", "m", "l"]:
        raise ValueError("Invalid priority. Please enter 'H', 'M', or 'L'.")

# Function to validate due date input
def validate_due_date(due_date):
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

# Function to add a task to the to-do list
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority_input = input("Enter priority (H/M/L): ").lower()
    validate_priority(priority_input)
    priority_mapping = {"h": "High", "m": "Medium", "l": "Low"}
    priority = priority_mapping[priority_input]

    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        validate_due_date(due_date)
        tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})
        print("Task added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

# Function to remove a task from the to-do list
def remove_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    task_index = int(input("Enter the task index to remove: "))
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['name']}' removed successfully!")
    else:
        print("Invalid task index. No task removed!")

# Function to mark a task as completed
def mark_completed(tasks):
    if not tasks:
        print("No tasks found.")
        return

    task_index = int(input("Enter the task index to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index. No task marked as completed!")

# Function to display the to-do list
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        table = []
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            table.append([i, task['name'], task['priority'], task['due_date'], status])

        headers = ["Index", "Task Name", "Priority", "Due Date", "Status"]
        print(tabulate(table, headers, tablefmt="grid"))

# Function to display not completed tasks sorted by priority
def display_not_completed_sorted(tasks):
    not_completed_tasks = [task for task in tasks if not task["completed"]]
    if not not_completed_tasks:
        print("No not completed tasks found.")
    else:
        sorted_tasks = sorted(not_completed_tasks, key=lambda x: x["priority"])
        table = []
        for i, task in enumerate(sorted_tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            table.append([i, task['name'], task['priority'], task['due_date'], status])

        headers = ["Index", "Task Name", "Priority", "Due Date", "Status"]
        print(tabulate(table, headers, tablefmt="grid"))

# Function to save tasks to a file
def save_tasks_to_file(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['name']},{task['priority']},{task['due_date']},{task['completed']}\n")

# Function to load tasks from a file
def load_tasks_from_file(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(',')
                tasks.append({"name": task_data[0], "priority": task_data[1], "due_date": task_data[2], "completed": task_data[3] == "True"})
    return tasks

# Main function
def main():
    filename = "internship/1-coding-raja/tasks.txt"

    tasks = load_tasks_from_file(filename)

    while True:
        print("\nTo-Do List Application\n")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Show Not Completed Tasks Sorted by Priority")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            display_not_completed_sorted(tasks)
        elif choice == "6":
            save_tasks_to_file(tasks, filename)
            print("Exiting the application. Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
