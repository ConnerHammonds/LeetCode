-- Write your PostgreSQL query statement below
Select a1.machine_id, ROUND(AVG(CAST(a2.timestamp - a1.timestamp AS DECIMAL)), 3) as processing_time
FROM Activity a1
INNER JOIN Activity a2 ON a1.machine_id = a2.machine_id and a1.process_id = a2.process_id
and a1.activity_type = 'start' and a2.activity_type = 'end'
GROUP BY a1.machine_id
ORDER BY a1.machine_id;
