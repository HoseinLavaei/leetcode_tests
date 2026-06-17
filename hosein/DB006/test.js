db = db.getSiblingDB('leetcode');

var result = db.employees.aggregate([
  // 1. Compute average salary per department (subquery) using $lookup + pipeline
  {
    $lookup: {
      from: "employees",
      let: { deptId: "$departmentId" },
      pipeline: [
        { $match: { $expr: { $eq: ["$departmentId", "$$deptId"] } } },
        { $group: { _id: null, avgSal: { $avg: "$salary" } } }
      ],
      as: "deptAvgInfo"
    }
  },
  // 2. Unwind the array (it will have exactly one element)
  { $unwind: "$deptAvgInfo" },
  // 3. Add a field for department average
  { $addFields: { dept_avg: { $round: ["$deptAvgInfo.avgSal", 2] } } },
  // 4. Filter only employees with salary > dept average
  { $match: { $expr: { $gt: ["$salary", "$dept_avg"] } } },
  // 5. Lookup department name from departments collection
  {
    $lookup: {
      from: "departments",
      localField: "departmentId",
      foreignField: "_id",
      as: "deptInfo"
    }
  },
  { $unwind: "$deptInfo" },
  // 6. Project final fields
  {
    $project: {
      _id: 0,
      department: "$deptInfo.name",
      employee: "$name",
      salary: 1,
      dept_avg: 1
    }
  },
  // 7. Sort
  { $sort: { department: 1, salary: -1 } }
]).toArray();

print(JSON.stringify(result));