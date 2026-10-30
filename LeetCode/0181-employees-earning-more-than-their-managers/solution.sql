-- Write your PostgreSQL query statement below
SELECT e.name as Employee
FROM Employee as e 
INNER JOIN Employee as c ON e.managerId = c.id 
WHERE e.salary > c.salary;

