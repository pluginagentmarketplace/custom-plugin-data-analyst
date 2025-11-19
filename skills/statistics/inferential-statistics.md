---
name: "Inferential Statistics"
description: "Master hypothesis testing, p-values, confidence intervals, t-tests, and ANOVA for data-driven decision making"
category: "Statistics"
level: "Intermediate"
duration: "5-7 weeks"
---

# Inferential Statistics

## Quick Start

Inferential statistics lets you make conclusions about populations based on samples. Within your first week, you'll understand p-values and hypothesis testing. By week five, you'll design experiments, interpret results, and make data-driven decisions with confidence.

**First Task (30 minutes):**
1. Formulate a null and alternative hypothesis
2. Run a t-test on two sample groups
3. Interpret the p-value and draw conclusions
4. Calculate a 95% confidence interval

## Key Concepts

### 1. Hypothesis Testing Framework
**What it is:** Statistical method to test claims about populations using sample data.

**Components:**
```
Null Hypothesis (H0): No effect, difference, or relationship exists
Alternative Hypothesis (H1): An effect, difference, or relationship exists

Example:
H0: New marketing campaign has NO effect on sales
H1: New marketing campaign DOES affect sales

Two-Tailed Test: Looking for any difference (≠)
One-Tailed Test (Right): Looking for increase (>)
One-Tailed Test (Left): Looking for decrease (<)
```

**Hypothesis Testing Steps:**
```
1. State hypotheses (H0 and H1)
2. Choose significance level (α, usually 0.05)
3. Select appropriate test
4. Calculate test statistic
5. Determine p-value
6. Make decision: Reject or fail to reject H0
7. Draw conclusion and communicate uncertainty
```

**Example:**
```
Scenario: Claim that average customer spending increased after new feature
H0: μ_before = μ_after (no change)
H1: μ_before ≠ μ_after (there is a change)
α = 0.05

Run paired t-test:
p-value = 0.032

Since p < 0.05: Reject H0
Conclusion: Evidence suggests spending changed (95% confidence)
```

### 2. P-Values & Significance
**What it is:** Probability of observing results as extreme as ours, assuming H0 is true.

**Interpretation:**
```
p-value = 0.001:
"If H0 were true, there's 0.1% chance of seeing this data"
→ Strong evidence against H0 (reject H0)

p-value = 0.05:
"If H0 were true, there's 5% chance of seeing this data"
→ Just at threshold (borderline)

p-value = 0.20:
"If H0 were true, there's 20% chance of seeing this data"
→ Weak evidence against H0 (fail to reject H0)

Common Significance Levels:
0.001: Very strong evidence needed
0.01: Strong evidence needed
0.05: Standard (80% of research uses this)
0.10: Lenient (mainly in exploratory analysis)
```

**Common Misinterpretation:**
```
WRONG: p-value = 0.03 means 97% chance H0 is false
RIGHT: p-value = 0.03 means if H0 true, 3% chance of this result

WRONG: p-value = 0.15 means 85% chance H1 is true
RIGHT: p-value = 0.15 means if H0 true, 15% chance of this result
```

### 3. Confidence Intervals
**What it is:** Range of values with specified probability containing true population parameter.

**Example (95% Confidence Interval):**
```
Sample mean: $2,500
Standard error: $100
95% CI: $2,500 ± 1.96×$100 = [$2,304, $2,696]

Interpretation:
"We're 95% confident the true population mean lies between $2,304-$2,696"

NOT: "95% probability the true mean is in this range"
     (It either is or isn't; probability is binary)

Instead: "If we repeated this sampling 100 times, ~95 intervals contain true mean"
```

**Relationship to hypothesis testing:**
```
95% CI for difference: [-10, 20]
Contains zero → Cannot reject H0 at 0.05 level

95% CI for difference: [5, 25]
Does NOT contain zero → Reject H0 at 0.05 level
```

### 4. Common Statistical Tests
**What it is:** Different tests for different data types and questions.

**Selection guide:**
```
Comparing 1 group to a value:
→ One-sample t-test

Comparing 2 independent groups:
→ Independent samples t-test (or Mann-Whitney if non-normal)

Comparing 2 related groups (before/after):
→ Paired t-test

Comparing 3+ groups:
→ ANOVA (Analysis of Variance)

Comparing categorical variables:
→ Chi-square test

Correlation between two continuous variables:
→ Pearson correlation (or Spearman if non-normal)
```

**T-Test Example (Python with scipy):**
```python
from scipy import stats
import numpy as np

# Before/after data
before = [2000, 2100, 1950, 2200, 2050]
after = [2300, 2400, 2100, 2500, 2200]

# Paired t-test
t_stat, p_value = stats.ttest_rel(before, after)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Spending significantly increased")
else:
    print("No significant difference detected")
```

### 5. ANOVA (Analysis of Variance)
**What it is:** Test for differences among 3+ group means.

**Example:**
```
Question: Do sales differ by region (North, South, East, West)?

H0: μ_North = μ_South = μ_East = μ_West
H1: At least one region differs

ANOVA Result:
F-statistic: 4.23
p-value: 0.012

Since p < 0.05: Reject H0
Conclusion: At least one region has significantly different sales

Follow-up: Post-hoc test (Tukey, Bonferroni) to identify which regions differ
```

**ANOVA Assumptions:**
```
1. Normality: Data in each group approximately normal
2. Homogeneity: Similar variance across groups
3. Independence: Observations independent

If violated: Use Kruskal-Wallis test (non-parametric alternative)
```

**Python Example:**
```python
from scipy import stats

north_sales = [5000, 5200, 4900, 5100]
south_sales = [6000, 6100, 5900, 6200]
east_sales = [4500, 4700, 4400, 4600]
west_sales = [5500, 5600, 5400, 5700]

f_stat, p_value = stats.f_oneway(north_sales, south_sales, east_sales, west_sales)
print(f"F-statistic: {f_stat:.4f}, p-value: {p_value:.4f}")
```

## Tools and Resources

**Python Libraries:**
- scipy.stats: All common statistical tests
- statsmodels: Advanced modeling and testing
- pingouin: Simplified statistical testing
- pandas: Data exploration

**Excel Functions:**
- T.TEST: t-test for two samples
- CHISQ.TEST: Chi-square test
- F.TEST: Test for variance equality
- CORREL: Correlation coefficient

**Online Calculators:**
- StatKey.io: Interactive hypothesis testing
- GraphPad QuickCalcs: One-sample, t-test, ANOVA
- Rosner Statistics Calculator

**Learning Resources:**
- Seeing Theory (Brown University): Interactive probability/statistics
- Coursera: Statistics with R (free)
- Khan Academy: Probability and statistics

## Best Practices

1. **Pre-Register Hypotheses:** Decide on tests before collecting data to avoid p-hacking
2. **Check Assumptions:** Verify normality, homogeneity before running tests
3. **Appropriate Sample Size:** Power analysis to determine needed sample size
4. **Report Effect Size:** p-value tells if difference exists; effect size tells if it matters
5. **Correct for Multiple Tests:** Bonferroni correction when running many tests
6. **Consider Practical Significance:** p < 0.05 doesn't mean the difference matters
7. **Communicate Uncertainty:** Always include confidence intervals with estimates
8. **Validate with Hold-Out Data:** Test conclusions on new data if possible

## Next Steps

1. **Week 1-2:** Understand hypothesis testing and p-values conceptually
2. **Week 2-3:** Master t-tests and confidence intervals
3. **Week 3-4:** Learn ANOVA and non-parametric alternatives
4. **Week 4-5:** Run hypothesis tests on real business problems
5. **Week 5-6:** Design experiments with proper power and sample size
6. **Week 6-7:** Communicate statistical findings to stakeholders
7. **After:** Move to Regression Analysis (predictive modeling)
8. **Progression:** Inferential → Regression → Advanced Statistical Modeling
