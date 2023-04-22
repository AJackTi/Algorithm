# Write your MySQL query statement below
SELECT id, count(*) AS num FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) AS friends_count
GROUP BY id
ORDER BY num DESC LIMIT 1;