# Advanced Analytics Guide

## Linear Regression
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f"R²: {model.score(X_test, y_test)}")
```

## A/B Testing
1. Define hypothesis
2. Calculate sample size
3. Run experiment
4. Analyze with t-test
5. Make decision
