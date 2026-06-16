import os
from hosein.run_mongodb_test import run_mongodb_test


def test_customer_spending():
    assert run_mongodb_test(os.path.dirname(__file__)) == [{"customer_id": "C001", "total_spent": 225},{"customer_id": "C002", "total_spent": 250},{"customer_id": "C003", "total_spent": 300}]