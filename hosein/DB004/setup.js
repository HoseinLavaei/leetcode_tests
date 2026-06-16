db = db.getSiblingDB('leetcode');

db.orders.drop();

var result = db.orders.insertMany([
  { _id: 1, customer_id: "C001", total_amount: 150, order_date: ISODate("2025-01-01") },
  { _id: 2, customer_id: "C002", total_amount: 200, order_date: ISODate("2025-01-02") },
  { _id: 3, customer_id: "C001", total_amount: 75,  order_date: ISODate("2025-01-03") },
  { _id: 4, customer_id: "C003", total_amount: 300, order_date: ISODate("2025-01-04") },
  { _id: 5, customer_id: "C002", total_amount: 50,  order_date: ISODate("2025-01-05") }
]);