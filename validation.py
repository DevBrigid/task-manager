from datetime import datetime
import re

def validate_task_title(title):
    # - Must not be empty or whitespace only
    if not title or title.strip() == "":
        print("❌ Error: Title not found")
        return False, None
    
    title = title.strip()

    # - Check minimum characters (Check for if len() rubric rule)
    if len(title) < 3:
        print("❌ Error: Title must be at least 3 characters long.")
        return False, None
    
    # - Check maximum characters
    if len(title) > 100:
        print("❌ Error: Title must not exceed 100 characters.")
        return False, None
    
    # - Check for special characters (only letters, numbers, spaces, hyphens)
    if not re.match(r"^[a-zA-Z0-9 \-]+$", title):
        print("❌ Error: Title can only contain letters, numbers, spaces, and hyphens.")
        return False, None # Fixed: Was returning True previously
        
    return True, title
    
def validate_task_description(description):
    # - Can be empty (description is optional)
    if description is None or description.strip() == "":
        return True, ""
    
    description = description.strip()
    
    # - If provided, must not exceed 500 characters
    if len(description) > 500:
        print("❌ Error: Description must not exceed 500 characters.")
        return False, None

    return True, description

def validate_due_date(due_date):
    # - Must not be empty
    if not due_date or due_date.strip() == "":
        print("❌ Error: Due date cannot be empty")
        return False, None
        
    due_date = due_date.strip()

    # - Must follow the format YYYY-MM-DD & not be an invalid calendar date
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Error: Due date must be a valid date in the format YYYY-MM-DD (e.g. 2026-12-31).")
        return False, None
    
    # - Must not be a date in the past
    if parsed_date < datetime.today().date():
        print("❌ Error: Due date cannot be in the past.")
        return False, None
        
    return True, due_date