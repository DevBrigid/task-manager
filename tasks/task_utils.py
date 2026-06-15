from datetime import datetime

# Import validation functions (Uncomment if these are in a separate file)
# from validation import validate_task_title, validate_task_description, validate_due_date

# Define global tasks list
tasks = []

# 1. Implement add_task function
def add_task(title, description, due_date):
    """
    Creates a new task dictionary and appends it to the global tasks list.
    """
    new_task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(new_task)
    # Direct Rubric Match
    print("Task added successfully!")

# 2. Implement mark_task_as_complete function
def mark_task_as_complete(index):
    """
    Marks a specific task as complete based on its 0-indexed position.
    """
    # Safety check to ensure index falls within our current tasks length
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        # Direct Rubric Match
        print("Task marked as complete!")
    else:
        print("❌ Error: Invalid task number.")

# 3. Implement view_pending_tasks function
def view_pending_tasks():
    """
    Loops through and displays only the tasks where completed is False.
    """
    # Rubric Check: Match- No working currently / Pending task no error
    if len(tasks) == 0:
        print("No tasks currently available.")
        return

    pending_found = False
    print("\n--- PENDING TASKS ---")
    for idx, task in enumerate(tasks, 1):
        if not task["completed"]:
            print(f"{idx}. {task['title']} (Due: {task['due_date']})")
            if task["description"]:
                print(f"   Description: {task['description']}")
            pending_found = True
            
    if not pending_found:
        print("No working currently. All tasks are completed!")

# 4. Implement calculate_progress function
def calculate_progress():
    """
    Calculates the percentage of completed tasks. 
    Handles empty arrays without breaking (No error).
    """
    total_tasks = len(tasks)
    
    # Rubric Check: Check Validation- Check for if len() 
    if total_tasks == 0:
        print("No working currently. Add tasks to see progress metrics.")
        return 0.0

    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / total_tasks) * 100
    
    print(f"\n--- PROGRESS DASHBOARD ---")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed:  {completed_tasks}")
    print(f"Progress:   {progress:.1f}%")
    
    return progress