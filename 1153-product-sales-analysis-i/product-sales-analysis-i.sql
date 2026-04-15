/* Write your PL/SQL query statement below */
SELECT product.product_name as product_name, sales.year as year,sales.price as price
FROM sales
INNER JOIN product
ON product.product_id = sales.product_id;