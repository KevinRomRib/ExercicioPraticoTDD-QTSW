from src.salary_calculator import Employee, SalaryCalculator

def test_developer_high_salary():
    employee = Employee("João Silva", "teste@example.com", 3000.0, "DESENVOLVEDOR")
    calculator = SalaryCalculator()
    assert calculator.calculate_net_salary(employee) == 2400.0

def test_developer_low_salary():
    employee = Employee("Maria Oliveira", "teste@example.com", 2500.0, "DESENVOLVEDOR")
    calculator = SalaryCalculator()
    assert calculator.calculate_net_salary(employee) == 2250.0

def test_dba_high_salary():
    employee = Employee("Carlos Santos", "teste@example.com", 2000.0, "DBA")
    calculator = SalaryCalculator()
    assert calculator.calculate_net_salary(employee) == 1500.0
