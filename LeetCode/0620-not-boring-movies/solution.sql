-- Write your PostgreSQL query statement below
SELECT c.id, c.movie, c.description, c.rating
FROM Cinema c
WHERE c.description != 'boring' and c.id % 2 = 1
ORDER BY c.rating desc

