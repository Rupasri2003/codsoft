import json
import os

def load_todo_list():
    if os.path.exists('todo.json'):
        with open('todo.json', 'r') as file:
            return json.load(file)
    else:
        return []

def save_todo_list(todo_list):
    with open('todo.json', 'w') as file:
        json.dump(todo_list, file)

def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    save_todo_list(todo_list)
    print(f"Task '{task}' added to your to-do list.")

def update_task(todo_list, index, new_task):
    if 1 <= index <= len(todo_list):
        todo_list[index - 1] = new_task
        save_todo_list(todo_list)
        print(f"Task {index} updated to '{new_task}'.")
    else:
        print("Invalid task index.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\n1. Display to-do list\n2. Add task\n3. Update task\n4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '3':
            index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            update_task(todo_list, index, new_task)
        elif choice == '4':
            print("Quitting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__== '__main__':
    main()
