# Write your MySQL query statement below

WITH ProductCount AS (
    -- Step 1: Count total unique products
    SELECT COUNT(*) AS total_products
    FROM Product
)

SELECT c.customer_id
FROM Customer c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = (SELECT total_products FROM ProductCount);