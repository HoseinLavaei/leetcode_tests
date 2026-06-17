db = db.getSiblingDB('leetcode');

var result = db.products.aggregate([
  {
    $setWindowFields: {
      partitionBy: "$category",
      sortBy: { price: -1 },
      output: {
        rank: { $denseRank: {} }
      }
    }
  },
  { $match: { rank: { $lte: 3 } } },
  {
    $project: {
      _id: 0,
      category: "$category",
      name: "$name",
      price: "$price"
    }
  },
  { $sort: { category: 1, price: -1, name: 1 } }
]).toArray();

print(JSON.stringify(result));