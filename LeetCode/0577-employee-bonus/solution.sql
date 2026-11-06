-- Write your PostgreSQL query statement below
SELECT e.name, b.bonus
FROM Employee as e
FULL JOIN BONUS as b ON b.empId = e.empId
WHERE b.bonus < 1000 or b.bonus is null;
