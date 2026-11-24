-- Overall sales KPIs
SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(revenue_eur), 2) AS total_revenue_eur,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(revenue_eur) / COUNT(DISTINCT order_id), 2) AS average_order_value_eur
FROM retail_sales;

-- Monthly revenue trend
SELECT
    strftime('%Y-%m', order_date) AS order_month,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(revenue_eur), 2) AS total_revenue_eur
FROM retail_sales
GROUP BY order_month
ORDER BY order_month;

-- Revenue by product category
SELECT
    product_category,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS units_sold,
    ROUND(SUM(revenue_eur), 2) AS total_revenue_eur
FROM retail_sales
GROUP BY product_category
ORDER BY total_revenue_eur DESC;

-- Revenue by region
SELECT
    region,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(revenue_eur), 2) AS total_revenue_eur,
    ROUND(AVG(revenue_eur), 2) AS average_order_value_eur
FROM retail_sales
GROUP BY region
ORDER BY total_revenue_eur DESC;

-- Top 10 products by revenue
SELECT
    product_name,
    product_category,
    SUM(quantity) AS units_sold,
    ROUND(SUM(revenue_eur), 2) AS total_revenue_eur
FROM retail_sales
GROUP BY product_name, product_category
ORDER BY total_revenue_eur DESC
LIMIT 10;
