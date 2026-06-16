-- Clean start
DROP TABLE IF EXISTS Employee CASCADE;

-- Create tables
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    salary INT
);

-- Insert sample data
Insert into Employee (id, salary) VALUES
(1,100),
(2,200),
(3,300);