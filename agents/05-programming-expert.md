---
name: 05-programming-expert
description: Master Python, R, pandas, NumPy, and data manipulation to automate analysis and unlock advanced capabilities
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
---

# 05 - Programming Expert

## Overview

The Programming Expert role elevates you from analyst to technical specialist. While Foundations Specialists work in spreadsheets and SQL Experts query databases, Programming Experts write code to automate, scale, and unlock capabilities unavailable in traditional tools. Python and R are the languages of data science, machine learning, and modern analytics. This role teaches you to think like a programmer while maintaining your analyst perspective.

**Why This Matters**: Programming skills multiply your impact exponentially. Analysis that takes hours in Excel takes minutes in Python. Solutions that are impossible in spreadsheets become straightforward with code. This is the most valuable skill multiplier in analytics.

---

## Learning Path Overview

This learning journey transforms you from tool-based analyst to code-based programmer who can:
- Write Python and R scripts for data analysis
- Use pandas, NumPy, and other powerful libraries
- Automate repetitive analytical tasks
- Build reproducible analyses
- Combine multiple tools into integrated solutions
- Understand machine learning fundamentals
- Write efficient, readable code

**Timeline**: 14-18 weeks of focused learning | **Skill Level**: Intermediate Programmer

---

## Learning Phase 1: Python Fundamentals & Data Structures

### Objectives
- Master Python syntax and programming concepts
- Understand data structures and object-oriented basics
- Learn to write clean, readable code
- Understand when and how to use Python for analytics
- Set up development environment

### Core Topics

#### Python Environment Setup
```bash
# Installation
Windows/Mac/Linux: python.org

# Virtual Environment (best practice)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Package Management
pip install pandas numpy matplotlib jupyter
pip install --upgrade package_name
pip list  # See installed packages

# Jupyter Notebook (interactive development)
pip install jupyter
jupyter notebook
# Creates notebook files (.ipynb)

# IDEs
VSCode + Python extension (lightweight, recommended)
PyCharm (full-featured, heavier)
Spyder (science-focused)
```

#### Python Fundamentals
```python
# Variables and Data Types
name = "Alice"                      # String
age = 30                            # Integer
score = 95.5                        # Float
is_active = True                    # Boolean

# Lists (ordered, mutable)
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
numbers.append(6)                   # Add element
numbers[0]                          # Access by index (0-based)

# Tuples (ordered, immutable)
coordinates = (40.7128, -74.0060)  # Latitude, longitude
x, y = coordinates                  # Unpacking

# Dictionaries (key-value pairs)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
person["name"]                      # Access by key
person["age"] = 31                  # Update value

# Sets (unique values, unordered)
unique_colors = {"red", "blue", "green"}
unique_colors.add("yellow")

# String Operations
message = "Hello, World!"
message.lower()                     # "hello, world!"
message.split(",")                  # ["Hello", " World!"]
",".join(["a", "b", "c"])          # "a,b,c"
```

#### Control Flow
```python
# If/Else Conditions
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Loops - For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Range for numeric loops
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# While loops
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# List Comprehension (powerful pattern)
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]   # [1, 4, 9, 16, 25]

# With condition
even_numbers = [x for x in numbers if x % 2 == 0]  # [2, 4]
```

#### Functions & Code Organization
```python
# Function Definition
def greet(name, greeting="Hello"):
    """This function greets someone."""
    return f"{greeting}, {name}!"

# Function Call
greet("Alice")                      # "Hello, Alice!"
greet("Bob", "Hi")                  # "Hi, Bob!"

# Multiple Return Values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

min_val, max_val, avg = get_stats([1, 2, 3, 4, 5])

# *args for variable arguments
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4, 5)             # 15

# **kwargs for keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")

# Lambda (anonymous functions)
square = lambda x: x ** 2
square(5)                           # 25

# Map and Filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

#### Working with Files
```python
# Reading Files
with open("data.txt", "r") as file:
    content = file.read()           # Read entire file

with open("data.txt", "r") as file:
    lines = file.readlines()        # Read as list of lines

# Writing Files
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# CSV Files
import csv

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)   # Read as list of dicts
    for row in reader:
        print(row["name"], row["age"])

# Writing CSV
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)

# JSON Files
import json

# Reading JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Writing JSON
data = {"name": "Alice", "age": 30}
with open("output.json", "w") as file:
    json.dump(data, file, indent=2)
```

#### Error Handling
```python
# Try/Except
try:
    number = int("abc")             # This will fail
except ValueError:
    print("That's not a valid number")

# Multiple Exception Types
try:
    data = {"name": "Alice"}
    print(data["age"])              # KeyError
except KeyError:
    print("Key not found")
except Exception as e:
    print(f"Other error: {e}")

# Finally (always runs)
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if "file" in locals():
        file.close()

# Raising Exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

### Tools & Resources
- **Development Environments**:
  - VSCode + Python extension (recommended)
  - Jupyter Notebook (interactive)
  - PyCharm Community Edition
  - Google Colab (free cloud notebook)
- **Learning Resources**:
  - "Python Crash Course" by Eric Matthes
  - DataCamp Python courses
  - Codecademy Python track
  - Real Python tutorials (realpython.com)
- **Practice Platforms**:
  - LeetCode (coding problems)
  - HackerRank (programming challenges)
  - CodeWars (gamified learning)

### Key Deliverables
- [ ] Complete 50+ Python exercises covering fundamentals
- [ ] Write 10+ functions solving different problems
- [ ] Understand list comprehensions and lambda functions
- [ ] Handle file I/O with multiple formats
- [ ] Complete 20 LeetCode problems

---

## Learning Phase 2: Data Analysis with Pandas & NumPy

### Objectives
- Master NumPy arrays and operations
- Learn pandas DataFrames and Series
- Perform data manipulation and cleaning with code
- Learn data aggregation and transformation
- Understand vectorization and performance

### Core Topics

#### NumPy Fundamentals
```python
import numpy as np

# Arrays
arr = np.array([1, 2, 3, 4, 5])
arr.shape                           # (5,)
arr.dtype                           # dtype('int64')

# 2D Arrays (matrices)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
matrix.shape                        # (2, 3)
matrix[0, 1]                        # Access element: 2

# Creating Arrays
np.zeros((3, 3))                   # 3x3 array of zeros
np.ones(5)                          # Array of ones
np.arange(0, 10, 2)                 # [0 2 4 6 8]
np.linspace(0, 1, 5)                # 5 evenly spaced values

# Array Operations (vectorized)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr1 + arr2                         # [5 7 9]
arr1 * arr2                         # [4 10 18]
arr1 ** 2                           # [1 4 9]

# Aggregations
arr = np.array([1, 5, 3, 9, 2])
np.sum(arr)                         # 20
np.mean(arr)                        # 4.0
np.std(arr)                         # Standard deviation
np.min(arr), np.max(arr)            # 1, 9

# Indexing & Slicing
arr = np.array([10, 20, 30, 40, 50])
arr[0]                              # 10
arr[1:4]                            # [20 30 40]
arr[::2]                            # [10 30 50] every 2nd element

# Boolean Indexing
arr = np.array([1, 2, 3, 4, 5])
arr[arr > 2]                        # [3 4 5]
arr[(arr > 2) & (arr < 5)]          # [3 4]
```

#### Pandas Series & DataFrames
```python
import pandas as pd

# Series (1D labeled array)
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s['a']                              # 1
s.iloc[0]                           # 1 (by position)
s.loc['a']                          # 1 (by label)

# DataFrame (2D labeled table)
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35],
    'city': ['NYC', 'LA', 'Chicago']
})

# Accessing Data
df['name']                          # Column (Series)
df[['name', 'age']]                 # Multiple columns (DataFrame)
df.iloc[0]                          # First row
df.loc[0, 'age']                    # Specific cell

# Creating DataFrame from Different Sources
df = pd.read_csv('data.csv')
df = pd.read_json('data.json')
df = pd.read_sql("SELECT * FROM table", connection)
df = pd.read_excel('data.xlsx')
```

#### Data Cleaning & Transformation
```python
import pandas as pd

# Load data
df = pd.read_csv('sales.csv')

# Explore data
df.shape                            # (1000, 5) rows, columns
df.head()                           # First 5 rows
df.info()                           # Data types and null counts
df.describe()                       # Summary statistics

# Handle Missing Data
df.isnull().sum()                   # Count nulls per column
df.dropna()                         # Remove rows with nulls
df.fillna(0)                        # Replace nulls with 0
df['age'].fillna(df['age'].mean())  # Replace with mean

# Data Type Conversion
df['age'] = df['age'].astype(int)
df['date'] = pd.to_datetime(df['date'])

# String Operations
df['name'] = df['name'].str.upper()
df['name'] = df['name'].str.replace(' ', '_')
df['first_name'] = df['name'].str.split(' ').str[0]

# Filtering
high_earners = df[df['salary'] > 100000]
tech_workers = df[df['department'] == 'Engineering']
combined = df[(df['salary'] > 100000) & (df['department'] == 'Engineering')]

# Sorting
df.sort_values('salary', ascending=False)
df.sort_values(['department', 'salary'], ascending=[True, False])

# Grouping & Aggregation
df.groupby('department')['salary'].mean()
df.groupby('department').agg({
    'salary': 'mean',
    'age': 'max',
    'id': 'count'
})

# Pivoting
pivot = df.pivot_table(
    index='department',
    columns='year',
    values='salary',
    aggfunc='mean'
)

# Merging
df_merged = pd.merge(df1, df2, on='id', how='inner')
df_merged = df1.join(df2)  # Join on index
```

#### Data Analysis with Pandas
```python
# Time Series Analysis
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.resample('M').sum()              # Monthly aggregation
df.rolling(7).mean()                # 7-day moving average

# Correlation
correlation = df[['age', 'salary']].corr()
correlation_matrix = df.corr()

# Categorical Data
df['category'] = pd.Categorical(df['category'])
df.groupby('category').size()

# Multi-level Indexing
df.set_index(['year', 'department'], inplace=True)
df.loc[(2023, 'Engineering')]       # Access specific level

# Performance: Vectorization vs Loops
# SLOW: Loop (avoid)
for i, row in df.iterrows():
    df.loc[i, 'new_col'] = row['col1'] + row['col2']

# FAST: Vectorized (use this)
df['new_col'] = df['col1'] + df['col2']
```

### Tools & Resources
- **NumPy Documentation**: numpy.org
- **Pandas Documentation**: pandas.pydata.org
- **Online Courses**:
  - DataCamp Pandas track
  - Udemy "Data Analysis with Pandas"
  - Real Python pandas tutorials
- **Books**: "Python for Data Analysis" by Wes McKinney

### Key Deliverables
- [ ] Master NumPy operations on 100+ problems
- [ ] Clean and transform 10+ datasets with pandas
- [ ] Write functions for repeated data cleaning tasks
- [ ] Perform groupby aggregations (15+ scenarios)
- [ ] Complete merge/join operations (10+ scenarios)
- [ ] Optimize slow pandas operations (5+ examples)

---

## Learning Phase 3: Data Visualization with Python & Matplotlib

### Objectives
- Create publication-quality visualizations with code
- Learn matplotlib, seaborn, and plotly
- Automate visualization creation
- Combine plotting with analysis
- Understand when to use each visualization library

### Core Topics

#### Matplotlib Basics
```python
import matplotlib.pyplot as plt
import numpy as np

# Simple Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Sine Wave')
plt.show()

# Multiple Subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(x[:20], y[:20])
axes[1, 1].hist(y, bins=20)
plt.tight_layout()
plt.show()

# Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
plt.bar(categories, values)
plt.ylabel('Count')
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Customization
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linewidth=2, label='Sine')
plt.plot(x, np.cos(x), color='red', linestyle='--', label='Cosine')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Saving Figures
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf')
```

#### Seaborn for Statistical Graphics
```python
import seaborn as sns
import pandas as pd

# Load sample data
df = pd.read_csv('data.csv')

# Distribution Plots
sns.histplot(df['age'], kde=True)
sns.kdeplot(df['salary'], fill=True)

# Categorical Plots
sns.boxplot(data=df, x='department', y='salary')
sns.violinplot(data=df, x='department', y='salary')
sns.stripplot(data=df, x='department', y='salary', jitter=True)

# Relational Plots
sns.scatterplot(data=df, x='age', y='salary', hue='department')
sns.lineplot(data=df, x='month', y='revenue', hue='product')

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.show()

# Pair Plot (distributions and correlations)
sns.pairplot(df[['age', 'salary', 'years_experience']])

# FacetGrid (multiple subplots by category)
g = sns.FacetGrid(df, col='department', height=4)
g.map(plt.scatter, 'age', 'salary')
```

#### Plotly for Interactive Visualizations
```python
import plotly.express as px
import plotly.graph_objects as go

# Interactive Line Plot
fig = px.line(df, x='date', y='sales', title='Sales Over Time')
fig.show()

# Interactive Scatter
fig = px.scatter(df, x='age', y='salary',
                color='department', size='experience',
                hover_name='name', title='Employee Data')
fig.show()

# Interactive Bar Chart
fig = px.bar(df.groupby('department')['salary'].mean().reset_index(),
            x='department', y='salary',
            title='Average Salary by Department')
fig.show()

# Choropleth Map
fig = px.choropleth(df, locations='state', color='cases',
                   title='COVID Cases by State')
fig.show()

# Dashboard (multiple plots)
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2,
                   subplot_titles=('Plot 1', 'Plot 2', 'Plot 3', 'Plot 4'))
fig.add_trace(go.Scatter(x=x, y=y, name='Trace 1'), row=1, col=1)
fig.add_trace(go.Bar(x=x, y=y, name='Trace 2'), row=1, col=2)
fig.show()
```

### Tools & Resources
- **Matplotlib**: matplotlib.org (documentation)
- **Seaborn**: seaborn.pydata.org
- **Plotly**: plotly.com/python
- **Courses**: DataCamp visualization courses
- **Gallery**: matplotlib.org/stable/gallery, seaborn examples

### Key Deliverables
- [ ] Create 20+ different chart types
- [ ] Master matplotlib customization
- [ ] Build publication-quality figures
- [ ] Create interactive dashboards with plotly
- [ ] Automate report generation with visualizations

---

## Learning Phase 4: Advanced Topics & Integration

### Objectives
- Learn SQL integration with Python
- Understand APIs and data ingestion
- Learn automation and scheduling
- Build end-to-end analytical pipelines
- Understand performance optimization

### Core Topics

#### Working with Databases from Python
```python
# SQLite (built-in)
import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_sql("SELECT * FROM employees", conn)
conn.close()

# MySQL/MariaDB
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="analytics"
)
df = pd.read_sql("SELECT * FROM sales", conn)
conn.close()

# PostgreSQL
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="analyst",
    password="password",
    database="analytics"
)
df = pd.read_sql("SELECT * FROM products", conn)
conn.close()

# Using SQLAlchemy (unified interface)
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@localhost/database')
df = pd.read_sql("SELECT * FROM sales", engine)

# Write data back to database
df.to_sql('new_table', con=engine, if_exists='replace', index=False)
```

#### APIs & Data Ingestion
```python
import requests
import json

# GET Request
response = requests.get('https://api.example.com/data')
data = response.json()
df = pd.DataFrame(data)

# Handling Parameters
params = {
    'start_date': '2024-01-01',
    'end_date': '2024-12-31',
    'region': 'US'
}
response = requests.get('https://api.example.com/sales', params=params)
data = response.json()

# Authentication
headers = {'Authorization': f'Bearer {api_token}'}
response = requests.get('https://api.example.com/data', headers=headers)

# Error Handling
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")

# Rate Limiting
import time
for page in range(1, 11):
    response = requests.get(f'https://api.example.com/data?page={page}')
    data = response.json()
    time.sleep(1)  # Wait 1 second between requests
```

#### Automation & Scheduling
```python
# Schedule Python Scripts to Run Periodically

# Using Schedule library
import schedule
import time

def update_dashboard():
    """Run daily analysis"""
    df = pd.read_csv('data.csv')
    # ... analysis code ...
    df.to_csv('results.csv', index=False)
    print("Dashboard updated!")

# Schedule to run daily at 8 AM
schedule.every().day.at("08:00").do(update_dashboard)

# Keep running
while True:
    schedule.run_pending()
    time.sleep(60)

# Using APScheduler for more complex scheduling
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(update_dashboard, 'cron', hour=8, minute=0)
scheduler.start()

# Windows: Use Task Scheduler
# Mac/Linux: Use cron
# Production: Use tools like Airflow
```

#### Building Data Pipelines
```python
import pandas as pd
from datetime import datetime

def extract_data(source):
    """Extract from various sources"""
    if source == 'csv':
        return pd.read_csv('data.csv')
    elif source == 'sql':
        return pd.read_sql("SELECT * FROM sales", conn)
    elif source == 'api':
        return pd.DataFrame(requests.get(url).json())

def transform_data(df):
    """Clean and transform data"""
    # Remove nulls
    df = df.dropna()
    # Convert types
    df['date'] = pd.to_datetime(df['date'])
    # Create new columns
    df['profit_margin'] = df['profit'] / df['revenue']
    # Remove duplicates
    df = df.drop_duplicates()
    return df

def load_data(df, destination):
    """Load to destination"""
    if destination == 'csv':
        df.to_csv('output.csv', index=False)
    elif destination == 'sql':
        df.to_sql('processed_data', conn, if_exists='replace')
    elif destination == 'api':
        requests.post(url, json=df.to_dict())

# Main Pipeline
def run_etl():
    # Extract
    df = extract_data('csv')

    # Transform
    df = transform_data(df)

    # Load
    load_data(df, 'sql')

    # Log
    print(f"Pipeline completed at {datetime.now()}")

# Execute
if __name__ == "__main__":
    run_etl()
```

#### Performance Optimization
```python
# Optimizing Pandas Operations

# SLOW: Iterating through rows
result = []
for idx, row in df.iterrows():
    result.append(row['value'] * 2)
df['new_col'] = result

# FAST: Vectorized operation
df['new_col'] = df['value'] * 2

# SLOW: Multiple groupby operations
summary = {}
for dept in df['department'].unique():
    summary[dept] = df[df['department'] == dept]['salary'].mean()

# FAST: Single groupby
summary = df.groupby('department')['salary'].mean()

# SLOW: Large DataFrame with unused columns
df = pd.read_csv('huge_file.csv')  # 100 columns

# FAST: Read only needed columns
df = pd.read_csv('huge_file.csv', usecols=['col1', 'col2', 'col3'])

# Use appropriate data types
df['category'] = df['category'].astype('category')  # Saves memory
df['value'] = df['value'].astype('int32')  # Instead of int64

# Chunking for large files
chunks = []
for chunk in pd.read_csv('huge_file.csv', chunksize=10000):
    chunks.append(transform_data(chunk))
df = pd.concat(chunks, ignore_index=True)
```

### Tools & Resources
- **Database Drivers**: mysql-connector, psycopg2, pymongo
- **API Libraries**: requests, httpx
- **Scheduling**: schedule, APScheduler, Airflow
- **Workflow Orchestration**: Apache Airflow, Prefect, Dagster
- **Courses**: DataCamp advanced Python, Udemy ETL courses

### Key Deliverables
- [ ] Build database connection and query from Python
- [ ] Fetch data from 5+ different APIs
- [ ] Schedule Python script to run automatically
- [ ] Build complete ETL pipeline (E→T→L)
- [ ] Optimize slow pandas operations (10+ examples)

---

## Real-World Projects

### Project 1: Automated Sales Analysis Pipeline
**Scenario**: Build automated pipeline that processes sales data and generates reports.

**Objectives**:
- Extract data from multiple sources (CSV, SQL, API)
- Transform and clean data automatically
- Perform analysis (aggregations, trends)
- Generate visualizations and reports
- Schedule to run daily
- Create email notification system

**Deliverables**:
- Python pipeline code (well-organized, documented)
- Automated report generation
- Scheduling setup
- Email notification system
- Documentation and troubleshooting guide

**Skills Applied**: File I/O, databases, APIs, pandas, visualization, scheduling, automation

---

### Project 2: Machine Learning-Ready Data Preprocessing
**Scenario**: Prepare customer dataset for machine learning model.

**Objectives**:
- Load data from multiple sources
- Handle missing data appropriately
- Feature engineering (create useful variables)
- Outlier detection and handling
- Data normalization/scaling
- Create train/test split
- Document data preparation for model handoff

**Deliverables**:
- Preprocessing Python script
- Feature engineering documentation
- Data quality report
- Ready-to-use train/test datasets
- Reproducible preprocessing pipeline

**Skills Applied**: Data cleaning, feature engineering, numpy operations, pandas mastery

---

### Project 3: Interactive Dashboard with Real-Time Updates
**Scenario**: Build Python-based interactive dashboard that updates automatically.

**Objectives**:
- Set up Streamlit or Dash application
- Connect to live data source
- Build interactive visualizations
- Implement filtering and drill-down
- Deploy to cloud (Heroku, AWS, etc.)
- Monitor and troubleshoot

**Deliverables**:
- Deployed interactive dashboard
- Python application code
- Data pipeline keeping dashboard current
- User documentation
- Deployment and maintenance guide

**Skills Applied**: Web frameworks, visualization, databases, deployment, cloud services

---

## Career Progression

### Timeline & Advancement
```
Months 1-3:     Basic Competency
├── Understand Python fundamentals
├── Learn pandas basics
├── Create first scripts
└── Understand why programming matters

Months 4-6:     Intermediate Competency
├── Automate analysis tasks
├── Master pandas and NumPy
├── Create visualizations with code
├── Understand performance optimization

Months 7-10:    Advanced Competency
├── Build ETL pipelines
├── Integrate multiple data sources
├── Create production code
├── Mentor others on Python

Months 11-18:   Expert Competency
├── Build machine learning pipelines
├── Design scalable systems
├── Lead technical initiatives
├── Ready for data science/engineering roles
```

### Role Opportunities
- **Data Analyst (Python)** (Python-focused analyst)
- **Analytics Engineer** (Pipeline-focused)
- **Data Engineer** (Infrastructure-focused)
- **Data Scientist** (ML-focused)
- **Machine Learning Engineer** (Model-focused)

### Salary Expectations (2024 US Market)
```
Entry Level (0-2 years):        $70,000 - $95,000
Mid Level (2-5 years):          $95,000 - $135,000
Advanced (5+ years):            $135,000 - $175,000
Senior/Lead (8+ years):         $175,000 - $250,000+
```

---

## Best Practices

### 1. Code Style & Readability
```python
# PEP 8 Style Guide (Python standard)

# Good: Clear variable names, spaces
def calculate_average_salary(employees):
    """Calculate average salary for a group of employees."""
    total = sum(emp['salary'] for emp in employees)
    return total / len(employees)

# Bad: Unclear, hard to read
def calc_avg(e):
    t = sum([x['sal'] for x in e])
    return t / len(e)

# Use type hints (Python 3.5+)
from typing import List, Dict

def process_data(data: List[Dict]) -> float:
    """Process data and return average."""
    return sum(d['value'] for d in data) / len(data)

# Docstrings for functions
def analyze_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze dataset and return summary statistics.

    Args:
        df: Input DataFrame with sales data

    Returns:
        DataFrame with aggregated results
    """
    return df.groupby('category').agg({'sales': 'sum'})
```

### 2. Version Control with Git
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit"

# Create branches for features
git checkout -b feature/new-analysis
# ... make changes ...
git commit -m "Add new analysis"
git checkout main
git merge feature/new-analysis

# Good commit messages
✓ "Add customer segmentation analysis"
✓ "Fix null handling in revenue calculation"
✗ "Update"
✗ "Work in progress"
```

### 3. Testing Your Code
```python
# Unit tests
def test_calculate_average():
    employees = [
        {'name': 'Alice', 'salary': 100000},
        {'name': 'Bob', 'salary': 120000}
    ]
    assert calculate_average_salary(employees) == 110000

# Using unittest framework
import unittest

class TestAnalysis(unittest.TestCase):
    def test_data_loading(self):
        df = load_data('test_data.csv')
        self.assertEqual(len(df), 100)

    def test_missing_values(self):
        df = load_data('test_data.csv')
        self.assertEqual(df.isnull().sum().sum(), 0)

if __name__ == '__main__':
    unittest.main()
```

### 4. Documentation
```python
"""
sales_analysis.py

This module performs monthly sales analysis.

Functions:
    load_sales_data: Load sales from database
    calculate_monthly_totals: Aggregate sales by month
    generate_report: Create summary report

Example:
    df = load_sales_data('2024-01')
    monthly = calculate_monthly_totals(df)
    report = generate_report(monthly)
"""
```

### 5. Project Organization
```
project/
├── data/
│   ├── raw/           # Original, unmodified data
│   ├── processed/     # Cleaned, processed data
│   └── output/        # Final reports/results
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── analysis.py
│   └── reporting.py
├── tests/
│   ├── test_loader.py
│   ├── test_preprocessing.py
│   └── test_analysis.py
├── notebooks/
│   ├── 01_exploration.ipynb
│   └── 02_analysis.ipynb
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── main.py            # Entry point
```

---

## Best Tools & Resources

### Development Tools
- **IDEs**: VSCode (lightweight), PyCharm (full-featured)
- **Jupyter Notebook**: Interactive development
- **Google Colab**: Free cloud Jupyter
- **GitHub**: Version control and collaboration

### Libraries
- **Data**: pandas, NumPy, Polars
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Statistics**: SciPy, StatsModels
- **Machine Learning**: Scikit-learn (beginner), TensorFlow/PyTorch (advanced)
- **Web Frameworks**: Streamlit (easiest), Dash, Flask

### Learning Resources
- **Books**:
  - "Python Crash Course" - Eric Matthes
  - "Python for Data Analysis" - Wes McKinney
  - "Fluent Python" - Luciano Ramalho
- **Online Courses**:
  - DataCamp Python & Pandas tracks
  - Udemy complete courses
  - Real Python (realpython.com)
  - MIT OpenCourseWare
- **Communities**:
  - r/learnprogramming (Reddit)
  - Stack Overflow
  - Python Discord servers

---

## Next Steps

### Immediate Actions (Next 2 Weeks)
1. **Set up environment**
   - Install Python and VSCode
   - Create first virtual environment
   - Write "Hello World" script

2. **Learn fundamentals**
   - Complete Python basics module
   - Understand data structures
   - Write 10+ small functions

3. **Join community**
   - Follow Python blogs
   - Join r/learnprogramming
   - Connect with Python developers

### Short-term Goals (1-3 Months)
1. **Master pandas & NumPy**
   - Complete DataCamp tracks
   - Clean 5+ real datasets
   - Create visualizations with code

2. **Write first automation**
   - Automate repetitive task
   - Schedule script to run automatically
   - Save yourself 5+ hours/week

3. **Build portfolio project**
   - Complete end-to-end analysis with code
   - Push to GitHub
   - Write clear documentation

### Advanced Preparation (3-6 Months)
1. **Prepare for data science roles**
   - Learn machine learning basics
   - Build predictive models
   - Learn deep learning fundamentals

2. **Optimize and scale**
   - Understand parallel processing
   - Learn cloud platforms (AWS, GCP, Azure)
   - Build production systems

### Recommended Learning Sequence
```
Current Role: Programming Expert ✓ (You are here)
        ↓
Option A: Deepen programming expertise
        ↓
Option B: Move to Phase 6 - Advanced Analytics
        ↓
Option C: Combine with Phase 5 & 6 for data science
        ↓
Career Leadership Roles (7 - Career Coach)
```

---

## Key Takeaways

As a Programming Expert, you'll understand that:

1. **Code is communication** - Write for humans first, computers second
2. **Automation multiplies impact** - 1 hour to automate saves 5+ hours/week
3. **Testing prevents disasters** - Automated tests save debugging time
4. **Reproducibility matters** - Document so others (and future you) understand
5. **Performance optimization is iterative** - Measure first, optimize what matters
6. **The right tool matters** - Pandas for structured data, NumPy for numerical, etc.

Programming transforms you from tool-user to tool-builder. This is the most valuable skill in modern analytics.

---

## FAQ

**Q: Should I learn Python or R first?**
A: Python is more general-purpose and has better job market. Learn Python first, then R if needed for statistics.

**Q: How long until I'm comfortable programming?**
A: 4-6 weeks basics, 3-4 months competency. Programming is a skill best learned by doing.

**Q: Do I need to be a software engineer?**
A: No. You need practical skills to automate analysis, not enterprise software patterns.

**Q: Should I memorize functions?**
A: No. Learn how to find documentation. Experienced programmers Google constantly.

**Q: Is writing "spaghetti code" bad?**
A: In production yes, in exploratory notebooks no. Clean it up when sharing.

---

**Last Updated**: November 2024
**Difficulty Level**: Intermediate
**Estimated Time to Completion**: 14-18 weeks
