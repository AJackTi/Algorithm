SELECT e.name AS Employee
FROM Employee e
WHERE e.salary > (
        SELECT salary
        FROM Employee
        WHERE id = e.managerId
    )