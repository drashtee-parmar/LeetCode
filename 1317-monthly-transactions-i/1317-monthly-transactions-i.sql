# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month 
        , country
        , COUNT(trans_date) AS trans_count 
        , SUM(case when state ='approved' THEN 1 ELSE 0 END)  
         AS approved_count
        , SUM(amount) AS trans_total_amount
        , SUM(case when state ='approved' then amount ELSE 0 END) 
        AS approved_total_amount       
FROM Transactions 
GROUP BY month,country