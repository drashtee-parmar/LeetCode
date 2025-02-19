# Write your MySQL query statement below
select e.name
from Employee e
join Employee m on e.id = m.managerId
group by e.id, e.name
having count(m.id) >= 5
