---
name: "SQL Advanced"
description: "Master window functions, CTEs, subqueries, and query optimization for complex analytical queries"
category: "Databases/SQL"
level: "Intermediate-Advanced"
duration: "4-6 weeks"
---

# SQL Advanced

## Quick Start

Advanced SQL enables complex analytical queries without leaving the database. In your first week, you'll write CTEs and understand window functions. By week four, you'll optimize queries to run seconds instead of minutes on large datasets.

**First Task (30 minutes):**
1. Write a CTE (WITH clause) to calculate monthly totals
2. Use a window function to rank customers by spending
3. Identify a slow query and add an index
4. Compare execution time before and after optimization

## Key Concepts

### 1. Common Table Expressions (CTEs)
**What it is:** Temporary named result sets that make complex queries readable and reusable.

**Example:**
```sql
-- Simple CTE
WITH monthly_sales AS (
  SELECT DATE_TRUNC('month', order_date) as month,
         SUM(amount) as sales
  FROM orders
  GROUP BY DATE_TRUNC('month', order_date)
)
SELECT month, sales,
       LAG(sales) OVER (ORDER BY month) as prev_month_sales,
       ROUND(100.0 * (sales - LAG(sales) OVER (ORDER BY month))
             / LAG(sales) OVER (ORDER BY month), 2) as pct_growth
FROM monthly_sales
ORDER BY month DESC;

-- Multiple CTEs (with dependencies)
WITH customer_lifetime_value AS (
  SELECT customer_id, SUM(amount) as total_spent
  FROM orders
  GROUP BY customer_id
),
high_value_customers AS (
  SELECT customer_id, total_spent
  FROM customer_lifetime_value
  WHERE total_spent > 10000
)
SELECT c.customer_name, hvc.total_spent
FROM high_value_customers hvc
JOIN customers c ON hvc.customer_id = c.customer_id
ORDER BY total_spent DESC;
```

**When to use:** Breaking complex logic into steps, avoiding subquery nesting, improving readability.

### 2. Window Functions
**What it is:** Functions that calculate results across a set of rows (window) without collapsing results.

**Key window functions:**
```sql
-- ROW_NUMBER: Unique rank (handles ties with different numbers)
SELECT customer_id, order_amount,
       ROW_NUMBER() OVER (ORDER BY order_amount DESC) as rank
FROM orders;

-- RANK: Dense ranking (ties get same rank)
SELECT customer_id, order_amount,
       RANK() OVER (PARTITION BY region ORDER BY order_amount DESC) as rank
FROM orders;

-- LAG/LEAD: Access previous/next row values
SELECT order_date, amount,
       LAG(amount) OVER (ORDER BY order_date) as prev_order,
       LEAD(amount) OVER (ORDER BY order_date) as next_order,
       amount - LAG(amount) OVER (ORDER BY order_date) as change
FROM orders;

-- Running totals with SUM window
SELECT order_date, amount,
       SUM(amount) OVER (ORDER BY order_date
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total
FROM orders;

-- Percentile ranking
SELECT customer_id, spending,
       PERCENT_RANK() OVER (ORDER BY spending) as percentile
FROM customer_spending
WHERE percentile >= 0.75;
```

**Partition clause:**
```sql
-- Calculate metrics per region
SELECT region, month, sales,
       AVG(sales) OVER (PARTITION BY region) as region_avg,
       SUM(sales) OVER (PARTITION BY region, month) as region_month_total
FROM regional_sales;
```

### 3. Subqueries & Derived Tables
**What it is:** Queries nested within queries to solve multi-step problems.

**Example:**
```sql
-- Scalar subquery (returns single value)
SELECT order_id, amount,
       (SELECT AVG(amount) FROM orders) as avg_order
FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders);

-- Derived table (subquery in FROM clause)
SELECT top_regions.region, top_regions.sales,
       ROUND(100.0 * top_regions.sales / (SELECT SUM(sales) FROM regional_sales), 2) as pct_of_total
FROM (
  SELECT region, SUM(sales) as sales
  FROM sales
  GROUP BY region
) as top_regions
WHERE top_regions.sales > 50000
ORDER BY sales DESC;

-- Correlated subquery (slower, use with caution)
SELECT customer_id, order_amount
FROM orders o1
WHERE order_amount > (
  SELECT AVG(order_amount)
  FROM orders o2
  WHERE o2.customer_id = o1.customer_id  -- Correlation
);
```

### 4. Query Optimization
**What it is:** Techniques to make queries faster without changing results.

**Key optimization strategies:**
```sql
-- 1. Use indexes on frequently filtered columns
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_order_date ON orders(order_date);

-- 2. Avoid functions on indexed columns (prevents index use)
-- BAD: WHERE YEAR(order_date) = 2024
-- GOOD: WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'

-- 3. Filter early with WHERE (reduce rows before GROUP BY)
SELECT customer_id, COUNT(*) as orders
FROM orders
WHERE order_date >= '2023-01-01'  -- Filter first
GROUP BY customer_id;

-- 4. Use EXISTS instead of IN for large subqueries
-- Better performance:
SELECT customer_name FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);

-- 5. Pre-aggregate with CTEs instead of subquery per row
WITH customer_stats AS (
  SELECT customer_id, COUNT(*) as order_count
  FROM orders
  GROUP BY customer_id
)
SELECT c.customer_name, cs.order_count
FROM customer_stats cs
JOIN customers c ON cs.customer_id = c.customer_id;
```

**Check execution plan:**
```sql
-- PostgreSQL
EXPLAIN ANALYZE SELECT ...;

-- MySQL
EXPLAIN SELECT ...;

-- SQL Server
SET STATISTICS IO ON; SET STATISTICS TIME ON;
```

### 5. Advanced Aggregations
**What it is:** Complex aggregation patterns for sophisticated analysis.

**Example:**
```sql
-- FILTER clause (conditional aggregation)
SELECT product_id,
       COUNT(*) as total_orders,
       COUNT(*) FILTER (WHERE status = 'completed') as completed_orders,
       SUM(amount) FILTER (WHERE status = 'completed') as completed_revenue
FROM orders
GROUP BY product_id;

-- Pivot/Crosstab (in PostgreSQL)
SELECT *
FROM crosstab('
  SELECT region, month, SUM(sales)
  FROM sales GROUP BY region, month'
) AS result(region text, jan numeric, feb numeric, mar numeric);

-- Multiple GROUP BY levels
SELECT
  region, product_category, NULL as product,
  SUM(sales) as sales
FROM sales
GROUP BY region, product_category
UNION ALL
SELECT
  region, product_category, product,
  SUM(sales)
FROM sales
GROUP BY region, product_category, product;
```

## Tools and Resources

**Query Analysis Tools:**
- pgAdmin/DBeaver: Visual query execution plans
- SQL Server Management Studio: Execution plan analyzer
- Database vendor documentation

**Learning Resources:**
- Advanced SQL for Data Analytics (Udemy courses)
- SQL Window Functions Tutorial (Mode Analytics)
- Database optimization guides (PostgreSQL docs, MySQL docs)

**Performance Monitoring:**
- Slow query logs: Identify problematic queries
- Query execution plans: Understand WHERE time is spent
- EXPLAIN ANALYZE: Detailed query performance metrics

## Best Practices

1. **CTEs for Readability:** Use WITH clauses to make complex queries understandable
2. **Minimize Data Movement:** Filter early, aggregate efficiently
3. **Index Strategically:** Index columns used in WHERE, JOIN, GROUP BY
4. **Avoid N+1 Queries:** Fetch all data in one query, not multiple loops
5. **Use Appropriate Data Types:** DECIMAL for money, INT for IDs
6. **Partition Window Functions:** PARTITION BY for meaningful comparisons
7. **Test on Sample Data:** Verify query logic on smaller subset first
8. **Monitor Performance:** Track slow queries and optimize regularly
9. **Document Complex Logic:** Explain CTEs, window functions, and join conditions

## Next Steps

1. **Week 1-2:** Master CTEs and understand query structure
2. **Week 2-3:** Learn window functions and running calculations
3. **Week 3-4:** Apply optimization techniques to slow queries
4. **Week 4-5:** Build complex analytical dashboards with advanced SQL
5. **Week 5-6:** Optimize and maintain production queries
6. **After:** Move to Python for machine learning, or database administration
7. **Progression:** SQL Advanced → Python/R for statistical analysis → Machine Learning
