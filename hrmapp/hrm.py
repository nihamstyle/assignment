class Employee:
    EMPFILE = "employees.txt"

    def __init__(self, emp_id, name, position, department, hire_date, employment_status):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.department = department
        self.hire_date = hire_date
        self.employment_status = employment_status

    def __view_personal_info__(self):
        return f"ID: {self.emp_id}\nName: {self.name}\nPosition: {self.position}\nDepartment: {self.department}\nHire Date: {self.hire_date}\nStatus: {self.employment_status}"

    def __update_personal_info__(self, new_position, new_department):
        self.position = new_position
        self.department = new_department
        return "Information updated successfully."

    @classmethod
    def view_employees(cls):
        try:
            with open(cls.EMPFILE, "r") as file:
                print("Employee Details:")
                for line in file:
                    emp_id, name, position, department, hire_date, employment_status = line.strip().split(",")
                    print(f"Employee ID: {emp_id}")
                    print(f"Name: {name}")
                    print(f"Position: {position}")
                    print(f"Department: {department}")
                    print(f"Hire Date: {hire_date}")
                    print(f"Employment Status: {employment_status}")
                    print()
        except FileNotFoundError:
            print("Employees file not found.")

    @classmethod
    def load_and_save_employees(cls, employees=None):
        if employees is None:
            employees = []
        with open(cls.EMPFILE, "r") as file:
            for line in file:
                emp_id, name, position, department, hire_date, status = line.strip().split(",")
                employees.append(Employee(emp_id, name, position, department, hire_date, status))
        return employees

    def save_employees(self, employees):
        with open(self.EMPFILE, "w") as file:
            for employee in employees:
                file.write(
                    f"{employee.emp_id},{employee.name},{employee.position},{employee.department},{employee.hire_date},{employee.employment_status}\n")

    def add_employee(self, employees):
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        department = input("Enter employee department: ")
        hire_date = input("Enter employee hire date (YYYY-MM-DD): ")
        status = input("Enter employee status: ")
        new_employee = Employee(emp_id, name, position, department, hire_date, status)
        employees.append(new_employee)
        self.save_employees(employees)
        print("Employee added successfully.")

    def remove_employee(self, employees):
        emp_id = input("Enter employee ID to remove: ")
        for employee in employees:
            if employee.emp_id == emp_id:
                employees.remove(employee)
                self.save_employees(employees)
                print("Employee removed successfully.")
                return
        print("Employee not found.")

    def __submit_leave_request__(self, leave_type, duration, details):
        leave_request = f"Leave Request: Type - {leave_type}, Duration - {duration}, Details - {details}"
        return leave_request

    def __view_company_policies__(self):
        policies = """
            Company Policies:
            1. Dress code Policy
            2.Code of Conduct/Ethics Policy
            3. Anti-Discrimination and Harassment Policy
            4. Attendance and Punctuality Policy
            5. Leave and Time-Off Policy
            6. Remote Work Policy
            7. Information Security Policy
            8. Employee Benefits Policy
            9. Performance Evaluation and Feedback Policy
            10. Professional Development and Training Policy
            11. Conflict of Interest Policy
            12. Social Media and Internet Usage Policy
            13. Health and Safety Policy
                """
        return policies

    def __access_work_schedules__(self):
        schedules = """
            Work Schedule:
            Monday: 8:00 AM - 4:30 PM
            Tuesday: 8:00 AM - 4:30 PM
            Wednesday: 8:00 AM - 4:30 PM
            Thursday: 8:00 AM - 4:30 PM
            Friday: 8:00 AM - 11:30 AM
                """
        return schedules
