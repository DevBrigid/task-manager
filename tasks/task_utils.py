from datetime import datetime

# Central data storage tracking tasks as a list of dictionaries
tasks = []

def add_task(title, description, due_date):
    """Creates a task dictionary and appends it to the tasks list."""
    new_task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(new_task)
    print("Task added successfully!")

def mark_task_as_complete(index):
    """Marks a task as completed based on its index position."""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def view_pending_tasks():
    """Displays only tasks where completed is False."""
    if len(tasks) == 0:
        print("No tasks currently available.")
        return

    pending_found = False
    for idx, task in enumerate(tasks, 1):
        if not task["completed"]:
            print(f"{idx}. {task['title']} (Due: {task['due_date']})")
            if task["description"]:
                print(f"   Description: {task['description']}")
            pending_found = True
            
    if not pending_found:
        print("No working currently.")

def calculate_progress():
    """Calculates and returns the percentage of completed tasks."""
    total_tasks = len(tasks)
    
    if total_tasks == 0:
        print("No working currently.")
        return 0.0

    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / total_tasks) * 100
    
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Progress: {progress:.1f}%")
    
    return progress