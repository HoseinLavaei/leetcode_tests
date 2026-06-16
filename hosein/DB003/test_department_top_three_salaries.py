import os
from hosein.run_postgresql_test import run_postgresql_test


def test_department_top_three_salaries():
    assert run_postgresql_test(os.path.dirname(__file__)) == [('IT', 'Max', 90000),('IT', 'Joe', 85000),('IT', 'Randy', 85000),('IT', 'Henry', 80000)]