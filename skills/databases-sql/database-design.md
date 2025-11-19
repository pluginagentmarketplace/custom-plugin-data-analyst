---
name: "Database Design"
description: "Learn normalization, indexing, schema design, and ER diagrams to build efficient databases"
category: "Databases/SQL"
level: "Intermediate"
duration: "4-5 weeks"
---

# Database Design

## Quick Start

Good database design prevents problems before they occur. In your first week, you'll learn normalization concepts and design your first schema. By week three, you'll understand when and where to add indexes and optimize performance at the design stage.

**First Task (30 minutes):**
1. Sketch an ER diagram for a simple business (e.g., online store)
2. Identify tables, columns, and relationships
3. Check for normalization issues (data redundancy)
4. Create the database using SQL CREATE TABLE statements

## Key Concepts

### 1. Normalization Forms
**What it is:** Process of organizing data to minimize redundancy and ensure data integrity.

**Normal Forms:**
```
First Normal Form (1NF):
- Each column contains atomic (indivisible) values
- NO: Product column with "Apple, Banana" (multiple values)
- YES: Separate rows for each product

Second Normal Form (2NF):
- Must be in 1NF
- Remove partial dependencies (non-key columns depend on entire primary key)
- NO: Product table with (product_id, supplier_id, supplier_name)
- YES: Separate Suppliers table referenced by product_id

Third Normal Form (3NF):
- Must be in 2NF
- Remove transitive dependencies (non-key columns depend on other non-key columns)
- NO: Employee table with (emp_id, salary, tax_rate, tax_amount)
- YES: Calculate tax_amount from salary, keep tax_rate in separate table

Boyce-Codd Normal Form (BCNF):
- Strict 3NF variant; rarely needed in practice
```

**Example normalization:**
```
BEFORE (Unnormalized):
Orders(order_id, customer_name, customer_email, product_name, quantity, price)

AFTER (3NF):
Customers(customer_id, name, email)
Products(product_id, name, price)
Orders(order_id, customer_id, order_date)
OrderItems(order_id, product_id, quantity)
```

### 2. Entity Relationship (ER) Diagrams
**What it is:** Visual representation of database structure showing entities and relationships.

**Relationship cardinality:**
```
One-to-One (1:1)
Customers --- has one --- Account
(Typically merge into single table)

One-to-Many (1:N)
Department --- has many --- Employees
(Common: Foreign key in Employees table)

Many-to-Many (N:N)
Students --- enrolls in --- Courses
(Requires junction table: StudentCourses)

Zero or One (0..1)
Customer --- may have --- VIP_Status

Zero or Many (0..*)
Department --- manages zero or many --- Projects
```

**ER Diagram Example (Text notation):**
```
Customers (PK: customer_id)
  customer_id (INT, PRIMARY KEY)
  name (VARCHAR)
  email (VARCHAR, UNIQUE)
  created_date (DATE)

Orders (PK: order_id, FK: customer_id)
  order_id (INT, PRIMARY KEY)
  customer_id (INT, FOREIGN KEY -> Customers)
  order_date (DATE)
  total_amount (DECIMAL)

OrderItems (PK: order_id + product_id, FK: order_id, product_id)
  order_id (INT, FOREIGN KEY -> Orders)
  product_id (INT, FOREIGN KEY -> Products)
  quantity (INT)
  price_at_order (DECIMAL)

Products (PK: product_id, FK: category_id)
  product_id (INT, PRIMARY KEY)
  name (VARCHAR)
  category_id (INT, FOREIGN KEY -> Categories)
  price (DECIMAL)
```

### 3. Indexing Strategy
**What it is:** Data structures that speed up query retrieval by allowing fast lookups.

**Index types:**
```sql
-- Single column index
CREATE INDEX idx_customers_email ON customers(email);

-- Composite index (multiple columns)
CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date);

-- Unique index (enforces uniqueness AND speeds up lookups)
CREATE UNIQUE INDEX idx_users_username ON users(username);

-- Full-text index (for text search)
CREATE FULLTEXT INDEX idx_products_description ON products(description);

-- Partial index (subset of rows - saves space)
CREATE INDEX idx_orders_active ON orders(customer_id)
WHERE status = 'active';
```

**When to index:**
- Columns frequently used in WHERE clauses
- Columns used in JOIN conditions
- Columns in GROUP BY or ORDER BY
- NOT: Columns with many NULL values, low cardinality (few distinct values)

**Index trade-offs:**
```
PROS: Faster queries
CONS: Slower inserts/updates, more storage

Solution: Index wisely - balance read vs. write performance
```

### 4. Key Constraints & Data Integrity
**What it is:** Rules that maintain data accuracy and consistency.

**Example:**
```sql
CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) NOT NULL,
  age INT CHECK (age >= 18),
  department_id INT NOT NULL REFERENCES departments(dept_id),
  created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Foreign key constraints
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT NOT NULL REFERENCES customers(customer_id)
    ON DELETE CASCADE,  -- Delete orders when customer deleted
  product_id INT REFERENCES products(product_id)
    ON DELETE SET NULL  -- Set NULL if product deleted
);
```

### 5. Schema Design Patterns
**What it is:** Common solutions to recurring design problems.

**Star Schema (for data warehousing):**
```
Central Fact table with foreign keys to dimension tables
Facts: sales, metrics (fact_sales)
Dimensions: time, products, customers (dim_date, dim_product, dim_customer)
Optimized for analytical queries
```

**Slowly Changing Dimensions (SCD):**
```
Type 1: Overwrite old data (simple, loses history)
Type 2: Add new row with version (maintains history, more complex)
Type 3: Keep current + previous (balance between 1 and 2)
```

**Example:**
```
Fact Table (fact_sales):
  sale_id, date_id, product_id, customer_id, amount

Dimension Tables:
  dim_date: date_id, date, month, quarter, year
  dim_product: product_id, product_name, category, price
  dim_customer: customer_id, customer_name, region, segment
```

## Tools and Resources

**ER Diagram Tools:**
- Lucidchart: Cloud-based diagramming (free tier available)
- Draw.io: Free, open-source
- DBeaver: Built-in ER diagram generation
- MySQL Workbench: Database design tool
- PostgreSQL pgAdmin: Schema visualization

**SQL Tools:**
- DataGrip: Professional IDE
- DBeaver Community: Free database tool
- Adminer: Web-based management

**Learning Resources:**
- Database Design Fundamentals (Pluralsight courses)
- Normalization Tutorial (Mode Analytics)
- ER Diagram Best Practices (various databases)

## Best Practices

1. **Start with Normalization:** Design to 3NF minimum, denormalize only for performance
2. **Use Surrogate Keys:** Auto-increment INT for primary keys (better than natural keys)
3. **Enforce Referential Integrity:** Use FOREIGN KEY constraints, not application logic
4. **Name Consistently:** Use singular table names (customer, not customers), clear column names
5. **Use Appropriate Data Types:** Date, Timestamp for dates; DECIMAL for money; INT for IDs
6. **Plan for Growth:** Consider future data volume when designing indexes, partitioning
7. **Document Schema:** Add comments explaining tables, columns, relationships
8. **Test Constraints:** Verify data integrity rules catch bad data
9. **Version Your Schema:** Track schema changes with migration scripts
10. **Denormalize Carefully:** Only when query performance metrics show need

## Next Steps

1. **Week 1:** Learn normalization and ER diagram basics
2. **Week 2:** Design a complete schema for a realistic scenario
3. **Week 3:** Implement with CREATE TABLE, constraints, indexes
4. **Week 4:** Practice identifying normalization issues and refactoring
5. **Week 5:** Learn advanced patterns (star schema, SCD)
6. **After:** Move to SQL Advanced for optimization, or Data Warehousing
7. **Progression:** Database Design → Data Warehousing → Cloud Databases (BigQuery, Redshift)
