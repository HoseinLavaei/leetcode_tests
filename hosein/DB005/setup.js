db = db.getSiblingDB('leetcode');

db.products.drop();

db.products.insertMany([
  { _id: 1, name: "Laptop", category: "Electronics", price: 1200 },
  { _id: 2, name: "Phone", category: "Electronics", price: 800 },
  { _id: 3, name: "Tablet", category: "Electronics", price: 600 },
  { _id: 4, name: "Monitor", category: "Electronics", price: 800 },
  { _id: 5, name: "Sofa", category: "Furniture", price: 1500 },
  { _id: 6, name: "Chair", category: "Furniture", price: 400 },
  { _id: 7, name: "Table", category: "Furniture", price: 700 },
  { _id: 8, name: "Bed", category: "Furniture", price: 1200 },
  { _id: 9, name: "Desk", category: "Furniture", price: 700 }
]);