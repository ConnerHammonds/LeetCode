-- Write your PostgreSQL query statement below
SELECT v.customer_id, COUNT(v.visit_id) as count_no_trans
FROM Visits as v
LEFT JOIN Transactions as t ON t.visit_id = v.visit_id
WHERE t.transaction_id is null
GROUP BY v.customer_id;

