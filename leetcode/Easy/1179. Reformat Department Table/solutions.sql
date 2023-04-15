# Write your MySQL query statement below
SELECT
    id,
    SUM(
        CASE
            WHEN month = 'jan' THEN revenue
            ELSE null
        END
    ) AS Jan_Revenue,
    sum(
        CASE
            WHEN month = 'feb' THEN revenue
            ELSE null
        END
    ) AS Feb_Revenue,
    sum(
        CASE
            WHEN month = 'mar' THEN revenue
            ELSE null
        END
    ) AS Mar_Revenue,
    sum(
        CASE
            WHEN month = 'apr' THEN revenue
            ELSE null
        END
    ) AS Apr_Revenue,
    sum(
        CASE
            WHEN month = 'may' THEN revenue
            ELSE null
        END
    ) AS May_Revenue,
    sum(
        CASE
            WHEN month = 'jun' THEN revenue
            ELSE null
        END
    ) AS Jun_Revenue,
    sum(
        CASE
            WHEN month = 'jul' THEN revenue
            ELSE null
        END
    ) AS Jul_Revenue,
    sum(
        CASE
            WHEN month = 'aug' THEN revenue
            ELSE null
        END
    ) AS Aug_Revenue,
    sum(
        CASE 
            WHEN month = 'sep' THEN revenue
            ELSE null
        END
    ) AS Sep_Revenue,
    sum(
        CASE 
            WHEN month = 'oct' THEN revenue
            ELSE null
        END
    ) AS Oct_Revenue,
    sum(
        CASE 
            WHEN month = 'nov' THEN revenue
            ELSE null
        END
    ) AS Nov_Revenue,
    sum(
        CASE
            WHEN month = 'dec' THEN revenue
            ELSE null
        END
    ) AS Dec_Revenue
FROM department
GROUP BY id
ORDER BY id