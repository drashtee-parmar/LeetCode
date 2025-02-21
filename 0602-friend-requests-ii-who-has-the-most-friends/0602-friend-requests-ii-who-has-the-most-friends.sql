# Write your MySQL query statement below
SELECT fc.id, fc.num
FROM (
    SELECT user_id AS id, COUNT(*) AS num
    FROM (
        SELECT requester_id AS user_id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id AS user_id FROM RequestAccepted
    ) AS all_friends
    GROUP BY user_id
) AS fc
JOIN (
    SELECT MAX(num) AS max_num
    FROM (
        SELECT user_id AS id, COUNT(*) AS num
        FROM (
            SELECT requester_id AS user_id FROM RequestAccepted
            UNION ALL
            SELECT accepter_id AS user_id FROM RequestAccepted
        ) AS all_friends
        GROUP BY user_id
    ) AS counts
) AS max_counts ON fc.num = max_counts.max_num;