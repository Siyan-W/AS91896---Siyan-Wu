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

# Function to display task details
def print_task(task_id):
    task_details = Task_Dictionary.get(task_id)
    if task_details:
        message = f'Task ID: {task_id}\n' \
                  f'Title: {task_details["Title"]}\n' \
                  f'Description: {task_details["Description"]}\n' \
                  f'Assignee: {task_details["Assignee"]}\n' \
                  f'Priority: {task_details["Priority"]}\n' \
                  f'Status: {task_details["Status"]}'
        easygui.msgbox(message, title='Task Details')

# Get user input for Task ID
task_id = easygui.enterbox('Enter Task ID (eg., T1, T2, T3, ...):')

# Check if the entered Task ID is valid and display task details
if task_id in Task_Dictionary:
    print_task(task_id)
else:
    easygui.msgbox('Invalid Task ID entered.', title='Error')

def add_new_task():
    # Find the next available task ID by incrementing the last task ID
    last_task_id = sorted(Task_Dictionary.keys())[-1]
    new_task_id = 'T' + str(int(last_task_id[1:]) + 1)

    # Get user input for task details
    title = easygui.enterbox('Enter the title of the task:')
    description = easygui.enterbox('Enter the description of the task:')
    priority = easygui.integerbox('Enter priority rating (1-3) of the task:',\
                                   lowerbound=1, upperbound=3)
    status = easygui.choicebox('Select the status of the task:',\
                            choices=['Not Started', 'In Progress', 'Blocked'])

    # Add the new task to the Task Dictionary
    Task_Dictionary[new_task_id] = {
        'Title': title,
        'Description': description,
        'Assignee': None,  # Initially no assignee
        'Priority': priority,
        'Status': status
    }

    easygui.msgbox('New task added successfully!\nTask ID: {}'.format(new_task_id), title='Task Added')

# Main function to run the program
def main():
    add_new_task()

if __name__ == "__main__":
    main()