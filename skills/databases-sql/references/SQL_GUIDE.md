# SQL Guide

## Common Patterns
```sql
-- Aggregation
SELECT category, COUNT(*), AVG(amount)
FROM orders GROUP BY category;

-- Window Functions
SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY date) as rn
FROM orders;

-- CTE
WITH monthly AS (SELECT DATE_TRUNC('month', date) as m FROM orders)
SELECT m, COUNT(*) FROM monthly GROUP BY m;
```
