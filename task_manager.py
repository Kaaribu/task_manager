'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
from datetime import date


#====Login Section====
def usernames():
    # users dictionary
    global users
    users = {}

    # Open "user.txt" file
    with open("user.txt", "r") as user:

        # Check "user.txt" file for matching combination
        for line in user:
            user = line.strip("\n")
            # Prevent out-of-bound error
            if user != "":
                user = user.split(", ")
                users.update({user[0]: user[1]})
    return users


# Login function to check if username and password are registered into the user.txt file
def login(): 
    global username
    username = {}
    user_list = usernames()

    # Check the username against the dictionary
    username = input("Enter your username:\n")
    while username not in user_list:
        username = input("No record of your username. Please try again.\n")

    # Check the username against the dictionary and password value for their username key
    password = input("Enter your password:\n")
    while password != user_list[username]:
        password = input("Incorrect password. Please try again.\n")


# Function to create task                                         
def create_task() :
    global user_task
    user_task = {}

    # Open "tasks.txt" file
    with open("tasks.txt", "r") as file:
        # Check "tasks.txt" file for matching combination
        for line in enumerate(file, 1):
            user_task[line[0]] = line[1]


# Prints out the admin menu
def admin_menu():
    print('''\nSelect one of the following options below:
r -  Register a new user
a -  Add a task
va - View all tasks
vm - View my tasks
ds - Display statistics
e -  Exit
''')
   

# Prints out the regular user menu
def print_menu():
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    print('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
''')


# Function to register a new user    
def reg_user(username):
    # Check that user has admin rights
    if username != "admin":
        print("\nYou do not have admin rights to register a user")
    else:
        while True:
            # Open "user.txt" file in append mode
            with open("user.txt", "a") as file:
                # Enter new username to be added 
                new_username = input("Enter the username you want to add:\n")
           
                # Check that username does not exist before a new username is added
                if new_username in users:
                    print("Username already taken. Try a different one.\n")
                else:
                    password = input(f"Enter a new password:\n")
                    password_confirm = input("Confirm the password entered:\n")
                    # Check that password and password confirmation match
                    if password == password_confirm:
                        file.write(f"\n{new_username}, {password}\n")
                        print(f"\n{new_username} has been added successfully.\n")
                    else:
                        print("The passwords entered do not match, try again.\n")
            break # Breaks the loop 
    

# Function to add a task to "tasks.txt" file
def add_task(username):
    global task_complete
    # Prompts user for task data
    assign_user = input("Who is this task assigned to?\n")
    # Checks that user is in user.txt
    while assign_user not in users:
        assign_user = input("Not a valid user. Please try again.\n")
    task_name = input("What is the title of this task?\n")
    task_description = input("Enter the description for this task:\n")
    due_date = input("When is this task due? (format: dd Apr yyyy)\n")
    today_date = date.today().strftime("%d %b %Y")
    task_complete = "No"

   # Open "tasks.txt" file in append mode
    with open("tasks.txt", "a") as tasks:
        tasks.write(f"\n{assign_user}, {task_name}, {task_description}, {today_date}, {due_date}, {task_complete}")
        print("\nNew task has been added.\n")


# Views all tasks
def view_all():
    task_list = []  #This is the list for the Task Numbers
    f = open('tasks.txt', 'r+')
    row = f.readlines()
    task_num = 0

    # Loop through the file and print out the tasks
    for i in row:
        data = i.replace(" ", "")
        data = i.replace("\n","")
        data = i.split(",")
        task_num +=1
        task_list.append(task_num)
        
        # Print out the info
        print(f'''
        Task Number:        {task_num}
        Task assigned to:   {data[0]}
        Task title:        {data[1]}
        Task descrition:   {data[2]}
        Due Date:          {data[3]}
        Date Assigned:     {data[4]}
        Completed:         {data[5]}\n''')


# The function to view tasks for user logged in 
# The function receives the username as a parameter
def view_mine(username):
    task_list = []  #This is the list for the Task Numbers
    f = open('tasks.txt', 'r+')
    row = f.readlines()
    task_num = 0
    # Loop through the file 
    for i in row:
        data = i.replace(" ", "")
        data = i.replace("\n","")
        data = i.split(",")
        task_num +=1
        task_list.append(task_num)
        # Check if the username matches the username in the file
        if username == data[0]:
            print(f'''
            Task Number:        {task_num}
            Task assigned to:   {data[0]}
            Task title:        {data[1]}
            Task descrition:   {data[2]}
            Due Date:          {data[3]}
            Date Assigned:     {data[4]}
            Completed:         {data[5]}\n''')


# Function to display statistics for the tasks and users         
def display_statistics():
    if menu == "ds":

        tasks_num = 0 # This will count the number of tasks
        users_num = 0 # This will count the number of users
        
        # Open "tasks.txt" file in read mode
        with open("tasks.txt", "r") as task_file:
            
            # Loop through the file and count the number of tasks
            for line in task_file:
                tasks_num += 1
            print (f"\nTotal number of tasks: {tasks_num}")
            # Open "user.txt" file in read mode
            with open("user.txt", "r") as username:
                # Loop through the file and count the number of users
                for line in username:
                    users_num += 1
            print (f"Total number of users: {users_num}")

# Log into program
while login:
    user = login()

    if user == "admin" :
        admin_rights = True
        login = False

    elif user != "loop" :
        login = False

# While loop to continue returning to menu until user selects exit 
while True:
    if username == 'admin':
        admin_menu()  
    else:
       print_menu()
    
    menu = input("Please select an option:\n").lower()   
    # Register a new user, only admin can do this   
    if menu == "r":
        reg_user(username)
    # Add a task        
    elif menu == "a":
        add_task(users)
    # View all tasks        
    elif menu == "va":
        view_all()
    # View my tasks        
    elif menu == "vm":
        view_mine(username)
    # Display statistics        
    elif menu == "ds" :
        display_statistics()
    # Exit program        
    elif menu == "e":
        print('\nGoodbye!!!')
        exit()
    # If user enters an invalid option
    else:
        print("You have made a wrong choice, Please Try again\n")

#======================================== END OF PROGRAM ============================================

#                                           REFERENCES:
# For better understanding of file handling:
# https://www.w3schools.com/python/python_file_handling.asp

# For getting current date and time:
# https://www.stackoverflow.com/questions/250357/how-to-get-the-current-date-and-time-in-python

# For readding file data line by line into lists:
# https://www.stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

# Wanted to expand my grasp on directories:
# https://www.stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

# Formating code to allow only the admin to regiter users:
# https://stackoverflow.com/questions/65778538/how-to-format-a-program-so-that-only-username-admin-can-register-add-new-use

#====================================================================================================
