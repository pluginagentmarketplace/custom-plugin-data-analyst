---
name: "Regression Analysis"
description: "Master linear and logistic regression including assumptions, diagnostics, and prediction modeling"
category: "Advanced"
level: "Advanced"
duration: "5-6 weeks"
---

# Regression Analysis

## Quick Start

Regression models predict continuous values based on features. Within your first week, you'll build linear regression models and evaluate predictions. By week four, you'll understand when to use logistic regression for classification and apply advanced diagnostics.

**First Task (35 minutes):**
1. Load data with continuous outcome variable
2. Build simple linear regression model
3. Generate predictions on new data
4. Check model performance (R-squared, RMSE)
5. Create residual plot to check assumptions

## Key Concepts

### 1. Linear Regression Fundamentals
**What it is:** Predicting a continuous target from features using a line/plane.

**Simple Linear Regression:**
```
y = β0 + β1*x + ε

Where:
y = target variable (continuous)
x = feature variable
β0 = intercept (y when x=0)
β1 = slope (change in y per unit change in x)
ε = error/residual
```

**Example (Python with scikit-learn):**
```python
from sklearn.linear_model import LinearRegression
import pandas as pd

# Load data
df = pd.read_csv('house_prices.csv')
X = df[['square_feet']]  # Features (2D array)
y = df['price']          # Target (1D array)

# Create and fit model
model = LinearRegression()
model.fit(X, y)

# Make predictions
new_data = [[2000]]
prediction = model.predict(new_data)  # Predicted price for 2000 sq ft

# Model coefficients
print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")
# Interpretation: For each additional sq foot, price increases by $X
```

**Multiple Linear Regression:**
```python
# With multiple features
X = df[['square_feet', 'bedrooms', 'bathrooms', 'age']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Get coefficients
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")

# Prediction
new_house = [[3000, 4, 2.5, 10]]
prediction = model.predict(new_house)
```

### 2. Model Evaluation & Assumptions
**What it is:** Assessing model quality and checking if regression is appropriate.

**Performance Metrics:**
```
R-squared (R²): Proportion of variance explained
- Range: 0 to 1
- Higher is better
- Example: R² = 0.85 means 85% of price variation explained

Root Mean Squared Error (RMSE): Average prediction error
- Same units as target
- Lower is better
- Example: RMSE = $50,000 means average prediction off by $50k

Mean Absolute Error (MAE): Average absolute error
- Same units as target
- More robust to outliers than RMSE
- Example: MAE = $35,000

Adjusted R²: R² adjusted for number of features
- Penalizes adding features that don't improve predictions
- Use when comparing models with different numbers of features
```

**Python Example:**
```python
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

y_pred = model.predict(X)
rmse = np.sqrt(mean_squared_error(y, y_pred))
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"R²: {r2:.3f}")
print(f"RMSE: ${rmse:,.0f}")
print(f"MAE: ${mae:,.0f}")
```

**Regression Assumptions:**
```
1. Linearity: Relationship between X and y is linear
   Check: Scatter plot, residual plot

2. Independence: Observations are independent
   Check: No time patterns in residuals

3. Homoscedasticity: Constant variance of errors
   Check: Spread of residuals constant across fitted values

4. Normality: Errors are normally distributed
   Check: Q-Q plot, histogram of residuals

5. No Multicollinearity: Features not highly correlated
   Check: Correlation matrix, VIF (Variance Inflation Factor)

Diagnostics:
- Residual plot: Fitted values vs residuals
- Q-Q plot: Quantile-quantile plot for normality
- Scale-location: Standardized residuals vs fitted values
```

### 3. Feature Engineering & Selection
**What it is:** Creating and selecting features that improve model performance.

**Feature Engineering:**
```python
# Polynomial features (capture non-linear relationships)
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(df[['square_feet']])
# Creates: 1, square_feet, square_feet²

# Interaction terms
df['age_rooms_interaction'] = df['age'] * df['bedrooms']

# Binning continuous variables
df['size_category'] = pd.cut(df['square_feet'],
                             bins=[0, 1500, 2500, 5000],
                             labels=['small', 'medium', 'large'])

# Log transformation (for skewed data)
df['log_price'] = np.log(df['price'])

# Dummy variables (categorical to numeric)
df_encoded = pd.get_dummies(df, columns=['neighborhood'])
```

**Feature Selection:**
```python
# Remove highly correlated features
correlation = X.corr().abs()
# Keep features with correlation < 0.8

# Backward elimination (start with all, remove least important)
from sklearn.feature_selection import RFE

selector = RFE(estimator=model, n_features_to_select=5)
selector.fit(X, y)
X_selected = selector.transform(X)

# Regularization (built-in feature selection)
from sklearn.linear_model import Ridge, Lasso

# Ridge: Shrinks coefficients (keeps all features)
ridge = Ridge(alpha=1.0)
ridge.fit(X, y)

# Lasso: Sets some coefficients to zero (removes features)
lasso = Lasso(alpha=1.0)
lasso.fit(X, y)
```

### 4. Logistic Regression
**What it is:** Predicting binary outcomes (yes/no, 0/1).

**When to Use:**
```
Regression: Target is continuous (price, age, revenue)
Logistic Regression: Target is binary (purchased Y/N, default Y/N)

Output: Probability (0 to 1)
Decision boundary: Usually 0.5
- If P > 0.5: Predict "yes"
- If P ≤ 0.5: Predict "no"
```

**Example (Python):**
```python
from sklearn.linear_model import LogisticRegression

# Create binary target
df['purchased'] = (df['purchased'] == 'Yes').astype(int)

X = df[['age', 'income', 'previous_purchases']]
y = df['purchased']

# Fit logistic regression
model = LogisticRegression()
model.fit(X, y)

# Predictions
new_customer = [[35, 50000, 3]]
probability = model.predict_proba(new_customer)[0][1]  # Prob of purchasing
prediction = model.predict(new_customer)[0]  # 0 or 1

# Model coefficients (log-odds)
for feature, coef in zip(X.columns, model.coef_[0]):
    odds_ratio = np.exp(coef)
    print(f"{feature}: 1 unit increase → {odds_ratio:.2f}x odds of purchase")
```

**Evaluation Metrics:**
```
Accuracy: (TP + TN) / Total
- Example: 90% of predictions correct
- Problem: Bad for imbalanced data

Precision: TP / (TP + FP)
- Of predicted positives, how many correct?
- Important when false positives are costly

Recall (Sensitivity): TP / (TP + FN)
- Of actual positives, how many caught?
- Important when false negatives are costly

F1-Score: Harmonic mean of precision and recall
- Balanced metric for imbalanced data

ROC-AUC: Area under receiver operating characteristic curve
- Ranges 0 to 1 (higher is better)
- Robust to class imbalance
```

### 5. Model Validation & Overfitting
**What it is:** Ensuring models generalize to new data, not just fit training data.

**Train/Test Split:**
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train on training set
model.fit(X_train, y_train)

# Evaluate on both
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

# If train >> test: Overfitting (memorized training data)
# If train ≈ test: Good generalization
```

**Cross-Validation:**
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)  # 5-fold
print(f"Mean score: {scores.mean():.3f}")
print(f"Std dev: {scores.std():.3f}")
# More robust estimate of generalization performance
```

**Regularization (Combat Overfitting):**
```python
# Ridge Regression (L2 regularization)
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)  # Higher alpha = more regularization

# Lasso Regression (L1 regularization)
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.1)  # Higher alpha = fewer features

# ElasticNet (combination)
from sklearn.linear_model import ElasticNet
model = ElasticNet(alpha=1.0, l1_ratio=0.5)
```

## Tools and Resources

**Python Libraries:**
- scikit-learn: Regression models and evaluation
- statsmodels: Statistical tests and summaries
- numpy/pandas: Data manipulation
- matplotlib/seaborn: Visualization

**R Libraries:**
```r
# Linear regression
model <- lm(price ~ square_feet, data=df)
summary(model)

# Logistic regression
model <- glm(purchased ~ age + income, data=df, family=binomial)

# Model diagnostics
plot(model)
```

**Learning Resources:**
- Scikit-learn Documentation: Regression guide
- StatQuest with Josh Starmer: YouTube regression tutorials
- "Introduction to Statistical Learning": Free online book
- Coursera: Machine Learning specialization

## Best Practices

1. **Check Assumptions:** Never skip residual analysis
2. **Feature Scaling:** Many algorithms benefit from normalized features
3. **Handle Outliers:** Check for data entry errors or legitimate extremes
4. **Interpret Coefficients:** Understand what each feature means
5. **Avoid Overfitting:** Use train/test split and cross-validation
6. **Regularize When Needed:** Ridge/Lasso for many features
7. **Document Model Choices:** Why this model, not alternatives?
8. **Monitor Model Drift:** Refit regularly on new data
9. **Validate on Holdout Set:** Final performance on unseen data
10. **Simple Model First:** Start with linear regression, add complexity if needed

## Next Steps

1. **Week 1-2:** Master linear regression and model evaluation
2. **Week 2-3:** Understand assumptions and diagnostics
3. **Week 3-4:** Learn feature engineering and selection
4. **Week 4-5:** Apply logistic regression to classification problems
5. **Week 5-6:** Practice model validation and regularization
6. **After:** Move to advanced models (decision trees, ensembles)
7. **Progression:** Regression → Tree-based Models → Neural Networks
