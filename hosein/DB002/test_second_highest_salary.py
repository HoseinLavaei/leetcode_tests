import os
from hosein.run_postgresql_test import run_postgresql_test


def test_second_highest_salary():
    assert run_postgresql_test(os.path.dirname(__file__)) == [(200,)]