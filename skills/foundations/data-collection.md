---
name: "Data Collection"
description: "Master data sources, APIs, web scraping, and data ingestion techniques to build reliable data pipelines"
category: "Foundations"
level: "Beginner-Intermediate"
duration: "4-6 weeks"
---

# Data Collection

## Quick Start

Data collection is the foundation of analysis. In your first week, you'll identify data sources, connect to APIs, and perform basic web scraping. By week three, you'll build automated pipelines that ingest data from multiple sources into a central repository.

**First Task (30 minutes):**
1. Identify 3 data sources relevant to your domain (public APIs, databases, files)
2. Access one public API (e.g., OpenWeather, CoinGecko) and retrieve sample data
3. Save the data to a CSV file
4. Load and inspect the data in a spreadsheet or Python

## Key Concepts

### 1. Data Sources Classification
**What it is:** Understanding where data originates and how to access it.

**Types of sources:**
```
1. APIs (Application Programming Interface)
   - RESTful APIs: HTTP requests, JSON responses
   - GraphQL APIs: Flexible query structure
   - SDK-based: Language-specific libraries

2. Databases
   - Relational (SQL): PostgreSQL, MySQL
   - Cloud (BigQuery, Redshift)
   - NoSQL: MongoDB, DynamoDB

3. File-based
   - CSV/Excel files
   - JSON, XML, Parquet
   - Unstructured logs

4. Web Sources
   - HTML scraping
   - RSS feeds
   - Publicly available datasets

5. Real-time Streams
   - Event streams (Kafka)
   - WebSockets
   - Message queues (RabbitMQ)
```

### 2. API Integration
**What it is:** Using HTTP requests to fetch data from web services programmatically.

**Example (Python with requests library):**
```python
import requests
import json

url = "https://api.example.com/data"
headers = {"Authorization": f"Bearer {API_KEY}"}
params = {"date": "2024-01-01", "limit": 100}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
```

**Common API patterns:**
```
GET /users          # Retrieve list
GET /users/123      # Retrieve specific item
POST /users         # Create new record
PUT /users/123      # Update record
DELETE /users/123   # Delete record
```

### 3. Web Scraping
**What it is:** Extracting structured data from HTML web pages programmatically.

**Example (Python with BeautifulSoup):**
```python
from bs4 import BeautifulSoup
import requests

url = "https://example.com/data"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all table rows
rows = soup.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    data = [cell.text.strip() for cell in cells]
    print(data)
```

**When to use:** Competitor monitoring, real estate listings, news aggregation, public data without API.

### 4. Data Ingestion Pipelines
**What it is:** Automated processes that extract, transform, and load data (ETL).

**Pipeline architecture:**
```
Source System → Extract → Transform → Load → Target Database
   (API)        (fetch)   (clean, map) (store) (Data warehouse)
     ↓
Scheduling (daily, hourly)
   ↓
Error handling & logging
   ↓
Data quality checks
```

**Example workflow:**
```
1. Schedule: Run at 2 AM daily
2. Extract: Fetch data from 3 APIs
3. Transform: Clean, deduplicate, merge
4. Load: Insert into PostgreSQL
5. Validate: Check row counts, data types
6. Alert: Notify team if issues detected
```

### 5. Data Quality & Validation
**What it is:** Ensuring collected data meets standards before analysis.

**Validation checks:**
```
1. Schema validation: Right columns, data types
2. Completeness: Required fields not null
3. Uniqueness: No duplicate records
4. Range validation: Values within expected bounds
5. Format validation: Dates are dates, emails are valid
6. Referential integrity: Foreign keys match
7. Freshness: Data within acceptable age
```

**Example (Python with Great Expectations):**
```python
from great_expectations import dataset

df = pd.read_csv("data.csv")
data = dataset.PandasDataset(df)

# Validate
data.expect_column_values_to_not_be_null("user_id")
data.expect_column_values_to_be_between("age", 0, 120)
data.expect_column_values_to_match_regex("email", r"^[\w\.-]+@[\w\.-]+\.\w+$")
```

## Tools and Resources

**API Tools:**
- Postman: Test APIs interactively (free)
- Insomnia: REST client with environment support
- curl: Command-line HTTP client

**Python Libraries:**
- `requests`: HTTP requests
- `beautifulsoup4`: Web scraping
- `selenium`: Browser automation for JavaScript-heavy sites
- `pandas`: Data loading and manipulation
- `sqlalchemy`: Database connections

**Services & Platforms:**
- Zapier: No-code automation
- Make (formerly Integromat): Workflow automation
- Fivetran: Managed ETL service
- Apache Airflow: Open-source workflow orchestration

**Public Datasets:**
- Kaggle.com: Datasets with notebooks
- data.gov: Government datasets
- GitHub: Trending datasets
- your_industry_specific_sites

## Best Practices

1. **Respect Rate Limits:** Check API documentation and implement backoff strategies
2. **Use API Keys Securely:** Store in environment variables, never commit to git
3. **Implement Error Handling:** Retry logic, fallback sources, error logging
4. **Cache When Possible:** Avoid redundant API calls; store intermediate results
5. **Monitor Data Quality:** Implement automated validation checks
6. **Document Data Sources:** Keep record of field definitions, update frequencies
7. **Obtain Permissions:** Ensure you have rights to collect and use the data
8. **Version Your Data:** Track when data was collected, what version of API used
9. **Plan for Scalability:** Design pipelines to handle growth in data volume
10. **Log Everything:** Track successes, failures, and data volumes for auditing

## Next Steps

1. **Week 1-2:** Connect to 2-3 public APIs and understand rate limits
2. **Week 2-3:** Build first basic web scraper with error handling
3. **Week 3-4:** Create simple daily ingestion pipeline (spreadsheet or database)
4. **Week 4-5:** Add data quality validation checks
5. **Week 5-6:** Schedule automated ingestion with error alerts
6. **After:** Learn SQL for database storage, Python for complex transformations
7. **Progression:** Basic APIs → Advanced ETL → Stream processing (Kafka, Spark)
