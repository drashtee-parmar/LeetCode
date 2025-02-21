# Write your MySQL query statement below
SELECT 
    (SELECT DISTINCT salary 
     FROM Employee 
     ORDER BY salary DESC 
     LIMIT 1 OFFSET 1) -- Skips the highest salary and selects the second highest.
     AS SecondHighestSalary;
