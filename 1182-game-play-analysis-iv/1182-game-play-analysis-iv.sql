# Write your MySQL query statement below
SELECT Round(Count(DISTINCT player_id) / 
(
    SELECT Count(DISTINCT player_id)
    FROM   activity), 2) AS fraction
FROM   activity
WHERE  ( player_id, 
        Date_sub(event_date, interval 1 day) ) IN
              (SELECT 
                    player_id,
                    Min(event_date) AS first_login
               FROM   activity
              GROUP  BY player_id) 