-- Write your PostgreSQL query statement below
SELECT p1.email as Email
FROM Person as p1
LEFT JOIN Person as p2 ON p1.id = p2.id
GROUP BY p1.email
HAVING COUNT(p1.email) > 1;
