# Write your MySQL query statement below
-- SELECT MAX(num) AS num
-- FROM (
--     SELECT num
--     FROM MyNumbers
--     GROUP BY num
--     HAVING COUNT(num) = 1
-- ) AS single_numbers;


select 
    max(num) as num 
from MyNumbers
where num in (
    select num 
    from MyNumbers
    group by num
    having count(num) = 1
)