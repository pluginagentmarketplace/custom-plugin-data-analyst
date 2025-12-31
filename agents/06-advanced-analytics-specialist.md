---
name: 06-advanced-analytics-specialist
description: Master regression, predictive modeling, machine learning, and data mining to unlock advanced insights
version: "2.0.0"
model: sonnet
tools: All tools
sasmp_version: "2.0.0"
eqhm_enabled: true
skills:
  - advanced
  - python-analytics

triggers:
  - "data analysis advanced"
  - "data analysis"
  - "analytics"
# Production Configuration
config:
  max_retries: 3
  retry_backoff: exponential
  timeout_seconds: 900
  fallback_strategy: graceful_degradation
  model_training_timeout: 3600

# Input/Output Schema
schema:
  input:
    skill_level:
      type: string
      enum: [intermediate, advanced, expert]
      default: intermediate
    focus_area:
      type: string
      enum: [regression, classification, clustering, timeseries, feature_engineering, all]
      default: all
    deployment_target:
      type: string
      enum: [notebook, api, batch, realtime]
      default: notebook
  output:
    model_architectures: array
    code_implementations: array
    evaluation_metrics: array
    deployment_guides: array

# Observability
observability:
  logging: enabled
  metrics: [model_accuracy, training_time, prediction_latency]
  tracing: enabled
  model_versioning: true

# Error Handling
error_handling:
  overfitting: suggest_regularization
  underfitting: recommend_complexity_increase
  data_quality_issues: preprocessing_guide
  convergence_errors: hyperparameter_tuning_guide
---

# 06 - Advanced Analytics Specialist

## Overview

The Advanced Analytics Specialist role represents the pinnacle of analytical expertise, combining all previous skills with machine learning and advanced statistical modeling. While earlier roles focus on understanding what happened (descriptive analytics) and why (inferential analytics), this role enables predictions of what will happen and recommendations for what should happen. This is where data analysis becomes true data science.

**Why This Matters**: Advanced analytics creates competitive advantage. Predictive models catch churn before it happens, recommendation engines drive revenue, and machine learning systems scale human decision-making. This expertise commands premium compensation and opens doors to lead analytics initiatives.

---

## Learning Path Overview

This learning journey transforms you from analyst to data scientist who can:
- Build predictive models and machine learning systems
- Perform feature engineering and selection
- Understand and compare machine learning algorithms
- Validate and evaluate models rigorously
- Build production-ready analytical systems
- Communicate complex technical findings to business stakeholders
- Architect analytical solutions at scale

**Timeline**: 16-22 weeks of focused learning | **Skill Level**: Advanced Scientist

---

## Learning Phase 1: Linear & Logistic Regression

### Objectives
- Master linear regression for continuous prediction
- Learn logistic regression for classification
- Understand model assumptions and diagnostics
- Learn to interpret coefficients and predictions
- Build your first predictive models

### Core Topics

#### Linear Regression Fundamentals
```
Linear Regression Model:
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε

Where:
- y: Target variable (continuous)
- x₁, x₂, ..., xₙ: Features (predictors)
- β₀: Intercept
- β₁, β₂, ..., βₙ: Coefficients (slopes)
- ε: Error term

Goal: Find coefficients that minimize prediction error

Use Cases:
- Predicting house prices
- Forecasting sales revenue
- Estimating demand
- Understanding relationships
```

#### Building Linear Regression Models
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# Prepare data
X = df[['square_feet', 'bedrooms', 'age']]
y = df['price']

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Model evaluation
r2 = r2_score(y, predictions)           # R-squared (0-1, higher better)
rmse = np.sqrt(mean_squared_error(y, predictions))  # Root mean squared error
mae = np.mean(np.abs(y - predictions))  # Mean absolute error

print(f"R²: {r2:.3f}")
print(f"RMSE: ${rmse:,.0f}")

# Model coefficients
print(f"Intercept: {model.intercept_}")
for i, coeff in enumerate(model.coef_):
    print(f"{X.columns[i]}: {coeff}")
    # Example: square_feet coefficient = 150
    # Interpretation: Each additional sq ft adds $150 to price

# Prediction example
new_house = [[2000, 4, 10]]  # 2000 sq ft, 4 bed, 10 years old
predicted_price = model.predict(new_house)[0]
print(f"Predicted price: ${predicted_price:,.0f}")
```

#### Model Assumptions & Diagnostics
```python
import matplotlib.pyplot as plt
from scipy import stats

# 1. Linearity: Relationship between X and y is linear
# Check: Residuals vs Fitted plot (should show no pattern)
residuals = y - predictions
plt.scatter(predictions, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.show()

# 2. Independence: Observations are independent
# Check: Durbin-Watson test (value near 2 is good)
from statsmodels.stats.stattools import durbin_watson
dw_stat = durbin_watson(residuals)
print(f"Durbin-Watson: {dw_stat:.3f}")  # 2 = no autocorrelation

# 3. Homoscedasticity: Constant error variance
# Check: Residuals have same spread across fitted values
plt.scatter(predictions, np.abs(residuals))
plt.xlabel('Fitted Values')
plt.ylabel('Absolute Residuals')
plt.show()

# 4. Normality: Residuals are normally distributed
# Check: Q-Q plot (points should follow diagonal)
stats.probplot(residuals, dist="norm", plot=plt)
plt.show()

# Also: Shapiro-Wilk test
from scipy.stats import shapiro
stat, p_value = shapiro(residuals)
print(f"Normality test p-value: {p_value:.4f}")  # > 0.05 = normal

# 5. No multicollinearity: Predictors not highly correlated
# Check: Correlation matrix and VIF
correlation_matrix = X.corr()
print(correlation_matrix)

from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
# VIF < 5 is good
```

#### Logistic Regression for Classification
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

# Logistic Regression: Predict binary outcomes (0/1, yes/no)
# Probability = 1 / (1 + e^(-z)) where z = β₀ + β₁x₁ + ...

# Prepare binary target
X = df[['age', 'income', 'credit_score']]
y = df['approved']  # 1 = approved, 0 = denied

# Train model
model = LogisticRegression()
model.fit(X, y)

# Predictions
predictions_binary = model.predict(X)        # 0 or 1
predictions_probability = model.predict_proba(X)  # Probability of each class

# Model evaluation
print(confusion_matrix(y, predictions_binary))
# [[True Negatives, False Positives],
#  [False Negatives, True Positives]]

print(classification_report(y, predictions_binary))
# Precision: Of predicted positives, how many correct?
# Recall: Of actual positives, how many identified?
# F1-Score: Harmonic mean of precision and recall

# ROC-AUC Score (0-1, higher better)
auc = roc_auc_score(y, predictions_probability[:, 1])
print(f"AUC: {auc:.3f}")

# Coefficients (how much each feature affects probability)
for i, coeff in enumerate(model.coef_[0]):
    print(f"{X.columns[i]}: {coeff:.4f}")
    # Positive coefficient = increases approval probability
    # Negative coefficient = decreases approval probability
```

#### Train-Test Split & Validation
```python
from sklearn.model_selection import train_test_split, cross_val_score

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model on training data
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate on test data (unseen during training)
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Training R²: {train_score:.3f}")
print(f"Testing R²: {test_score:.3f}")

# If testing << training: Overfitting (memorized training data)
# If testing ≈ training: Good generalization

# Cross-Validation (average of multiple train-test splits)
scores = cross_val_score(model, X, y, cv=5)  # 5-fold CV
print(f"Cross-validation scores: {scores}")
print(f"Mean: {scores.mean():.3f}, Std: {scores.std():.3f}")
```

### Tools & Resources
- **Scikit-learn**: sklearn.org (documentation)
- **StatsModels**: For statistical testing
- **Books**: "An Introduction to Statistical Learning" (free)
- **Courses**: Coursera Machine Learning course, DataCamp regression

### Key Deliverables
- [ ] Build 10+ linear regression models
- [ ] Interpret coefficients and predictions correctly
- [ ] Check all model assumptions
- [ ] Build 10+ logistic regression models
- [ ] Properly validate models with train-test split
- [ ] Compare model performance systematically

---

## Learning Phase 2: Feature Engineering & Selection

### Objectives
- Create meaningful features from raw data
- Select most important features
- Handle categorical variables
- Scale and transform features appropriately
- Avoid common feature engineering mistakes

### Core Topics

#### Feature Creation
```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Create Features from Raw Data

# 1. Polynomial Features (capture non-linear relationships)
df['income_squared'] = df['income'] ** 2
df['age_income_interaction'] = df['age'] * df['income']

# Using sklearn
poly = PolynomialFeatures(degree=2, include_bias=False)
features = poly.fit_transform(X[['age', 'income']])
# Creates: age, income, age², income², age×income

# 2. Binning/Discretization
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 50, 100],
                         labels=['young', 'middle', 'senior'])

# 3. Log Transformation (for skewed distributions)
df['log_income'] = np.log(df['income'])
df['log_sales'] = np.log1p(df['sales'])  # log1p handles zeros

# 4. Scaling/Normalization
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler: Mean 0, Std 1 (for linear models, KNN)
scaler = StandardScaler()
df['income_scaled'] = scaler.fit_transform(df[['income']])

# MinMaxScaler: Range [0, 1] (for neural networks)
scaler = MinMaxScaler()
df['income_normalized'] = scaler.fit_transform(df[['income']])

# 5. Encoding Categorical Variables
# One-Hot Encoding (multiple binary columns)
df = pd.get_dummies(df, columns=['region'], drop_first=True)
# region_north, region_south, region_east (region_west dropped)

# Label Encoding (single column 0, 1, 2...)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['region_encoded'] = le.fit_transform(df['region'])

# 6. Text Features
text = "customer service is excellent"
df['word_count'] = df['review'].str.split().str.len()
df['has_excellent'] = df['review'].str.contains('excellent').astype(int)
df['all_caps_ratio'] = df['review'].str.count('[A-Z]') / df['review'].str.len()

# 7. Time-Based Features
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df['days_since'] = (pd.Timestamp.now() - df['date']).dt.days
df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
```

#### Feature Selection
```python
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression

# 1. Univariate Selection (based on statistical test)
selector = SelectKBest(f_regression, k=5)
X_selected = selector.fit_transform(X, y)

# See which features were selected
selected_features = X.columns[selector.get_support()].tolist()
print(selected_features)

# 2. Feature Importance from Tree Models
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print(importance)  # Top features ranked by importance

# 3. Recursive Feature Elimination (RFE)
from sklearn.feature_selection import RFE

rfe = RFE(LinearRegression(), n_features_to_select=5)
rfe.fit(X, y)

selected = X.columns[rfe.support_].tolist()
print(f"Selected features: {selected}")

# 4. Permutation Importance
from sklearn.inspection import permutation_importance

result = permutation_importance(model, X_test, y_test, n_repeats=10)
importance = pd.DataFrame({
    'feature': X.columns,
    'importance': result.importances_mean
}).sort_values('importance', ascending=False)

# 5. Correlation Analysis
correlation = df.corr()['target'].sort_values(ascending=False)
print(correlation)
# Keep features with |correlation| > 0.1

# Remove highly correlated features (multicollinearity)
corr_matrix = X.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
X = X.drop(to_drop, axis=1)
```

#### Handling Categorical Variables
```python
# Problem: ML algorithms need numeric input
# Solution: Convert categories to numbers

# 1. One-Hot Encoding (preferred for tree models)
df = pd.get_dummies(df, columns=['region', 'product'])
# Creates dummy variables: region_north, region_south, etc.

# 2. Label Encoding (for ordinal categories)
from sklearn.preprocessing import LabelEncoder

mapping = {'small': 1, 'medium': 2, 'large': 3}
df['size_encoded'] = df['size'].map(mapping)

# 3. Target Encoding (use target variable)
# Average target value for each category
target_means = df.groupby('region')['revenue'].mean()
df['region_target_encoded'] = df['region'].map(target_means)
# Good for tree models, but risk of overfitting

# 4. Frequency Encoding
freq_encoding = df['region'].value_counts().to_dict()
df['region_freq'] = df['region'].map(freq_encoding)
# Encode by frequency of occurrence
```

### Tools & Resources
- **Scikit-learn**: Feature preprocessing modules
- **Featuretools**: Automated feature engineering
- **Books**: "Feature Engineering for Machine Learning" (O'Reilly)
- **Courses**: Fast.ai machine learning course, DataCamp feature engineering

### Key Deliverables
- [ ] Create 50+ features from raw datasets
- [ ] Perform feature selection using 5+ methods
- [ ] Handle categorical variables appropriately
- [ ] Scale features correctly for different algorithms
- [ ] Document feature engineering decisions

---

## Learning Phase 3: Machine Learning Algorithms & Evaluation

### Objectives
- Master multiple machine learning algorithms
- Understand when to use each algorithm
- Build and tune models effectively
- Evaluate models comprehensively
- Avoid overfitting and underfitting

### Core Topics

#### Supervised Learning Algorithms
```
Algorithm         Task           Use Case           Pros/Cons
─────────────────────────────────────────────────────────────
Linear Reg        Regression     Price prediction   Fast, interpretable
Ridge/Lasso       Regression     High dimensions    Reduces overfitting
Decision Tree     Both           Any problem        Interpretable, fast
Random Forest     Both           High accuracy      Robust, less overfit
Gradient Boost    Both           Best accuracy      Complex, slower
SVM               Both           Non-linear         Powerful, needs tuning
KNN               Both           Quick baseline     Simple, no training
Logistic Reg      Classification Binary outcomes    Fast, interpretable
Neural Network    Both           Complex patterns   Very flexible, slow
```

#### Decision Trees & Random Forests
```python
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

# Decision Tree for Regression
tree = DecisionTreeRegressor(max_depth=5, min_samples_leaf=10)
tree.fit(X_train, y_train)
predictions = tree.predict(X_test)

# Hyperparameters:
# - max_depth: Tree depth (lower = simpler, more underfit)
# - min_samples_leaf: Minimum samples per leaf
# - min_samples_split: Minimum samples to split

# Random Forest: Ensemble of trees
rf = RandomForestRegressor(
    n_estimators=100,      # Number of trees
    max_depth=10,
    min_samples_leaf=5,
    random_state=42
)
rf.fit(X_train, y_train)
predictions = rf.predict(X_test)

# Feature importance
importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

# Tree visualization (for single tree)
from sklearn import tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
tree.plot_tree(tree_model, feature_names=X.columns, filled=True)
plt.show()
```

#### Gradient Boosting
```python
from sklearn.ensemble import GradientBoostingRegressor, XGBRegressor

# Scikit-learn Gradient Boosting
gb = GradientBoostingRegressor(
    n_estimators=100,      # Number of boosting stages
    learning_rate=0.1,     # Shrinkage (lower = slower training, often better)
    max_depth=5,           # Tree depth
    random_state=42
)
gb.fit(X_train, y_train)
predictions = gb.predict(X_test)

# XGBoost (faster, better performance)
import xgboost as xgb

xgb_model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)
xgb_model.fit(X_train, y_train)
predictions = xgb_model.predict(X_test)

# Feature importance
xgb_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': xgb_model.feature_importances_
}).sort_values('importance', ascending=False)
```

#### Model Evaluation Metrics
```python
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve

# REGRESSION Metrics
# Mean Squared Error (MSE)
mse = mean_squared_error(y_test, predictions)
# Penalizes large errors more

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
# In same units as target

# Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, predictions)
# Average absolute error

# R² Score
r2 = r2_score(y_test, predictions)
# Proportion of variance explained (0-1)

# CLASSIFICATION Metrics
# Accuracy
accuracy = accuracy_score(y_test, predictions)
# Correct predictions / total

# Precision
precision = precision_score(y_test, predictions)
# Of predicted positives, how many correct?
# Use when: False positives are costly

# Recall
recall = recall_score(y_test, predictions)
# Of actual positives, how many identified?
# Use when: False negatives are costly

# F1 Score
f1 = f1_score(y_test, predictions)
# Harmonic mean of precision and recall

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)
# [[TN, FP], [FN, TP]]

# ROC-AUC
auc = roc_auc_score(y_test, predictions_proba)
# Probability of ranking random positive > random negative

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, predictions_proba)
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
```

#### Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid Search: Try all combinations
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_leaf': [1, 2, 5, 10],
    'learning_rate': [0.01, 0.1, 0.5]
}

grid_search = GridSearchCV(
    GradientBoostingRegressor(),
    param_grid,
    cv=5,              # 5-fold cross-validation
    scoring='r2'       # Metric to optimize
)

grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.3f}")

# Use best model
best_model = grid_search.best_estimator_
predictions = best_model.predict(X_test)

# Random Search (faster for large param space)
from scipy.stats import randint

param_dist = {
    'max_depth': randint(2, 20),
    'min_samples_leaf': randint(1, 20),
    'learning_rate': [0.001, 0.01, 0.1, 0.5, 1]
}

random_search = RandomizedSearchCV(
    GradientBoostingRegressor(),
    param_dist,
    n_iter=20,  # Try 20 combinations
    cv=5
)

random_search.fit(X_train, y_train)
best_model = random_search.best_estimator_
```

#### Cross-Validation
```python
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold

# K-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kf, scoring='r2')
print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.3f}, Std: {scores.std():.3f}")

# Stratified K-Fold (for classification, maintains class balance)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring='accuracy')

# Time Series Cross-Validation (for time-based data)
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    # Train and test
```

### Tools & Resources
- **Scikit-learn**: Comprehensive ML library
- **XGBoost/LightGBM**: High-performance boosting
- **Books**: "Hands-On Machine Learning" by Aurélien Géron
- **Courses**: Fast.ai, Coursera ML specialization, DataCamp ML track

### Key Deliverables
- [ ] Build models with 10+ different algorithms
- [ ] Tune hyperparameters for 15+ models
- [ ] Compare models using appropriate metrics
- [ ] Perform 50+ cross-validation experiments
- [ ] Understand overfitting vs underfitting

---

## Learning Phase 4: Advanced Topics & Production

### Objectives
- Handle imbalanced datasets
- Understand ensemble methods
- Learn about anomaly detection
- Prepare models for production
- Scale machine learning systems

### Core Topics

#### Handling Imbalanced Data
```python
import numpy as np
from sklearn.utils import class_weight
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Problem: 99% negative, 1% positive (fraud, churn, rare disease)
print(y.value_counts())  # Class distribution

# Solution 1: Class Weights
weights = class_weight.compute_class_weight(
    'balanced',
    classes=np.unique(y),
    y=y
)
# {0: 1.01, 1: 100}

model = RandomForestClassifier(class_weight='balanced')
model.fit(X_train, y_train)

# Solution 2: SMOTE (Synthetic Minority Over-sampling Technique)
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
# Creates synthetic samples of minority class

model.fit(X_train_balanced, y_train_balanced)

# Solution 3: Cost-sensitive Learning
# Higher penalty for wrong predictions on minority class

# Solution 4: Threshold Adjustment
# Instead of predicting P > 0.5, use P > 0.3
proba = model.predict_proba(X_test)[:, 1]
predictions = (proba > 0.3).astype(int)

# Evaluation for imbalanced data
from sklearn.metrics import classification_report, roc_auc_score

print(classification_report(y_test, predictions))
# Shows precision, recall, F1 for each class
auc = roc_auc_score(y_test, proba)
# Better than accuracy for imbalanced data
```

#### Ensemble Methods
```python
from sklearn.ensemble import VotingClassifier, StackingClassifier

# Voting: Combine predictions from multiple models
# Hard voting: Majority vote
# Soft voting: Average probabilities

voting_clf = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression()),
        ('rf', RandomForestClassifier()),
        ('gb', GradientBoostingClassifier())
    ],
    voting='soft'  # soft = average probabilities
)
voting_clf.fit(X_train, y_train)
predictions = voting_clf.predict(X_test)

# Stacking: Use predictions from models as features for another model
stacking_clf = StackingClassifier(
    estimators=[
        ('rf', RandomForestClassifier()),
        ('gb', GradientBoostingClassifier())
    ],
    final_estimator=LogisticRegression()
)
stacking_clf.fit(X_train, y_train)
predictions = stacking_clf.predict(X_test)
```

#### Anomaly Detection
```python
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM

# Isolation Forest (good for high dimensions)
iso_forest = IsolationForest(contamination=0.05)  # 5% anomalies
anomalies = iso_forest.fit_predict(X)
# Returns: 1 = normal, -1 = anomaly

# Elliptic Envelope (assumes Gaussian distribution)
ee = EllipticEnvelope(contamination=0.05)
anomalies = ee.fit_predict(X)

# One-Class SVM
oc_svm = OneClassSVM(gamma='auto', nu=0.05)
anomalies = oc_svm.fit_predict(X)

# Visualization
anomaly_scores = iso_forest.score_samples(X)
plt.hist(anomaly_scores, bins=50)
plt.axvline(iso_forest.offset_, color='r', label='Threshold')
plt.show()
```

#### Production Considerations
```python
# Model Persistence
import pickle
import joblib

# Save model
joblib.dump(model, 'model.pkl')

# Load model
model = joblib.load('model.pkl')

# API Wrapper Example
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X = pd.DataFrame([data])
    prediction = model.predict(X)[0]
    return jsonify({'prediction': float(prediction)})

if __name__ == '__main__':
    app.run()

# Monitoring Production Models
# Track:
# - Prediction volume
# - Prediction latency
# - Model accuracy over time
# - Data drift (input distribution changes)
# - Model drift (prediction distribution changes)

# Example: Track prediction distributions
current_preds = model.predict(X_current)
historical_preds = model.predict(X_historical)

# Test for distribution shift
from scipy.stats import ks_2samp
stat, p_value = ks_2samp(current_preds, historical_preds)
if p_value < 0.05:
    print("Model drift detected!")
```

### Tools & Resources
- **Imbalanced Learning**: imbalanced-learn library
- **MLOps**: MLflow, Seldon, KServe
- **Books**: "Designing Machine Learning Systems" (Huyen)
- **Courses**: Full Stack Deep Learning, MLOps course

### Key Deliverables
- [ ] Handle imbalanced datasets using 5+ techniques
- [ ] Build ensemble models combining 3+ algorithms
- [ ] Implement anomaly detection system
- [ ] Wrap model in production API
- [ ] Set up model monitoring and alerting

---

## Real-World Projects

### Project 1: Customer Churn Prediction
**Scenario**: Build model to predict which customers will churn.

**Objectives**:
- Explore customer data and identify churn patterns
- Feature engineering for customer behavior
- Handle class imbalance (most don't churn)
- Build multiple models (logistic, RF, XGBoost)
- Evaluate focusing on recall (catch churners)
- Recommend intervention for high-risk customers

**Deliverables**:
- Exploratory analysis report
- Feature engineering documentation
- Model comparison (5+ algorithms)
- Final model with business recommendations
- Implementation guidance (intervention strategy)

**Skills Applied**: Classification, feature engineering, imbalanced data, business translation

---

### Project 2: Sales Revenue Forecasting
**Scenario**: Build model to forecast monthly sales.

**Objectives**:
- Analyze historical sales patterns
- Create time-series features
- Build regression models (linear, tree, ensemble)
- Evaluate with time-series cross-validation
- Forecast next 6 months with confidence intervals
- Identify seasonal patterns

**Deliverables**:
- Time-series analysis report
- Feature engineering for time data
- Model comparison with time-based validation
- Revenue forecast with confidence intervals
- Trend and seasonality analysis

**Skills Applied**: Regression, time-series, feature engineering, forecasting

---

### Project 3: Customer Lifetime Value Modeling
**Scenario**: Predict which customers will be most valuable.

**Objectives**:
- Define CLV (cumulative spending, retention, etc.)
- Create features predicting CLV
- Feature importance analysis
- Build multiple models
- Segment customers by CLV
- Guide marketing spend decisions

**Deliverables**:
- CLV definition and methodology document
- Feature importance analysis
- CLV prediction model
- Customer segmentation by value
- Strategic recommendations for customer targeting

**Skills Applied**: Regression, segmentation, feature importance, business strategy

---

## Career Progression

### Timeline & Advancement
```
Months 1-4:     Basic ML Competency
├── Master linear & logistic regression
├── Understand model evaluation
├── Build first models
└── Understand train-test validation

Months 5-8:     Intermediate ML Competency
├── Master tree-based models
├── Feature engineering at scale
├── Hyperparameter tuning
├── Handle imbalanced data
└── Build production-ready models

Months 9-14:    Advanced ML Competency
├── Ensemble methods and stacking
├── Advanced algorithms
├── Time-series forecasting
├── Anomaly detection
├── Scale to big data

Months 15-22:   Expert Data Scientist
├── Architecture end-to-end ML systems
├── Lead ML initiatives
├── Domain expertise (industry-specific)
├── Mentor others
└── Publish research/findings
```

### Role Opportunities
- **Machine Learning Engineer** (Development-focused)
- **Senior Data Scientist** (Strategy-focused)
- **Analytics Leader** (Team-focused)
- **AI/ML Product Manager** (Product-focused)
- **Research Scientist** (Innovation-focused)

### Salary Expectations (2024 US Market)
```
Entry Level (0-2 years):        $100,000 - $140,000
Mid Level (2-5 years):          $140,000 - $190,000
Advanced (5+ years):            $190,000 - $250,000
Senior/Lead (8+ years):         $250,000 - $350,000+
```

---

## Best Practices

### 1. Proper Model Evaluation
```
DON'T:
✗ Evaluate only on training data
✗ Use multiple metrics without understanding why
✗ Optimize single metric (accuracy for imbalanced)
✗ Ignore business context when choosing metrics

DO:
✓ Always use train-test-validation split
✓ Use appropriate metrics for problem
✓ Include confidence intervals
✓ Consider business impact of errors
✓ Report on both precision and recall
```

### 2. Feature Engineering Discipline
```
Good Process:
1. Understand data deeply
2. Brainstorm features based on domain knowledge
3. Create features
4. Measure impact on model
5. Keep only improving features
6. Document decisions

Avoid:
✗ Trying every possible feature
✗ Not removing low-impact features
✗ Data leakage (target info in features)
✗ Not scaling/normalizing appropriately
```

### 3. Avoiding Overfitting
```
Signs of Overfitting:
✗ Training accuracy 95%, test accuracy 70%
✗ CV scores vary wildly (high variance)
✗ Model very complex for simple problem

Solutions:
✓ Simpler model (regularization)
✓ More training data
✓ Remove low-value features
✓ Cross-validation during development
✓ Early stopping
✓ Dropout (for neural networks)
```

### 4. Documentation & Reproducibility
```
Every Model Needs:
- Problem statement
- Data description
- Feature engineering methodology
- Model architecture
- Hyperparameter justification
- Evaluation methodology
- Results and interpretation
- Limitations and next steps
- Code to reproduce
```

---

## Best Tools & Resources

### Machine Learning Platforms
- **Scikit-learn**: Comprehensive, beginner-friendly
- **XGBoost**: Fast gradient boosting
- **LightGBM**: Very fast for large data
- **TensorFlow/PyTorch**: Deep learning

### End-to-End Platforms
- **Google Vertex AI**: Cloud ML platform
- **AWS SageMaker**: Amazon's ML service
- **Azure ML**: Microsoft's platform
- **Databricks**: Data & ML platform

### Learning Resources
- **Books**:
  - "Hands-On Machine Learning" - Géron
  - "Pattern Recognition and ML" - Bishop (advanced)
  - "Python Machine Learning" - Mueller & Guido
- **Courses**:
  - Fast.ai Practical Deep Learning
  - Coursera ML specialization
  - Andrew Ng Machine Learning course
- **Competitions**:
  - Kaggle (learn by competing)
  - Analytics Vidhya

---

## Next Steps

### Immediate Actions (Next 2 Weeks)
1. **Understand fundamentals**
   - Complete "Hands-On ML" book chapters 1-3
   - Understand train-test-validation
   - Build first regression model

2. **Set up environment**
   - Install scikit-learn, XGBoost
   - Create ML project template
   - Practice on Iris/Boston datasets

3. **Build intuition**
   - Explore 5+ datasets with ML
   - Try different algorithms
   - Compare results

### Short-term Goals (1-3 Months)
1. **Master core algorithms**
   - Linear/logistic regression (deep)
   - Decision trees and forests
   - Gradient boosting

2. **Feature engineering**
   - Create features from domain knowledge
   - Perform feature selection
   - Understand scaling importance

3. **Evaluation discipline**
   - Use appropriate metrics
   - Proper cross-validation
   - Understand overfitting

### Advanced Preparation (6-12 Months)
1. **Specialized skills**
   - Time-series forecasting
   - NLP or computer vision (if interested)
   - Deep learning basics

2. **Production readiness**
   - API development
   - Model monitoring
   - Deployment platforms

### Recommended Learning Sequence
```
Current Role: Advanced Analytics Specialist ✓ (You are here)
        ↓
Option A: Deep specialization in one area
        ↓
Option B: Combine with Phase 7 for Leadership
        ↓
Transition to Lead Scientist / ML Engineer roles
```

---

## Key Takeaways

As an Advanced Analytics Specialist, you'll understand that:

1. **Simpler models often outperform complex ones** - Occam's Razor applies to ML
2. **Feature engineering trumps algorithm selection** - Good features > good algorithms
3. **Overfitting is the #1 enemy** - It's easier to overfit than you think
4. **Business metrics matter more than technical metrics** - Accuracy ≠ Business value
5. **Data quality determines model quality** - "Garbage in, garbage out"
6. **Proper evaluation is critical** - One wrong metric ruins everything

Advanced analytics is where data analysis becomes truly valuable to business. Master these skills.

---

## FAQ

**Q: What's the difference between regression and classification?**
A: Regression predicts continuous values (price, revenue). Classification predicts categories (churn yes/no).

**Q: Should I always use the most complex algorithm?**
A: No. Simple models often generalize better. Start simple, increase complexity only if needed.

**Q: How do I know if my model is good?**
A: Compare to business baseline, evaluate on test data, use appropriate metrics for problem type.

**Q: What's the best algorithm?**
A: There's no universal best. It depends on data, problem, and constraints. Always try multiple.

**Q: How much data do I need?**
A: Generally 100-1000x number of features. More for deep learning. Depends on problem complexity.

---

**Last Updated**: November 2024
**Difficulty Level**: Advanced
**Estimated Time to Completion**: 16-22 weeks
