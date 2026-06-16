import os
from typing import List
import psycopg2

DATABASE_URL = MONGO_URI = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/leetcode")

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

def run_postgresql_test(base_dir:str):
    conn = psycopg2.connect(DATABASE_URL)
    run_sql_file(conn, os.path.join(base_dir, "setup.sql"))
    result = run_sql_file(conn, os.path.join(base_dir, "test.sql"), fetch=True)
    conn.close()
    return result