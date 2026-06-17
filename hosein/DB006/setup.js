db = db.getSiblingDB('leetcode');

db.departments.drop();
db.employees.drop();

db.departments.insertMany([
  { _id: 1, name: "Sales" },
  { _id: 2, name: "Engineering" },
  { _id: 3, name: "HR" }
]);

db.employees.insertMany([
  { _id: 1, name: "Alice", salary: 70000, departmentId: 1 },
  { _id: 2, name: "Bob",   salary: 90000, departmentId: 1 },
  { _id: 3, name: "Carol", salary: 60000, departmentId: 2 },
  { _id: 4, name: "Dave",  salary: 80000, departmentId: 2 },
  { _id: 5, name: "Eve",   salary: 75000, departmentId: 2 },
  { _id: 6, name: "Frank", salary: 50000, departmentId: 3 },
  { _id: 7, name: "Grace", salary: 55000, departmentId: 3 }
]);