---
name: "Predictive Modeling"
description: "Master decision trees, random forests, neural networks, and model evaluation techniques for advanced predictions"
category: "Advanced"
level: "Advanced"
duration: "6-8 weeks"
---

# Predictive Modeling

## Quick Start

Predictive modeling builds models to forecast future outcomes. Within your first week, you'll build decision trees that are interpretable. By week four, you'll ensemble multiple models for better accuracy and apply neural networks to complex patterns.

**First Task (40 minutes):**
1. Load classification dataset (e.g., customer churn)
2. Build decision tree and evaluate
3. Build random forest ensemble
4. Compare model accuracy and interpretability
5. Create feature importance visualization

## Key Concepts

### 1. Decision Trees
**What it is:** Tree-like model that makes sequential decisions to reach predictions.

**How It Works:**
```
Decision Tree for Loan Approval:
┌─── Income > $50k? ───┬─── NO: Reject
│                       ├─── YES: Employment stable?
│                           ├─── NO: Reject
│                           └─── YES: Credit score > 700?
│                               ├─── NO: Reject
│                               └─── YES: Approve
```

**Advantages:**
- Interpretable: Easy to explain decisions
- Handles non-linear relationships
- Feature importance built-in
- Works with mixed data types

**Disadvantages:**
- Prone to overfitting
- Unstable (small data change = big tree change)
- May create very deep trees

**Example (Python):**
```python
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Create and fit
tree = DecisionTreeClassifier(max_depth=5, min_samples_split=10)
tree.fit(X_train, y_train)

# Predictions
y_pred = tree.predict(X_test)
probability = tree.predict_proba(X_test)  # [prob_no, prob_yes]

# Feature importance
for feature, importance in zip(X.columns, tree.feature_importances_):
    print(f"{feature}: {importance:.3f}")

# Visualize tree
plot_tree(tree, feature_names=X.columns, filled=True)
plt.show()
```

### 2. Random Forests & Ensemble Methods
**What it is:** Combining multiple models to improve predictions beyond any single model.

**Random Forest Algorithm:**
```
1. Build multiple decision trees on random subsets
2. Each tree sees different data and random features
3. Average predictions (regression) or majority vote (classification)
4. Result: More stable, less overfit than single tree
```

**Key Parameters:**
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,        # Number of trees
    max_depth=10,            # Max tree depth
    min_samples_split=5,     # Min samples to split node
    min_samples_leaf=2,      # Min samples in leaf
    max_features='sqrt',     # Features per split
    random_state=42,
    n_jobs=-1               # Use all CPU cores
)
```

**Feature Importance (from Random Forest):**
```python
importances = model.feature_importances_
sorted_features = sorted(zip(X.columns, importances), key=lambda x: x[1], reverse=True)
for feature, importance in sorted_features[:10]:
    print(f"{feature}: {importance:.3f}")

# Visualize
plt.barh(X.columns[importance_idx], importances[importance_idx])
plt.xlabel('Importance')
plt.show()
```

**Other Ensemble Methods:**
```python
# Gradient Boosting (sequential trees, each corrects previous)
from sklearn.ensemble import GradientBoostingClassifier
gbm = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)

# XGBoost (optimized gradient boosting)
from xgboost import XGBClassifier
xgb = XGBClassifier(n_estimators=100, max_depth=5)

# AdaBoost (weights misclassified samples more)
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier(n_estimators=50)

# Voting Ensemble (combine different model types)
from sklearn.ensemble import VotingClassifier
ensemble = VotingClassifier(
    estimators=[('tree', tree), ('rf', rf), ('xgb', xgb)],
    voting='soft'  # Average probabilities
)
```

### 3. Neural Networks & Deep Learning
**What it is:** Models inspired by neurons that learn complex patterns.

**When to Use Neural Networks:**
```
Images, text, time series, complex non-linear relationships
NOT for simple tabular data with limited samples

Advantages:
- Can learn very complex patterns
- Transfer learning (pre-trained models)
- End-to-end learning

Disadvantages:
- "Black box" - hard to interpret
- Requires lots of data
- Slow to train
- Sensitive to hyperparameters
```

**Basic Neural Network (Python with TensorFlow):**
```python
from tensorflow import keras
import numpy as np

# Build sequential model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    keras.layers.Dropout(0.2),  # Prevent overfitting
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')  # Binary classification
])

# Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,  # Use 20% for validation
    verbose=1
)

# Predict
y_pred = model.predict(X_test)
```

**Network Architecture:**
```
Input Layer (10 features)
    ↓
Dense(64, relu) - Hidden layer 1
    ↓
Dropout(0.2) - Prevent overfitting
    ↓
Dense(32, relu) - Hidden layer 2
    ↓
Dropout(0.2)
    ↓
Dense(16, relu) - Hidden layer 3
    ↓
Dense(1, sigmoid) - Output (0 to 1)
```

### 4. Model Evaluation & Comparison
**What it is:** Comprehensive evaluation beyond accuracy.

**Classification Metrics:**
```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, roc_curve
)

# Basic metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Area under ROC curve
auc = roc_auc_score(y_test, y_pred_proba)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
# [[True Neg, False Pos],
#  [False Neg, True Pos]]
```

**Regression Metrics:**
```python
from sklearn.metrics import mean_squared_error, r2_score

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
mae = np.mean(np.abs(y_test - y_pred))
```

**Model Comparison:**
```python
models = {
    'Decision Tree': tree,
    'Random Forest': rf,
    'XGBoost': xgb,
    'Neural Network': nn
}

results = {}
for name, model in models.items():
    y_pred = model.predict(X_test)
    results[name] = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1': f1_score(y_test, y_pred)
    }

comparison_df = pd.DataFrame(results).T
print(comparison_df)
```

### 5. Hyperparameter Tuning & Optimization
**What it is:** Finding best settings for models.

**Grid Search:**
```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
params = {
    'max_depth': [5, 10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'n_estimators': [50, 100, 200]
}

# Search
grid_search = GridSearchCV(
    RandomForestClassifier(),
    params,
    cv=5,  # 5-fold cross-validation
    n_jobs=-1,  # Use all cores
    verbose=1
)
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.3f}")

best_model = grid_search.best_estimator_
```

**Random Search:**
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Define distributions
distributions = {
    'max_depth': randint(3, 20),
    'n_estimators': randint(50, 500),
    'learning_rate': uniform(0.01, 0.3)
}

random_search = RandomizedSearchCV(
    GradientBoostingClassifier(),
    distributions,
    n_iter=20,  # Try 20 combinations
    cv=5,
    random_state=42
)
random_search.fit(X_train, y_train)
```

**Early Stopping (for gradient boosting):**
```python
xgb = XGBClassifier(n_estimators=1000)
xgb.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    early_stopping_rounds=10,  # Stop if no improvement for 10 rounds
    verbose=10
)
```

## Tools and Resources

**Python Libraries:**
- scikit-learn: Decision trees, ensemble methods
- XGBoost: Gradient boosting
- TensorFlow/Keras: Neural networks
- PyTorch: Deep learning framework
- H2O: AutoML (automatic model tuning)

**R Libraries:**
```r
# Decision trees
library(rpart)
tree <- rpart(target ~ ., data=df)

# Random Forest
library(randomForest)
rf <- randomForest(target ~ ., data=df)

# XGBoost
library(xgboost)
xgb <- xgboost(data, label=y, nrounds=100)

# Neural networks
library(keras)
```

**Learning Resources:**
- Kaggle Competitions: Real-world practice
- Fast.ai: Deep learning course (free)
- "Hands-On Machine Learning" book
- StatQuest: YouTube ML tutorials
- Scikit-learn Official Documentation

## Best Practices

1. **Start Simple:** Decision tree before ensemble before neural network
2. **Baseline First:** Compare against simple model
3. **Feature Engineering:** Matters more than model choice
4. **Cross-Validate:** Never evaluate on training data
5. **Tune Thoughtfully:** Grid search on cv, not test set
6. **Monitor Overfitting:** Watch train vs validation performance
7. **Interpret Results:** Explain why model makes predictions
8. **Handle Class Imbalance:** Use SMOTE, class weights, or stratified CV
9. **Calibrate Probabilities:** Ensure predicted probabilities are reliable
10. **Iterate:** Continuous improvement cycle

## Next Steps

1. **Week 1-2:** Master decision trees and understand tree concepts
2. **Week 2-3:** Build random forests and explore feature importance
3. **Week 3-4:** Learn ensemble methods and hyperparameter tuning
4. **Week 4-5:** Build and tune neural networks
5. **Week 5-6:** Model comparison and selection
6. **Week 6-7:** Deploy models and monitor performance
7. **Week 7-8:** AutoML and advanced techniques
8. **After:** Production ML, online learning, model monitoring
9. **Progression:** Simple Models → Ensembles → Deep Learning → Production ML
