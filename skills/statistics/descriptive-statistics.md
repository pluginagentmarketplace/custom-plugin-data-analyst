---
name: "Descriptive Statistics"
description: "Master mean, median, mode, variance, distributions, and quartiles to summarize and understand data"
category: "Statistics"
level: "Beginner"
duration: "3-4 weeks"
---

# Descriptive Statistics

## Quick Start

Descriptive statistics summarize data to reveal patterns and characteristics. Within your first week, you'll calculate basic statistics and visualize distributions. By week three, you'll understand data spread, skewness, and how to communicate data characteristics effectively.

**First Task (20 minutes):**
1. Load a sample dataset (e.g., house prices, student grades)
2. Calculate mean, median, mode, and standard deviation
3. Create a histogram and box plot
4. Identify outliers and describe data distribution shape

## Key Concepts

### 1. Central Tendency Measures
**What it is:** Values representing the "center" of a dataset.

**Measures:**
```
Mean (Average):
- Sum of all values / count of values
- Sensitive to outliers
- Example: [10, 20, 30, 40, 50] → mean = 30

Median:
- Middle value when sorted
- Robust to outliers
- Example: [10, 20, 30, 40, 50] → median = 30
- Example with even count: [10, 20, 30, 40] → median = 25 (average of 20, 30)

Mode:
- Most frequently occurring value
- Can be multiple modes (bimodal)
- Example: [10, 20, 20, 30, 20, 40] → mode = 20
- Example: [10, 10, 20, 20, 30] → bimodal (10 and 20)
```

**When to use each:**
```
Use Mean: For normally distributed data, mathematical calculations
Use Median: For skewed data, house prices, salary data
Use Mode: For categorical data, understanding popularity
```

**Example (Python with pandas):**
```python
import pandas as pd
import numpy as np

df = pd.read_csv('sales.csv')
print(f"Mean: {df['amount'].mean()}")
print(f"Median: {df['amount'].median()}")
print(f"Mode: {df['amount'].mode()[0]}")
```

### 2. Spread (Dispersion) Measures
**What it is:** How far apart data values are from the center.

**Measures:**
```
Range:
- Maximum - Minimum
- Example: [10, 20, 30, 40, 50] → range = 50 - 10 = 40

Variance:
- Average squared deviation from mean
- Formula: σ² = Σ(x - mean)² / N
- Difficult to interpret (squared units)

Standard Deviation:
- Square root of variance
- Same units as data
- 68% of data within 1 std dev (normal distribution)
- 95% within 2 std dev, 99.7% within 3 std dev
- Example: mean=100, std_dev=15
  ~68% of data between 85-115
  ~95% between 70-130

Coefficient of Variation (CV):
- Std Dev / Mean × 100
- Compares spread across different scales
- Example: Two products with different price ranges
```

**Interpretation:**
```
Low std dev = Data clustered near mean
High std dev = Data spread out
```

**Example (Python):**
```python
data = [10, 20, 30, 40, 50]
print(f"Std Dev: {np.std(data)}")  # Population std dev
print(f"Sample Std Dev: {np.std(data, ddof=1)}")  # Sample std dev
print(f"Variance: {np.var(data)}")
```

### 3. Quantiles & Box Plot
**What it is:** Dividing data into equal-sized groups to understand distribution.

**Percentiles & Quartiles:**
```
Percentile: Position where % of data falls below
- 25th percentile (Q1): 25% of data below this value
- 50th percentile (Q2/Median): 50% below
- 75th percentile (Q3): 75% below

Interquartile Range (IQR):
- Q3 - Q1
- Middle 50% of data
- Outlier detection: Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR

Box Plot Components:
┌─────────────────────────┐
│ Q1  Q2 (median)  Q3    │ ← Box: middle 50%
○ ●─────────┬─────────● ○
Outlier    Whiskers   Outlier
```

**Example:**
```
Data: [10, 15, 20, 25, 30, 35, 40, 45, 50]
Q1 (25th): 17.5
Q2 (50th): 30
Q3 (75th): 42.5
IQR: 42.5 - 17.5 = 25

Outlier detection:
Lower bound: 17.5 - 1.5×25 = -20 (no lower outliers)
Upper bound: 42.5 + 1.5×25 = 80 (no upper outliers)
```

### 4. Distribution Shapes
**What it is:** How data is distributed across the range of values.

**Common distributions:**
```
Normal (Bell Curve):
- Symmetric
- Mean = Median = Mode
- 68-95-99.7 rule applies

Right-Skewed (Positive Skew):
- Tail extends right
- Mean > Median > Mode
- Examples: Income, house prices

Left-Skewed (Negative Skew):
- Tail extends left
- Mean < Median < Mode
- Examples: Test scores with ceiling

Bimodal:
- Two peaks
- Two distinct groups in data
- Example: Male/female height distribution

Uniform:
- Flat distribution
- All values equally likely
- Example: Random number generator
```

**Interpreting skewness:**
```
Skewness > 0: Right-skewed (use median as center)
Skewness = 0: Symmetric (use mean)
Skewness < 0: Left-skewed (use median)
```

### 5. Data Summary & Communication
**What it is:** Presenting descriptive statistics to convey data story.

**Example summary:**
```
Dataset: Customer spending
n: 1,500 customers
Mean: $2,450
Median: $1,800
Std Dev: $1,100
Min: $50
Q1: $1,000
Q3: $3,500
Max: $8,900
Skewness: 0.85 (right-skewed)

Interpretation:
- Typical customer spends $1,800 (median more representative than mean)
- Half spend between $1,000-$3,500 (IQR shows most customers)
- Distribution right-skewed: some high-value customers pull mean up
- Outlier analysis: customers spending >$6,500 warrant investigation
```

## Tools and Resources

**Python Libraries:**
- pandas: describe() function for quick summary
- numpy: Statistical calculations
- scipy.stats: Advanced statistical functions
- matplotlib/seaborn: Visualization

**Excel Functions:**
- AVERAGE, MEDIAN, MODE
- STDEV (sample), STDEVP (population)
- QUARTILE, PERCENTILE
- Built-in statistics add-in

**Online Calculators & Tools:**
- StatKey.io: Interactive statistics
- GeoGebra: Free graphing/statistics
- Desmos: Distribution visualization

## Best Practices

1. **Report Multiple Measures:** Always show mean AND median to detect skewness
2. **Consider Outliers:** Decide if extreme values should be included
3. **Use Appropriate Scale:** For skewed data, use median and IQR instead of mean and SD
4. **Visualize Distributions:** Histograms and box plots reveal patterns numbers don't
5. **Sample Size Matters:** Larger samples give more reliable statistics
6. **Document Data Quality:** Note missing values, how they were handled
7. **Compare Context:** Statistics mean nothing without context or comparison
8. **Use Consistent Precision:** Round to sensible number of decimal places

## Next Steps

1. **Week 1:** Learn central tendency and spread measures
2. **Week 2:** Understand quartiles and visualize distributions
3. **Week 3:** Analyze real datasets and create summary reports
4. **Week 4:** Practice interpreting distributions and identifying patterns
5. **After:** Move to Inferential Statistics (hypothesis testing)
6. **Progression:** Descriptive → Inferential → Predictive Analysis
