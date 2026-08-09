SELECT e.name, b.bonus

FROM Employee AS e
LEFT JOIN Bonus AS b
ON e.empId = b.empId
WHERE  e.empId = b.empId AND b.bonus < 1000 OR b.bonus IS NULL

