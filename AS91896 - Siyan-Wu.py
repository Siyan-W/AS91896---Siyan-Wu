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

def add_task():
    # Generate sequential task ID
    new_task_id = 'T' + str(len(Task_Dictionary) + 1)

    # Input task details
    title = easygui.enterbox(msg="Enter task title:")
    description = easygui.enterbox(msg="Enter task description:")
    priority = easygui.enterbox(msg="Enter task priority (1-3):")
    assignee = easygui.choicebox(msg="Assign task to:", choices=list(Team_Member_Dictionary.keys()))
    status = easygui.choicebox(msg="Set task status:", choices=['Not Started', 'In Progress', 'Blocked', 'Completed'])

    # Add task to dictionaries
    Task_Dictionary[new_task_id] = {
        'Title': title,
        'Description': description,
        'Assignee': assignee,
        'Priority': int(priority),
        'Status': status
    }

    # Update team member's task list
    Team_Member_Dictionary[assignee]['Tasks Assigned'].append(new_task_id)

def update_task():
    task_id = easygui.enterbox(msg="Enter task ID to update:")

    if task_id in Task_Dictionary:
        # Update task status
        status = easygui.choicebox(msg="Set task status:", choices=['Not Started', 'In Progress', 'Blocked', 'Completed'])
        Task_Dictionary[task_id]['Status'] = status

        # Assign task to a team member
        assignee = easygui.choicebox(msg="Assign task to:", choices=list(Team_Member_Dictionary.keys()))
        Task_Dictionary[task_id]['Assignee'] = assignee

        # Update team member's task list
        Team_Member_Dictionary[assignee]['Tasks Assigned'].append(task_id)

        # Remove task from team member's task list if completed
        if status == 'Completed':
            Team_Member_Dictionary[Task_Dictionary[task_id]['Assignee']]['Tasks Assigned'].remove(task_id)
    else:
        easygui.msgbox("Task ID not found!", title="Error")
