class Employee:
    def __init__(self, name, email, base_salary, position):
        self.name = name
        self.email = email
        self.base_salary = base_salary
        self.position = position

class SalaryCalculator:
    def calculate_net_salary(self, employee):
        if employee.position == "DESENVOLVEDOR":
            if employee.base_salary >= 3000:
                return employee.base_salary * 0.8
            else:
                return employee.base_salary * 0.9
        elif employee.position == "DBA" or employee.position == "TESTADOR":
            if employee.base_salary >= 2000:
                return employee.base_salary * 0.75
            else:
                return employee.base_salary * 0.85
        elif employee.position == "GERENTE":
            if employee.base_salary >= 5000:
                return employee.base_salary * 0.7
            else:
                return employee.base_salary * 0.8
        else:
            return employee.base_salary
