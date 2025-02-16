# Write your MySQL query statement below
SELECT DISTINCT ( email ) AS Email
FROM   person
GROUP  BY email
HAVING Count(email) > 1 