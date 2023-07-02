class Employee:
    name: str
    id: str
    department: str
    salary: float

    def __init__(self):
        pass

    def get_data(self) -> None:
        self.name = input("Enter the name : ")
        self.id = input("Enter the employee id : ")
        self.department = input("Enter the department : ")
        self.salary = float(input("Enter the salary of the employee : "))

    def print_data(self) -> None:
        print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.department}\nSalary: {self.salary}\n")

    def update_salary(self, sal: float) -> None:
        self.salary = sal


EmployeeList: list = []


def update_salary(dep: str, salary: float) -> None:
    for employee in EmployeeList:
        if employee.department == dep:
            employee.update_salary(salary)


n: int = int(input("Enter the number of Employees : "))
print("Enter the employee details : ")
for i in range(n):
    EmployeeList.append(Employee())
    EmployeeList[i].get_data()

for emp in EmployeeList:
    emp.print_data()
