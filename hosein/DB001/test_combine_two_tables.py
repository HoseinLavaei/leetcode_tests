import os
from typing import List
import psycopg2

def run_sql_file(conn, path, fetch=False) -> List | None:
    with open(path) as f:
        cur = conn.cursor()
        cur.execute(f.read())
        if fetch:
            result = cur.fetchall()
            conn.commit()
            return result
        conn.commit()
        return None

def test_combine_two_tables():
    base_dir = os.path.dirname(__file__)
    conn = psycopg2.connect("postgresql://postgres:postgres@db/leetcode")
    run_sql_file(conn, os.path.join(base_dir, "setup.sql"))
    result = run_sql_file(conn, os.path.join(base_dir, "test.sql"), fetch=True)
    conn.close()
    assert result == [('Allen', 'Wang', None, None), ('Bob', 'Alice', 'New York City', 'New York')]