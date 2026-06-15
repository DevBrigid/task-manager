# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Create New Task ---")
            # 1. Validate Title Loop
            while True:
                title_input = input("Enter task title: ")
                is_valid, validated_title = validate_task_title(title_input)
                if is_valid:
                    break
            
            # 2. Validate Description Loop
            while True:
                desc_input = input("Enter task description (optional): ")
                is_valid, validated_desc = validate_task_description(desc_input)
                if is_valid:
                    break
                    
            # 3. Validate Due Date Loop
            while True:
                date_input = input("Enter due date (YYYY-MM-DD): ")
                is_valid, validated_date = validate_due_date(date_input)
                if is_valid:
                    break
            
            add_task(validated_title, validated_desc, validated_date)

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks working currently. Add a task first.")
            else:
                print("\n--- Current Tasks ---")
                for idx, task in enumerate(tasks, 1):
                    status = "✅ Done" if task["completed"] else "❌ Pending"
                    print(f"{idx}. {task['title']} [{status}]")
                
                while True:
                    idx_input = input("\nEnter the task number to complete: ").strip()
                    if idx_input.isdigit():
                        task_num = int(idx_input)
                        if 1 <= task_num <= len(tasks):
                            mark_task_as_complete(task_num - 1)
                            break
                    print(f"❌ Error: Please enter a number between 1 and {len(tasks)}.")

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()