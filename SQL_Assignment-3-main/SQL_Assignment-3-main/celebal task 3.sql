
CREATE DATABASE IF NOT EXISTS superstore_db;
USE superstore_db;

-- Preview Data
SELECT * FROM superstore_raw LIMIT 10;
-- STEP 1 : CREATE DIMENSION TABLES

 

CREATE TABLE orders AS
SELECT DISTINCT
`Order ID` AS order_id,
`Order Date` AS order_date,
`Ship Date` AS ship_date,
`Ship Mode` AS ship_mode,
`Customer ID` AS customer_id,
Sales,
Quantity,
Discount,
Profit
FROM superstore_raw;

CREATE TABLE products AS
SELECT DISTINCT
`Product ID` AS product_id,
`Product Name` AS product_name,
Category,
`Sub-Category` AS sub_category
FROM superstore_raw;

-- =================================
-- STEP 2 : SUBQUERY QUESTIONS
-- =================================

-- Orders having sales greater than average sales
SELECT order_id, customer_id, Sales
FROM orders
WHERE Sales > (
SELECT AVG(Sales)
FROM orders
);

-- Highest sales order for every customer
SELECT o.*
FROM orders o
WHERE o.Sales = (
SELECT MAX(Sales)
FROM orders
WHERE customer_id = o.customer_id
);

-- =================================
-- STEP 3 : CTE QUESTIONS
-- =================================

WITH sales_summary AS
(
SELECT customer_id,
SUM(Sales) AS total_sales
FROM orders
GROUP BY customer_id
)
SELECT *
FROM sales_summary;

WITH sales_summary AS
(
SELECT customer_id,
SUM(Sales) AS total_sales
FROM orders
GROUP BY customer_id
)
SELECT *
FROM sales_summary
WHERE total_sales >
(
SELECT AVG(total_sales)
FROM sales_summary
);

-- =================================
-- STEP 4 : WINDOW FUNCTIONS
-- =================================

WITH sales_summary AS
(
SELECT customer_id,
SUM(Sales) AS total_sales
FROM orders
GROUP BY customer_id
)
SELECT customer_id,
total_sales,
DENSE_RANK() OVER(ORDER BY total_sales DESC) AS customer_rank
FROM sales_summary;

SELECT customer_id,
order_id,
Sales,
ROW_NUMBER() OVER(
PARTITION BY customer_id
ORDER BY Sales DESC
) AS order_sequence
FROM orders;

WITH sales_summary AS
(
SELECT customer_id,
SUM(Sales) AS total_sales
FROM orders
GROUP BY customer_id
)
SELECT *
FROM
(
SELECT customer_id,
total_sales,
ROW_NUMBER() OVER(ORDER BY total_sales DESC) AS rn
FROM sales_summary
) ranked_customers
WHERE rn <= 3;


-- FINAL QUERY
-- JOIN + CTE + WINDOW FUNCTION

WITH customer_sales AS
(
SELECT customer_id,
SUM(Sales) AS total_sales
FROM orders
GROUP BY customer_id
)
SELECT
c.customer_name,
customer_sales.total_sales,
DENSE_RANK() OVER(
ORDER BY customer_sales.total_sales DESC
) AS sales_rank
FROM customer_sales
INNER JOIN customers c
ON customer_sales.customer_id = c.customer_id
ORDER BY sales_rank;

-- MINI PROJECT : CUSTOMER INSIGHTS

-- Top 5 Customers
SELECT customer_name,
SUM(Sales) AS total_sales
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 5;

-- Bottom 5 Customers

SELECT customer_name,
SUM(Sales) AS total_sales
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY customer_name
ORDER BY total_sales ASC
LIMIT 5;

-- Customers with only one order
SELECT c.customer_name,
COUNT(DISTINCT o.order_id) AS order_count
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
HAVING order_count = 1;

-- Customers with above-average sales
WITH customer_sales AS
(
SELECT customer_id,
SUM(Sales) AS total_sales
FROM orders
GROUP BY customer_id
)
SELECT c.customer_name,
cs.total_sales
FROM customer_sales cs
JOIN customers c
ON cs.customer_id = c.customer_id
WHERE cs.total_sales >
(
SELECT AVG(total_sales)
FROM customer_sales
);

-- Highest Order Value Per Customer
SELECT c.customer_name,
MAX(o.Sales) AS highest_order_value
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY highest_order_value DESC;
