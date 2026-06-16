-- Clean start (no need for separate tear_down)
DROP TABLE IF EXISTS Employee, Department CASCADE;

-- Department table
CREATE TABLE Department (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Employee table
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    salary INT,
    departmentId INT,
    FOREIGN KEY (departmentId) REFERENCES Department(id)
);

-- Official sample data (from LeetCode 185)
INSERT INTO Department (id, name) VALUES
(1, 'IT');

INSERT INTO Employee (id, name, salary, departmentId) VALUES
(1, 'Joe',   85000, 1),
(2, 'Henry', 80000, 1),
(3, 'Sam',   60000, 1),
(4, 'Max',   90000, 1),
(5, 'Janet', 69000, 1),
(6, 'Randy', 85000, 1),
(7, 'Will',  70000, 1);