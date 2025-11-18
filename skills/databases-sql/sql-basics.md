---
name: "SQL Basics"
description: "Learn core SQL commands including SELECT, WHERE, JOIN, GROUP BY, and aggregation queries for data exploration"
category: "Databases/SQL"
level: "Beginner"
duration: "3-4 weeks"
---

# SQL Basics

## Quick Start

SQL is the language of data analysis. Within your first week, you'll write SELECT queries, filter with WHERE, and join tables. By week three, you'll aggregate data with GROUP BY and create reports without leaving the database.

**First Task (20 minutes):**
1. Access a sample database (e.g., free tier PostgreSQL, SQLite, or online sandbox)
2. Explore table structure with `SELECT * FROM table_name LIMIT 10`
3. Write a query: Find total sales by product category
4. Export results to CSV

## Key Concepts

### 1. SELECT & Filtering Basics
**What it is:** Retrieving specific columns and rows from database tables.

**Example:**
```sql
-- Basic selection
SELECT product_name, price FROM products;

-- With filtering
SELECT customer_name, order_amount
FROM orders
WHERE order_amount > 1000;

-- Multiple conditions
SELECT * FROM employees
WHERE department = 'Sales' AND salary > 50000;

-- Pattern matching
SELECT * FROM customers
WHERE email LIKE '%@gmail.com';
```

**When to use:** Exploring data, answering specific questions, building datasets for analysis.

### 2. JOIN Operations
**What it is:** Combining data from multiple tables based on common keys.

**Join types:**
```sql
-- INNER JOIN: Only matching rows
SELECT o.order_id, c.customer_name, o.amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;

-- LEFT JOIN: All rows from left table + matches from right
SELECT p.product_name, COUNT(o.order_id) as times_ordered
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_id;

-- RIGHT JOIN: All rows from right table + matches from left
SELECT * FROM orders o RIGHT JOIN returns r ON o.order_id = r.order_id;

-- FULL JOIN: All rows from both tables
SELECT * FROM suppliers s FULL JOIN products p ON s.supplier_id = p.supplier_id;
```

**When to use:** Combining customer, order, and product data; enriching datasets with reference information.

### 3. GROUP BY & Aggregation
**What it is:** Summarizing data by grouping rows and calculating aggregate metrics.

**Example:**
```sql
-- Total sales by month
SELECT DATE_TRUNC('month', order_date) as month,
       SUM(amount) as total_sales
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month DESC;

-- Customer metrics
SELECT customer_id,
       COUNT(*) as order_count,
       AVG(amount) as avg_order,
       MAX(amount) as max_order,
       SUM(amount) as total_spent
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 5
ORDER BY total_spent DESC;

-- Multi-level grouping
SELECT region, product_category,
       SUM(sales) as revenue,
       COUNT(DISTINCT customer_id) as customers
FROM sales
GROUP BY region, product_category;
```

**Common Aggregate Functions:**
- `COUNT(*)` - Count rows
- `SUM(column)` - Total values
- `AVG(column)` - Average value
- `MIN/MAX(column)` - Minimum/maximum
- `COUNT(DISTINCT column)` - Unique count
- `STRING_AGG(column)` - Concatenate strings

### 4. Filtering Grouped Data with HAVING
**What it is:** WHERE filters rows before grouping; HAVING filters groups after aggregation.

**Example:**
```sql
-- Find products where total sales exceed $100,000
SELECT product_id, product_name, SUM(amount) as total_sales
FROM order_items
GROUP BY product_id, product_name
HAVING SUM(amount) > 100000
ORDER BY total_sales DESC;

-- Customers with more than 10 orders AND spending over $5,000
SELECT customer_id, COUNT(*) as orders, SUM(amount) as total
FROM orders
WHERE order_date >= '2023-01-01'
GROUP BY customer_id
HAVING COUNT(*) > 10 AND SUM(amount) > 5000;
```

### 5. Sorting & Limiting Results
**What it is:** Ordering results and restricting output for readability and performance.

**Example:**
```sql
-- Top 10 customers by spending
SELECT customer_name, SUM(amount) as total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;

-- Ascending sort with multiple columns
SELECT * FROM products
ORDER BY category ASC, price DESC
LIMIT 20 OFFSET 40;  -- Pagination: skip 40, take 20
```

## Tools and Resources

**SQL Databases (Free Tier):**
- PostgreSQL: Powerful, open-source (postgresql.org)
- SQLite: Lightweight, file-based (sqlite.org)
- MySQL: Widely used (mysql.com)
- Snowflake: Cloud DW (free trial)
- BigQuery: Google's data warehouse (free tier)

**Learning Platforms:**
- SQLZoo.net: Interactive SQL tutorial
- Mode Analytics SQL Tutorial: Free comprehensive course
- LeetCode: SQL challenges for practice
- HackerRank: SQL problems

**Tools:**
- DBeaver: Free GUI for databases
- DataGrip: JetBrains IDE for SQL
- Adminer: Web-based database tool
- pgAdmin: PostgreSQL management

## Best Practices

1. **Use Aliases for Clarity:** `SELECT o.order_id FROM orders o` is clearer than ambiguous references
2. **Qualify All Columns in JOINs:** Specify table.column to avoid ambiguity
3. **Index Your Queries:** Add indexes on frequently filtered columns for speed
4. **LIMIT During Development:** Test queries with LIMIT before running on millions of rows
5. **Comment Complex Logic:** Explain GROUP BY, JOIN conditions with comments
6. **Avoid SELECT *:** Specify columns you need; SELECT * is slower and unclear
7. **Use Proper Data Types:** Store dates as DATE, numbers as numeric types
8. **Understand NULL Logic:** NULL values behave unexpectedly (NULL != anything, even NULL)
9. **Test Edge Cases:** Check for duplicates, nulls, and unexpected values

## Next Steps

1. **Week 1:** Master SELECT, WHERE, and basic filtering
2. **Week 2:** Understand JOINs and multi-table queries
3. **Week 3:** Learn GROUP BY, aggregation, and HAVING
4. **Week 4:** Combine concepts into complex reports
5. **After:** Move to SQL Advanced (CTEs, window functions)
6. **Progression:** SQL Basics → SQL Advanced → Python for data transformation
