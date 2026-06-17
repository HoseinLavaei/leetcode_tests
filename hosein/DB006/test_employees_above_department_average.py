import os
from hosein.run_mongodb_test import run_mongodb_test


def test_employees_above_department_average():
    assert run_mongodb_test(os.path.dirname(__file__)) == [
        {"department": "Engineering", "employee": "Dave", "salary": 80000, "dept_avg": 71666.67},
        {"department": "Engineering", "employee": "Eve", "salary": 75000, "dept_avg": 71666.67},
        {"department": "HR", "employee": "Grace", "salary": 55000, "dept_avg": 52500},
        {"department": "Sales", "employee": "Bob", "salary": 90000, "dept_avg": 80000}
    ]