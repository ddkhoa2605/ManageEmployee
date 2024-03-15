class Employee:
    def __init__(self, employee_id, name, position, hours_worked=0):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.hours_worked = hours_worked
        self.next = None


class EmployeeLinkedList:
    def __init__(self):
        self.head = None

    def add_employee(self, employee):
        if not self.head:
            self.head = employee
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = employee

    def delete_employee(self, employee_id):
        current = self.head
        if current.employee_id == employee_id:
            self.head = current.next
            return
        while current.next:
            if current.next.employee_id == employee_id:
                current.next = current.next.next
                return
            current = current.next

    def display_employees(self):
        current = self.head
        while current:
            print(f"ID: {current.employee_id}, Name: {current.name}, Position: {current.position}, Hours Worked: {current.hours_worked}")
            current = current.next


def display_menu():
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Display Employees")
    print("4. Exit")


def main():
    employee_list = EmployeeLinkedList()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            employee = Employee(employee_id, name, position)
            employee_list.add_employee(employee)
            print("Employee added successfully.")
        elif choice == "2":
            employee_id = int(input("Enter Employee ID to delete: "))
            employee_list.delete_employee(employee_id)
            print("Employee deleted successfully.")
        elif choice == "3":
            print("Employee List:")
            employee_list.display_employees()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
