---
name: data-mining
description: Master data mining techniques, clustering, classification, pattern discovery, and anomaly detection. Learn unsupervised and supervised learning for data analysis.
---

# Data Mining & Pattern Discovery

## Quick Start

Data mining uncovers hidden patterns in large datasets using algorithms and statistical techniques.

```python
# K-Means Clustering example
from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv('customer_data.csv')
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(df[['spending', 'frequency']])
df['cluster'] = clusters
print(df.groupby('cluster').mean())
```

## Core Concepts

### 1. **Clustering Techniques**
- K-Means: Partition data into K clusters
- Hierarchical Clustering: Build cluster hierarchy
- DBSCAN: Density-based clustering
- Gaussian Mixture Models: Probabilistic clustering

### 2. **Classification Methods**
- Decision Trees: Rule-based classification
- Random Forests: Ensemble classification
- Naive Bayes: Probabilistic classifier
- SVM: Support Vector Machines

### 3. **Pattern Discovery**
- Association Rules: Market basket analysis
- Sequential Patterns: Time-ordered patterns
- Frequent Itemsets: Common patterns
- Anomaly Detection: Outlier identification

### 4. **Dimensionality Reduction**
- Principal Component Analysis (PCA)
- Feature Selection
- t-SNE for visualization
- Feature Extraction

### 5. **Evaluation Metrics**
- Silhouette Score: Clustering quality
- Davies-Bouldin Index: Cluster separation
- Confusion Matrix: Classification performance
- Precision, Recall, F1-Score: Classification metrics

## Tools & Technologies

**Python Libraries**
- scikit-learn: ML algorithms
- scipy: Scientific computing
- pandas: Data manipulation
- matplotlib/seaborn: Visualization

**R Packages**
- caret: ML workflow
- rpart: Decision trees
- cluster: Clustering methods
- igraph: Network analysis

**Visualization**
- Python: matplotlib, seaborn, plotly
- R: ggplot2, plotly
- Tableau, Power BI: Interactive exploration

## Best Practices

✅ **Data Preparation**
- Handle missing values
- Normalize/standardize features
- Remove duplicates
- Handle outliers appropriately

✅ **Algorithm Selection**
- Understand data type (numerical, categorical)
- Consider scalability
- Evaluate computational complexity
- Test multiple algorithms

✅ **Validation**
- Use cross-validation
- Test on holdout set
- Compare multiple metrics
- Validate business logic

✅ **Interpretation**
- Explain patterns found
- Validate against domain knowledge
- Document findings clearly
- Present actionable insights

✅ **Performance Optimization**
- Feature scaling
- Reduce dimensionality
- Sample data if needed
- Use efficient algorithms

## Real-World Applications

### Customer Segmentation
```python
# RFM Analysis with clustering
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

rfm_df = customer_data[['recency', 'frequency', 'monetary']]
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_df)

kmeans = KMeans(n_clusters=5, random_state=42)
segments = kmeans.fit_predict(rfm_scaled)

# Analyze segments
segment_profiles = customer_data.groupby(segments).mean()
```

### Market Basket Analysis
```python
from mlxtend.frequent_itemsets import apriori
from mlxtend.association_rules import association_rules

frequent_sets = apriori(transactions, min_support=0.05)
rules = association_rules(frequent_sets, metric='confidence', min_threshold=0.6)
print(rules.sort_values('lift', ascending=False))
```

### Anomaly Detection
```python
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(contamination=0.05, random_state=42)
anomalies = iso_forest.fit_predict(data)
anomaly_scores = iso_forest.score_samples(data)
```

## Learning Resources

**Documentation**
- scikit-learn: https://scikit-learn.org
- UCI ML Repository: https://archive.ics.uci.edu
- Kaggle Datasets: https://www.kaggle.com

**Courses**
- Andrew Ng's ML course (Coursera)
- Fast.ai ML course
- Udacity ML Nanodegree

**Books**
- "Introduction to Data Mining" by Tan, Steinbach, Kumar
- "Python Machine Learning" by Sebastian Raschka
- "The Hundred-Page ML Book"

## Key Takeaways

🎯 **Understand Your Data**
- Exploratory data analysis first
- Know data distribution
- Identify data quality issues

🎯 **Select Right Algorithm**
- Unsupervised vs supervised
- Scalability considerations
- Interpretability needs

🎯 **Validate Results**
- Multiple validation techniques
- Business validation crucial
- Document methodology

🎯 **Communicate Findings**
- Explain patterns clearly
- Provide actionable recommendations
- Visualize effectively

## Next Steps

1. **Beginner**: Start with K-Means clustering
2. **Intermediate**: Learn decision trees and ensemble methods
3. **Advanced**: Explore deep learning and neural networks
4. **Expert**: Implement custom algorithms and optimization

## Practice Exercises

1. Perform customer segmentation on e-commerce data
2. Build a classification model for churn prediction
3. Detect anomalies in credit card transactions
4. Perform market basket analysis on retail data
5. Build a recommendation system using collaborative filtering

## FAQ

**Q: How do I choose the number of clusters?**
A: Use elbow method, silhouette analysis, or domain knowledge

**Q: How do I handle imbalanced datasets?**
A: Use SMOTE, adjust class weights, or change decision threshold

**Q: What's the difference between supervised and unsupervised?**
A: Supervised has labeled data; unsupervised discovers patterns

**Q: How do I explain my model to non-technical stakeholders?**
A: Use visualizations, simple language, and business context
