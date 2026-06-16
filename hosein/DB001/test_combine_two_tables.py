import os
from hosein.run_postgresql_test import run_postgresql_test


def test_combine_two_tables():
    assert run_postgresql_test(os.path.dirname(__file__)) == [('Allen', 'Wang', None, None), ('Bob', 'Alice', 'New York City', 'New York')]