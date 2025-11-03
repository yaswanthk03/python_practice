"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""
import os


FILE_NAME = 'tasks.txt'

def get_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding="utf-8") as f:
            for line in f:
                task, status = line.strip().rsplit('||', 1)
                tasks.append({ 'task' : task, 'done': status == 'done' })
    return tasks

def upload_tasks(tasks:list[str]):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(f"{task["task"]} || {"done" if task['status'] else 'not_done'}\n")

def view_task(tasks:list[str]):
    for task in tasks:
        print(f"|{'✅' if task['status'] else " "}| {task['task']}")
    if not tasks:
        print("No tasks yet!")
    print()

def task_manager():
    tasks = get_tasks()

    while True:
        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()

        match choice:
            case "1":
                new_task = input("Enter the task: ").strip()
                if new_task:
                    tasks.append({ 'task' : new_task, 'status' : False })
                    upload_tasks(tasks)
                else:
                    print("Task should not be empty.\n")
            case '2':
                view_task(tasks)
            case '3':
                try:
                    view_task(tasks)
                    task_id = int(input("Enter the task number to be edited: "))
                    if 0 < task_id <= len(tasks):
                        tasks[task_id - 1]['status'] = True
                        upload_tasks(tasks)
                    else:
                        raise ValueError("Enter valid id.")
                except ValueError as e:
                    print(e)
            case '4':
                try:
                    view_task(tasks)
                    task_id = int(input("Enter the task number to be edited: "))
                    if 0 < task_id <= len(tasks):
                        tasks.pop(task_id - 1)
                        upload_tasks(tasks)
                    else:
                        raise ValueError("Enter valid id.")
                except ValueError as e:
                    print(e)
            case '5':
                break
            case _:
                print("Enter a valid option.")

task_manager()