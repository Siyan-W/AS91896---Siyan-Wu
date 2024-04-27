import easygui

# Task Dictionary containing details of tasks
Task_Dictionary = {
    'T1': {
        'Title': 'Design Homepage',
        'Description': 'Create a mochup of the homepage',
        'Assignee': 'JSM',
        'Priority': 3,
        'Status': 'In progress'
    },
    
    'T2': {
        'Title': 'Implement Login page',
        'Description': 'Create the Login page for the website',
        'Assignee': 'JSM',
        'Priority': 3,
        'Status': 'Blocked'
    },

    'T3': {
        'Title': 'Fix navigation menu',
        'Description': 'Fix the navigation menu to be more user-friendly',
        'Assignee': 'None',
        'Priority': 1,
        'Status': 'Not Started'
    },

    'T4': {
        'Title': 'Add payment processing',
        'Description': 'Implement payment processing for the website',
        'Assignee': 'JLO',
        'Priority': 2,
        'Status': 'In progress'
    },

    'T5': {
        'Title': 'Create an About Us page',
        'Description': 'Create a page with information about the company',
        'Assignee': 'BDI',
        'Priority': 1,
        'Status': 'Blocked'
    }
}

# Team Member Dictionary containing details of members
Team_Member_Dictionary = {
    'JSM': {
        'Name': "John Smith",
        'Email': 'John@techvison.com',
        'Tasks Assigned': 'T1, T2'
    },

    'JLO': {
        'Name': "Jane Love",
        'Email': 'Jane@techvison.com',
        'Tasks Assigned': 'T4'
    },

    'BDI': {
        'Name': "Bob Dilon",
        'Email': 'Bob@techvison.com',
        'Tasks Assigned': 'T5'
    }
}

# Function to add a new task
def add_task():
    while True:
        # Generate sequential task ID
        new_task_id = 'T' + str(len(Task_Dictionary) + 1)

        # Input task details
        title = easygui.enterbox(msg="Enter task title:")
        if title == None:
            break

        description = easygui.enterbox(msg="Enter task description:")
        if description == None:
            break
        
        priority = easygui.integerbox(msg="Enter task priority (1-3):", \
        lowerbound= 1, upperbound = 3)
        if priority == None:
            break

        status = easygui.choicebox(msg="Set task status:", \
        choices=['Not Started', 'In Progress', 'Blocked', 'Completed'])
        if status == None:
            break

        # Add the task to dictionaries
        Task_Dictionary[new_task_id] = {
            'Title': title,
            'Description': description,
            "Assignee": None,
            'Priority': int(priority),
            'Status': status
        }

        easygui.msgbox(f"Task {new_task_id} has been added")

        break

# Function to update an existing task
def update_task():
    while True:
        task_id = easygui.enterbox(msg="Enter task ID to update:")

        if task_id == None:
            break

        if task_id in Task_Dictionary:
            # Update task status by letting user choose
            status = easygui.choicebox(msg="Set task status:", \
                choices=['Not Started', 'In Progress', 'Blocked', 'Completed'])
            
            Task_Dictionary[task_id]['Status'] = status

            # Assign task to team member if not "Completed"
            if status != "Completed":
                assignee = easygui.choicebox(msg="Assign task to:", \
                        choices=list(Team_Member_Dictionary))
                Task_Dictionary[task_id]['Assignee'] = assignee

                # Remove task from team member's task list if completed
                tasks_assigned = Team_Member_Dictionary\
                [Task_Dictionary[task_id]['Assignee']]['Tasks Assigned']\
                .split(',')

                # Remove the task_id from the list
                tasks_assigned = \
                [task.strip() for task in tasks_assigned if task.strip() \
                !=task_id]

                # Convert the list back to a string
                Team_Member_Dictionary[Task_Dictionary[task_id]['Assignee']]\
                    ['Tasks Assigned'] = ', '.join(tasks_assigned)
            else:
                Task_Dictionary[task_id]['Assignee'] = "None"

            easygui.msgbox(f"Task {task_id} has been updated")
            break
            
        else:
            easygui.msgbox("Invalid task ID!", title="Error")

# Function to search for a task
def search_task():
    task_title = easygui.choicebox(msg="Choose a task to view:", \
            choices=list(Task_Dictionary))
    
    if task_title:
        task_details = Task_Dictionary[task_title]
        
        easygui.msgbox(msg=f"Title: {task_details['Title']}\
        \nDescription: {task_details['Description']}\
        \nAssignee: {task_details['Assignee']}\
        \nPriority:{task_details['Priority']}\
        \nStatus: {task_details['Status']}", \
        title="Task Details")
        
    else:
        easygui.msgbox("No task selected!", title="Error")

# Function to search for a team member
def search_team_member():
    team_member = easygui.choicebox(msg="Choose a team member to view:", \
    choices=list(Team_Member_Dictionary))

    if team_member:
        member_details = Team_Member_Dictionary[team_member]
        task_list = (member_details['Tasks Assigned'])
        easygui.msgbox(msg=f"Name: {member_details['Name']}\
        \nEmail: {member_details['Email']}\
        \nTasks Assigned: {task_list}", \
        title="Team Member Details")
        
    else:
        easygui.msgbox("No team member selected!", title="Error")

# Function to generate report of all the tasks
def generate_report():
    completed_tasks = in_progress_tasks = blocked_tasks = not_started_tasks = 0
    for task in Task_Dictionary.values():
        if task['Status'] == 'Completed':
            completed_tasks += 1
        elif task['Status'] == 'In progress':
            in_progress_tasks += 1
        elif task['Status'] == 'Blocked':
            blocked_tasks += 1
        elif task['Status'] == 'Not Started':
            not_started_tasks += 1

    report_msg = f"Tasks Completed: {completed_tasks}\
        \nTasks In Progress: {in_progress_tasks}\
        \nTasks Blocked: {blocked_tasks}\
        \nTasks Not Started: {not_started_tasks}"
    
    easygui.msgbox(msg=report_msg, title="Project Progress Report")

# Function to print out all the tasks and details
def print_all():
    task_collection = ""
    for task_id, task_details in Task_Dictionary.items():
        task_collection += f"Task ID: {task_id}\
            \nTitle: {task_details['Title']}\
            \nDescription: {task_details['Description']}\
            \nAssignee: {task_details['Assignee']}\
            \nPriority: {task_details['Priority']}\
            \nStatus: {task_details['Status']}\n\n"
        
    easygui.msgbox(task_collection, title="Task Collection")

# Main menu options
options = [
    "Add Task",
    "Update Task",
    "Search Task",
    "Search Member",
    "Generate Report",
    "Print All",
    "Exit"
]

# Letting user select what they want to make change of
while True:
    choice = easygui.buttonbox(msg="Choose an option:", choices=options)

    if choice == "Add Task":
        add_task()
    elif choice == "Update Task":
        update_task()
    elif choice == "Search Task":
        search_task()
    elif choice == "Search Member":
        search_team_member()
    elif choice == "Generate Report":
        generate_report()
    elif choice == "Print All":
        print_all()
    elif choice == "Exit":
        break
