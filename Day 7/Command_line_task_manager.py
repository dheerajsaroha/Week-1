# Command line Task Manager
import os

FILE_NAME = "task.txt"

def load_task():
    task = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            for line in file:
                task_id,title,status = line.strip().split(" | ")
                task[int(task_id)] = {"title":title,"status":status}
    return task

# Save task into the file

def save_task(tasks):
    with open(FILE_NAME,"w") as file:
        for task_id,task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")


# add a new task
def add_task(tasks):
    title = input("Enter the task title \n")
    task_id = max(tasks.keys(),default=0) + 1
    tasks[task_id] = {"title":title,"status":"incomplete"}
    print(f"Task '{title}' added.")

# view task

def view_task(tasks):
    if not tasks:
        print("No Tasks Available")
    else:
        for task_id, task in tasks.items():
            print(f"{[task_id]} {task['title']}-{task['status']}")

# update the status of task
def mark_task_complete(tasks):
    task_id= int(input("ENter task id to mark complete : \n"))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print("Task updated successfully")
        print(f"Task {tasks[task_id]['title']} marked as completed")
    else:
        print("Task id not found!")

def delete_task(tasks):
    task_id= int(input("Enter task id to delete : \n"))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print("Task updated successfully")
        print(f"Task {deleted_task['title']} Deleted")
    else:
        print("Task id not found!")

# Main Menu
def main():
    task = load_task()
    while True:
        print("\n Task Manager Menu")
        print("1) Add Task")
        print("2) View Task")
        print("3) Mark Task Complete")
        print("4) Delete Task")
        print("5) Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task(task)
        elif choice == 2:
            view_task(task)
        elif choice == 3:
            mark_task_complete(task)
        elif choice == 4:
            delete_task(task)
        elif choice == 5:
            save_task(task)
            print("Good Bye")
            break
        else:
            print("Enter a valid choice!")

if __name__ == "__main__":
    main()
