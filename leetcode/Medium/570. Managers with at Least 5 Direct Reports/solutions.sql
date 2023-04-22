SELECT name FROM Employee 
WHERE id IN (
    SELECT managerId FROM Employee
    WHERE managerId <> 'None'
    GROUP BY managerId
    HAVING count(1) >= 5
)