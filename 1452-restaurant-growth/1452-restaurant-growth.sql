# Write your MySQL query statement below
WITH 
DailyTotals AS (
    SELECT
        visited_on,
        SUM(amount) AS daily_amount
    FROM
        Customer
    GROUP BY
        visited_on
),
RunningTotals AS (
  SELECT
        visited_on,
        daily_amount,
        SUM(daily_amount) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS running_total,
        COUNT(*) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as running_count
    FROM
        DailyTotals
)
SELECT
    visited_on,
    running_total as amount,
    ROUND(running_total * 1.0 / running_count, 2) AS average_amount
FROM
    RunningTotals
WHERE running_count = 7
ORDER BY
    visited_on;