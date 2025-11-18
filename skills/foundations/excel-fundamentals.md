---
name: "Excel Fundamentals"
description: "Master core Excel skills including formulas, pivot tables, VLOOKUP, and data cleaning techniques for effective data analysis"
category: "Foundations"
level: "Beginner"
duration: "4-6 weeks"
---

# Excel Fundamentals

## Quick Start

Excel is the foundational tool for data analysts. In your first session, you'll create a spreadsheet, enter data, write basic formulas, and format cells. By the end of week one, you'll handle real datasets with cleaning, sorting, and filtering.

**First Task (15 minutes):**
1. Open Excel and create a new workbook
2. Enter sample sales data (date, product, quantity, price)
3. Create a formula to calculate total sales (quantity × price)
4. Apply conditional formatting to highlight top performers

## Key Concepts

### 1. Formula Fundamentals
**What it is:** Expressions that perform calculations or manipulate data in cells.

**Example:**
```
=SUM(A1:A10)           # Sum range
=AVERAGE(B2:B20)       # Calculate average
=IF(C5>100, "Yes", "No")  # Conditional logic
=CONCATENATE(A1, " ", B1)  # Join text
```

**When to use:** Whenever you need to automate calculations or create dynamic references instead of hardcoding values.

### 2. Pivot Tables
**What it is:** Dynamic summaries that automatically organize and summarize large datasets by dimensions and metrics.

**Example:**
```
Raw data: Date, Product, Region, Sales
Pivot table:
  Rows: Product
  Columns: Region
  Values: SUM(Sales)
Result: Sales by Product and Region cross-tabulation
```

**When to use:** Analyzing sales by category/region, summarizing customer data, trend analysis, quick reporting.

### 3. VLOOKUP & Data Relationships
**What it is:** Looks up values from one table and returns corresponding values from another (vertical lookup).

**Example:**
```
=VLOOKUP(A2, ProductList, 3, FALSE)
Finds product code in column A within ProductList range
Returns value from 3rd column of that range
FALSE ensures exact match
```

**When to use:** Matching customer IDs to names, product codes to descriptions, joining data from different ranges.

### 4. Data Cleaning Techniques
**What it is:** Processes to standardize, remove duplicates, and prepare raw data for analysis.

**Key techniques:**
- **TRIM():** Remove leading/trailing spaces
- **UPPER()/LOWER():** Standardize text case
- **Find & Replace:** Fix formatting inconsistencies
- **Remove Duplicates:** Data tab → Remove Duplicates
- **Text to Columns:** Split data by delimiters (comma, space)

**Example workflow:**
```
Raw: "  Product A  ", "  Product A  ", "$1,234"
Clean: "Product A" (no duplicates), 1234 (numeric)
```

### 5. Advanced Filtering & Sorting
**What it is:** Filter data by criteria and organize by multiple columns with custom sort orders.

**Example:**
```
AutoFilter: Show only Sales > $10,000 AND Region = "West"
Sort: By Date (oldest first), then by Sales (highest first)
Custom: Sort by custom lists (Jan, Feb, Mar, etc.)
```

**When to use:** Focusing on specific segments, preparing data for presentations, finding anomalies.

## Tools and Resources

**Microsoft Excel:**
- Excel Desktop (Windows/Mac)
- Excel Online (free with Microsoft account)
- Built-in Help: Ctrl+F1

**Recommended Learning Resources:**
- Microsoft Excel Training Hub: https://support.microsoft.com/en-us/excel
- ExcelJet.net: Formula reference and shortcuts
- YouTube: "Excel Formulas for Data Analysis" courses

**Essential Shortcuts:**
- Ctrl+H: Find & Replace
- Ctrl+Shift+L: Toggle AutoFilter
- Alt+D+P+P: Insert Pivot Table (Windows)
- F2: Edit cell formula

## Best Practices

1. **Use Meaningful Headers:** Create clear column names for data organization
2. **Keep Raw Data Separate:** Store original data in one sheet, analysis in another
3. **Avoid Hardcoding:** Use cell references in formulas for flexibility
4. **Validate Data Types:** Ensure dates are dates, numbers are numbers (not text)
5. **Document Complex Formulas:** Add comments explaining logic
6. **Create Data Validation:** Set rules for cells to ensure data quality
7. **Use Named Ranges:** Instead of A1:A100, use descriptive names like "Sales2024"
8. **Format for Readability:** Use consistent fonts, colors, and number formats

## Next Steps

1. **Week 2-3:** Master VLOOKUP, INDEX/MATCH, and advanced formulas
2. **Week 4:** Build your first pivot table dashboard
3. **Week 5-6:** Create a complete analysis project (sales report, inventory management)
4. **After:** Move to Google Sheets collaboration or SQL for larger datasets
5. **Progression:** Advanced Excel → Python/R for statistical analysis
