WITH FirstSales AS (
    -- Step 1: Get the first year each product was sold
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

-- Step 2: Get quantity and price for the first year of each product
SELECT s.product_id, 
       f.first_year, 
       s.quantity, 
       s.price
FROM Sales s
JOIN FirstSales f 
ON s.product_id = f.product_id 
AND s.year = f.first_year;