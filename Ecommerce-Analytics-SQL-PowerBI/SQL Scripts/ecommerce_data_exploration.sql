-- Data Exploration and testing

-- Total revenue by product using SELECT, FROM, JOIN, and GROUP BY
SELECT 
  p.category,
  SUM(oi.quantity * oi.item_price) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category;

-- Top 5 customers by spending adding ORDER BY and LIMIT

SELECT 
  c.first_name, c.last_name,
  SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 5;

-- Return Rate by product adding aggregators and LEFT Join

SELECT 
  p.product_name,
  COUNT(r.return_id) AS num_returns,
  COUNT(oi.order_item_id) AS total_sold,
  ROUND(COUNT(r.return_id) / COUNT(oi.order_item_id) * 100, 2) AS return_rate_percent
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN returns r ON oi.order_item_id = r.order_item_id
GROUP BY p.product_id;


-- Challenge Queries and Practice

-- Customer Lifetime Value

SELECT 
  c.customer_id,
  c.first_name,
  c.last_name,
  ROUND(SUM(o.total_amount), 2) AS lifetime_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY lifetime_value DESC
LIMIT 10;


-- Monthly Revenue Trend

SELECT 
  DATE_FORMAT(order_date, '%Y-%m') AS month,
  ROUND(SUM(total_amount), 2) AS monthly_revenue
FROM orders
GROUP BY month
ORDER BY month;

-- Top Returned Products

SELECT 
  p.product_name,
  COUNT(r.return_id) AS num_returns
FROM returns r
JOIN order_items oi ON r.order_item_id = oi.order_item_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY num_returns DESC
LIMIT 5;


-- Return rate by Category

SELECT 
  p.category,
  COUNT(r.return_id) AS returns,
  COUNT(oi.order_item_id) AS sold,
  ROUND(COUNT(r.return_id) / COUNT(oi.order_item_id) * 100, 2) AS return_rate
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN returns r ON oi.order_item_id = r.order_item_id
GROUP BY p.category;
 