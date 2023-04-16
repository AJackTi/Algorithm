# Write your MySQL query statement below
SELECT
    user_id AS buyer_id,
    join_date,
    sum(
        CASE
            WHEN order_id IS NOT NULL THEN 1
            ELSE 0
        END
    ) AS orders_in_2019
FROM users
    LEFT JOIN orders ON users.user_id = orders.buyer_id AND YEAR(order_date) = 2019
GROUP BY user_id, join_date
ORDER BY buyer_id