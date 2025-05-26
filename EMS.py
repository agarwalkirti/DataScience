'''
Employee Management System (EMS)
Objective - Create a simplified Employee Management System (EMS). This project will cover control structures, functions, and object-oriented programming concepts to manage employee data.

-The Data Storage:
Used a dictionary to store employee data where the keys is the emp_id (Employee ID) and the value is another dictionary containing:
name: Employee's name.
age: Employee's age.
department: Employee's department.
salary: Employee's monthly salary.
Initialize the dictionary with some sample employee data for testing (e.g., {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}).

- Defined a Menu System
Created a menu that displays the following options:
Add Employee
View All Employees
Search for Employee
Exit
Implemented a loop to continuously display the menu until the user chooses to Exit.

  - Added Employee Functionality
Prompted the User to enter the following details for a new employee:
emp_id (Employee ID)
name (Employee Name)
age (Employee Age)
department (Employee Department)
salary (Employee Salary)
Validate Input: Make sure the Employee ID is unique. If it already exists in the dictionary, ask the user to enter a new ID.
Store the Employee data in the dictionary using the entered emp_id as the key and the other details as values.
Display a message indicating the employee was successfully added.

  - View All Employees
Display all employees stored in the dictionary.
Format the display in a table-like structure, showing employee details (ID, name, age, department, salary).
If there are no employees in the system, display a message like:
"No employees available."

- Search for an Employee by ID
Prompt the User to enter the emp_id they want to search for.
Search the Dictionary:
If the employee exists, display their details (name, age, department, salary).
If the employee does not exist, display a message like:
"Employee not found."

  - Exit the Program
Add an Exit option in the menu.
If the user chooses Exit, display a thank-you message and exit the program.

Project Code Structure:
main_menu(): Displays the main menu and calls the appropriate function based on user input.
add_employee(): Adds a new employee to the dictionary.
view_employees(): Displays all employee details.
search_employee(): Searches for an employee by ID.
'''

# Dictionary to store employee data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Ravi', 'age': 30, 'department': 'Engineering', 'salary': 60000},
    103: {'name': 'Ananya', 'age': 25, 'department': 'Finance', 'salary': 55000},
    104: {'name': 'Priya', 'age': 35, 'department': 'Marketing', 'salary': 65000}
}


# Function to view all employees
def view_employees_normal():
    if not employees:
        print("No Employee Available.")
    else:
        for emp_id, details in employees.items():
            print(f"Employee ID: {emp_id}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
            print()  # Line break for better readability


def view_employees():
    if not employees:
        print("No Employee Available.")
    else:
        print("\n{:<10} {:<20} {:<5} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Department", "Salary"))
        print("-" * 65)

        for emp_id, details in employees.items():
            print("{:<10} {:<20} {:<5} {:<15} {:<10}".format(
                emp_id,
                details['name'],
                details['age'],
                details['department'],
                details['salary']
            ))


# Search for a specific employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            print(f"\nEmployee ID: {emp_id}")
            for key, value in employees[emp_id].items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Please enter a valid Employee ID.")


# Function to add an employee
def add_employee():
    try:
        while True:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print(f"Employee ID {emp_id} already exists. Please enter a different ID.")
            else:
                break  # ID is unique, exit the loop
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print(f"Employee {name} added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter correct data types.")


def main_menu():
    print("\n Employee Management System")
    print('Press 1 to Add Employee ')
    print('Press 2 to view all employees')
    print('press 3 to search for employee')
    print('press 4 to Exit the menu')


def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("Add Employee selected.")
            add_employee()
        elif choice == '2':
            print("View All Employees details in database.")
            view_employees()
        elif choice == '3':
            print("Search for Employee selected.")
            search_employee()
        elif choice == '4':
            print("Exiting program. Goodbye! Thank You!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
