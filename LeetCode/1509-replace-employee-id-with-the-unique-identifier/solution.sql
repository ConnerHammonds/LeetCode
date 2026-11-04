-- Write your PostgreSQL query statement below
SELECT e.name, u.unique_id
FROM Employees as e
LEFT JOIN EmployeeUNI as u ON u.id = e.id;

