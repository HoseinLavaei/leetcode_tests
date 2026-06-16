db = db.getSiblingDB('leetcode');

var result = db.orders.aggregate([
  {
    $group: {
      _id: "$customer_id",
      total_spent: { $sum: "$total_amount" }
    }
  },
  {
    $project: {
      _id: 0,
      customer_id: "$_id",
      total_spent: 1
    }
  },
  { $sort: { customer_id: 1 } }
]).toArray();

print(JSON.stringify(result));