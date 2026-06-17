import os
from hosein.run_mongodb_test import run_mongodb_test


def test_top_3_most_expensive_products_by_category():
    assert run_mongodb_test(os.path.dirname(__file__)) == [
  {"category":"Electronics","name":"Laptop","price":1200},
  {"category":"Electronics","name":"Monitor","price":800},
  {"category":"Electronics","name":"Phone","price":800},
  {"category":"Electronics","name":"Tablet","price":600},
  {"category":"Furniture","name":"Sofa","price":1500},
  {"category":"Furniture","name":"Bed","price":1200},
  {"category":"Furniture","name":"Desk","price":700},
  {"category":"Furniture","name":"Table","price":700}
]