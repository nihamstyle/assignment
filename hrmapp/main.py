from authentication import authenticate
from hrm import Employee

def main():
    employees = Employee.load_and_save_employees()
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if authenticate(username, password):
            print("Authentication successful.\n")
            current_user = Employee("1028401", "Mohammethu Niham", "Manager", "HR", "2024-03-10", "Active")

            print("Main Menu:")
            print("1. View Personal Information")
            print("2. Add New Employee information")
            print("3. Remove Employee")
            print("4. View All Employee Information")
            print("5. Update Personal Information")
            print("6. Submit Leave Requests")
            print("7. View Company Policies")
            print("8. Access Work Schedules")
            print("9. Logout")
            print("10. Exit")
            while True:
                choice = input("Enter your choice: ")

                if choice == "1":
                    print("")
                    print(current_user.__view_personal_info__())

                elif choice == "2":
                    print("")
                    current_user.add_employee(employees)
                    current_user.save_employees(employees)

                elif choice == "3":
                    print("")
                    current_user.remove_employee(employees)
                elif choice == "4":
                    print("")
                    Employee.view_employees()

                elif choice == "5":
                    print("")
                    new_position = input("Enter new position: ")
                    new_department = input("Enter new department: ")
                    update_status = current_user.__update_personal_info__(new_position, new_department)
                    print(update_status)

                elif choice == "6":
                    leave_type = input("Enter leave type: ")
                    duration: str = input("Enter duration: ")
                    details = input("Enter more details: ")
                    leave_request = current_user.__submit_leave_request__(leave_type, duration, details)
                    print(leave_request)
                    print("")
                    print("Your request has been submitted successfully.")

                elif choice == "7":
                    policies = current_user.__view_company_policies__()
                    print(policies)

                elif choice == "8":
                    schedules = current_user.__access_work_schedules__()
                    print(schedules)

                elif choice == "9":
                    log = input("Do you want to logout ?(yes/no): ")
                    if log == "yes":
                        print("Logging out.\n")
                        break
                    elif log == "no":
                        print("Cancelled.")
                        print("")
                        pass
                    else:
                        print("invalid input. Please try again.")
                elif choice == "10":
                    while True:
                        out: str = input("Do you want to exit?(yes / no): ")
                        if out == "no":
                            print("Cancelled.")
                            print("")
                            break
                        elif out == "yes":
                            print("Exiting from the session.")
                            exit()
                        else:
                            print("invalid input. Please try again.")


                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Authentication failed. Please try again.\n")


if __name__ == "__main__":
    main()
