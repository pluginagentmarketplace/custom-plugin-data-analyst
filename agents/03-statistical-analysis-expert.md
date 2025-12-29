---
name: 03-statistical-analysis-expert
description: Master statistical analysis, hypothesis testing, probability theory, and distributions to make data-driven decisions
model: sonnet
tools: All tools
sasmp_version: "1.3.0"
eqhm_enabled: true
---

# 03 - Statistics Specialist

## Overview

The Statistics Specialist role teaches you to look beyond raw numbers and understand what data truly reveals. While Foundations Specialists clean data and SQL Experts retrieve it, Statistics Specialists interpret data scientifically. This role equips you with the statistical rigor to support business decisions, validate hypotheses, and avoid common analytical mistakes that lead to false conclusions.

**Why This Matters**: Any analyst can calculate an average. Great analysts understand whether findings are statistically significant, whether observed differences are real or random chance, and can quantify confidence in recommendations. This expertise dramatically increases your value and credibility.

---

## Learning Path Overview

This learning journey transforms you from a descriptive analyst to an inferential scientist who can:
- Understand probability and statistical distributions
- Conduct rigorous hypothesis testing
- Design and analyze A/B experiments
- Build statistical models with confidence
- Communicate statistical findings to non-technical audiences
- Recognize when statistics are being misused

**Timeline**: 12-16 weeks of focused learning | **Skill Level**: Intermediate Data Scientist

---

## Learning Phase 1: Probability, Distributions & Descriptive Statistics

### Objectives
- Master probability fundamentals
- Understand major statistical distributions
- Learn to describe data statistically
- Recognize different data types and their properties
- Understand measures of central tendency and spread

### Core Topics

#### Probability Fundamentals
```
Basic Probability Concepts:

Probability = Number of favorable outcomes / Total possible outcomes

Coin flip: P(Heads) = 1/2 = 0.5
Die roll: P(3) = 1/6 ≈ 0.167
Card draw: P(King) = 4/52 ≈ 0.077

Key Rules:

Addition Rule (OR):
P(A or B) = P(A) + P(B) - P(A and B)
P(Customer buys OR refers) = P(buys) + P(refers) - P(buys AND refers)

Multiplication Rule (AND):
P(A and B) = P(A) × P(B|A)
P(2 heads in row) = 0.5 × 0.5 = 0.25

Conditional Probability:
P(A|B) = P(A and B) / P(B)
P(Customer buys | Saw ad) = P(buys AND saw ad) / P(saw ad)

Bayes' Theorem:
P(A|B) = P(B|A) × P(A) / P(B)
Used for: Medical testing, spam detection, diagnostic systems
```

#### Common Distributions
```
Distribution         When to Use                    Example
──────────────────────────────────────────────────────────────────
Normal             Continuous, symmetric          Heights, weights, test scores
(Gaussian)         data, many natural phenomena

Binomial           Count of successes in fixed    Clicks on 100 ad impressions
                   number of binary trials

Poisson            Count of events in time/space  Customer service calls per hour
                   interval, rare events

Exponential        Time until next event          Time between customer arrivals
                   (right-skewed)

Uniform            Equal probability in range     Random number generation
                   (rectangular)

Lognormal          Right-skewed, multiplicative   Income, stock prices, file sizes
                   processes

Chi-Square         Distribution of sum of         Goodness of fit tests
                   squared normal variables

t-distribution     Sample statistics when         Hypothesis testing with small
                   population sigma unknown       samples
```

#### Descriptive Statistics
```python
import numpy as np
from scipy import stats

# Sample data
data = [23, 25, 27, 29, 32, 34, 35, 38, 40, 45]

# Central Tendency
mean = np.mean(data)                    # Average
median = np.median(data)                # Middle value
mode = stats.mode(data)                 # Most frequent

# Spread/Dispersion
variance = np.var(data, ddof=1)         # Average squared deviation
std_dev = np.std(data, ddof=1)          # Square root of variance
range = np.max(data) - np.min(data)     # Max - Min
iqr = np.percentile(data, 75) - np.percentile(data, 25)  # Q3 - Q1

# Shape
skewness = stats.skew(data)             # Asymmetry (-: left, 0: symmetric, +: right)
kurtosis = stats.kurtosis(data)         # Tail heaviness

# Position
percentile_75 = np.percentile(data, 75)
z_score = (25 - mean) / std_dev         # Standard deviations from mean

# Correlation
correlation = np.corrcoef(data1, data2)[0, 1]  # -1 to 1
```

#### Data Types & Their Analysis
```
Data Type           Characteristics             Analysis Methods
────────────────────────────────────────────────────────────
Categorical         Distinct categories        - Mode
(Nominal)           No order (Red, Blue)        - Frequency tables
                                                - Chi-square tests

Ordinal             Categories with order      - Median, percentiles
                    (1st, 2nd, 3rd)            - Non-parametric tests
                    (Strongly Disagree-Agree)  - Spearman correlation

Continuous          Any value in range         - Mean, standard deviation
(Interval/Ratio)    (Temperatures, Income)     - Parametric tests
                    Ratio: has true zero       - Pearson correlation
                    Interval: no true zero     - Regression

Time Series         Observations over time     - Trend analysis
                    (Sequential, dependent)    - Seasonality detection
                                               - Autocorrelation
```

#### Visualizing Distributions
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram (distribution of continuous data)
plt.hist(data, bins=20, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Values')

# Box plot (quartiles and outliers)
plt.boxplot(data)
# Shows: min, Q1, median, Q3, max, outliers

# Q-Q plot (check normality)
stats.probplot(data, dist="norm", plot=plt)
# Points on diagonal = normally distributed

# Violin plot (distribution + density)
sns.violinplot(y=data)

# KDE plot (smooth density estimation)
sns.kdeplot(data=data, fill=True)
```

### Tools & Resources
- **Python Libraries**:
  - NumPy, SciPy, Pandas (numerical/statistical)
  - Matplotlib, Seaborn (visualization)
- **Excel**:
  - AVERAGE, STDEV, MEDIAN, PERCENTILE functions
  - Data Analysis ToolPak
- **Online Resources**:
  - Khan Academy Statistics (free, excellent)
  - StatQuest with Josh Starmer (YouTube)
  - DataCamp Statistics courses

### Key Deliverables
- [ ] Master probability calculations in 50+ scenarios
- [ ] Create distribution reference guide with examples
- [ ] Calculate mean, median, std dev for 10+ datasets
- [ ] Identify distribution type for 20+ datasets
- [ ] Build data profiling report (central tendency, spread, shape)

---

## Learning Phase 2: Hypothesis Testing & Statistical Inference

### Objectives
- Understand hypothesis testing framework
- Learn Type I and Type II errors
- Master common statistical tests
- Understand p-values and confidence intervals
- Apply hypothesis testing to business problems

### Core Topics

#### Hypothesis Testing Framework
```
The Scientific Method Applied to Data:

Step 1: Form Hypotheses
├── Null Hypothesis (H₀): Status quo, no effect
│   Example: μ = 100 (average is 100)
└── Alternative Hypothesis (H₁): Research claim
    Example: μ ≠ 100 (average is not 100)

Step 2: Choose Significance Level (α)
├── α = 0.05 (most common, 5% risk of false positive)
├── α = 0.01 (conservative, 1% risk)
└── α = 0.10 (lenient, 10% risk)

Step 3: Choose Appropriate Test
├── Based on data type and sample size
└── Calculate test statistic

Step 4: Calculate P-Value
├── Probability of observed result IF null hypothesis true
├── P < α: Reject null (finding is statistically significant)
└── P ≥ α: Fail to reject null (insufficient evidence)

Step 5: Interpret Results
├── Statistical significance ≠ practical significance
└── Consider context and effect size

Decision Matrix:
                    H₀ True     H₀ False
Reject H₀           Type I      ✓ Correct
                    Error       (Power)
Fail to Reject H₀   ✓ Correct   Type II
                                Error
```

#### Common Statistical Tests
```python
import scipy.stats as stats
import pandas as pd

# 1-Sample t-test
# Question: Is sample mean different from population mean?
# Data: 1 numerical variable, 1 sample
t_stat, p_value = stats.ttest_1samp(sample, popmean=100)
# Use when: Population std dev unknown, sample < 30

# 2-Sample t-test (Independent)
# Question: Are means of 2 groups different?
# Data: 1 numerical variable, 2 independent groups
t_stat, p_value = stats.ttest_ind(group1, group2)
# Example: Average salary of males vs females
# Assumption: Normal distribution, equal variances

# Paired t-test
# Question: Are means different for same group before/after?
# Data: 1 numerical variable, same subjects measured twice
t_stat, p_value = stats.ttest_rel(before, after)
# Example: Test scores before/after training

# Mann-Whitney U test (non-parametric alternative)
# Use when: Data not normally distributed or ordinal
u_stat, p_value = stats.mannwhitneyu(group1, group2)

# ANOVA (Analysis of Variance)
# Question: Are means different across 3+ groups?
f_stat, p_value = stats.f_oneway(group1, group2, group3)
# Example: Customer satisfaction across 5 regions

# Chi-Square Test
# Question: Are two categorical variables associated?
# Data: 2 categorical variables
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
# Example: Gender vs Product preference

# Correlation Tests
# Pearson correlation: Linear relationship, continuous data
r_coeff, p_value = stats.pearsonr(var1, var2)
# Spearman correlation: Monotonic relationship, ordinal data
r_coeff, p_value = stats.spearmanr(var1, var2)

# Normality Test (Shapiro-Wilk)
statistic, p_value = stats.shapiro(data)
# P > 0.05: Data appears normally distributed
```

#### P-Values, Confidence Intervals & Effect Size
```python
# Understanding P-Values
# P-value = Probability of observing this result if H₀ is true
#
# P = 0.03 means:
# "Only 3% probability of seeing this difference by random chance"
#
# Interpretation:
# P < 0.05: "Statistically significant" (reject H₀)
# P ≥ 0.05: "Not statistically significant" (fail to reject H₀)

# Confidence Interval
# 95% CI: Range we're 95% confident contains true population parameter
from scipy import stats

data = [45, 52, 48, 51, 49, 50]
mean = np.mean(data)
se = stats.sem(data)  # Standard error
ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=se)
# Result: [47.8, 51.2] - We're 95% confident true mean is in this range

# Effect Size (practical significance)
# How big is the difference? (Statistical significance ≠ practical)

# Cohen's d (standardized difference between means)
cohens_d = (mean1 - mean2) / np.std([group1, group2])
# Interpretation: 0.2 = small, 0.5 = medium, 0.8 = large

# R-squared (proportion of variance explained)
# Example: R² = 0.85 means variables explain 85% of variation

# Odds Ratio (for categorical data)
# Example: Treatment group 2x more likely to recover
```

#### Multiple Comparisons Problem
```
Scenario: Testing 20 different hypotheses at α = 0.05
Expected false positives: 20 × 0.05 = 1 ❌ BAD

Solution 1: Bonferroni Correction
Adjust α = 0.05 / 20 = 0.0025
Trade-off: More conservative, less likely to find real effects

Solution 2: False Discovery Rate (FDR)
Control proportion of false positives among significant findings
Less conservative than Bonferroni, better power

Solution 3: Planned Comparisons
Pre-specify comparisons before analyzing data
More powerful than post-hoc tests

Always:
✓ Pre-specify your hypotheses if possible
✓ Acknowledge multiple testing if post-hoc
✓ Use appropriate correction method
✗ Don't hide testing of multiple hypotheses
```

### Tools & Resources
- **Statistical Software**:
  - Python with SciPy, StatsModels
  - R (free, powerful for statistics)
  - Excel Data Analysis ToolPak
- **Learning Resources**:
  - "Statistical Rethinking" by Richard McElreath
  - "The Book of Why" by Judea Pearl
  - Khan Academy Statistics & Probability
  - Coursera Statistics specialization

### Key Deliverables
- [ ] Conduct 20+ hypothesis tests with real data
- [ ] Calculate and interpret confidence intervals (10+ datasets)
- [ ] Understand Type I/II errors with business examples
- [ ] Perform ANOVA and post-hoc tests
- [ ] Create hypothesis testing reference guide

---

## Learning Phase 3: A/B Testing & Experimental Design

### Objectives
- Master A/B testing methodology
- Understand experimental design principles
- Calculate sample size and power
- Detect and avoid common experimentation mistakes
- Analyze and communicate experiment results

### Core Topics

#### A/B Testing Fundamentals
```
A/B Testing Framework:

Step 1: Form Hypothesis
├── Control version (A): Current implementation
├── Treatment version (B): Proposed change
└── Metric to measure: Conversion rate, click-through, revenue

Step 2: Calculate Sample Size
├── Baseline conversion rate: 10%
├── Minimum detectable effect: 15% lift (1.5%)
├── Power: 80% (probability of detecting true effect)
├── Significance level: 5%
└── Sample size: Use online calculators or Python

Step 3: Run Experiment
├── Random assignment to A or B
├── Expose to both versions
├── Collect metrics over time
├── Monitor for data quality issues

Step 4: Analyze Results
├── Check statistical significance
├── Calculate confidence intervals
├── Consider practical significance
└── Report comprehensive findings

Step 5: Decide & Implement
├── Statistically significant + practically significant = implement
├── Statistically significant but small effect = decide by cost/benefit
├── Not statistically significant = don't implement
└── Document learnings
```

#### Sample Size Calculation
```python
from scipy.stats import norm

def calculate_sample_size(baseline_rate, lift, alpha=0.05, beta=0.20):
    """
    Calculate sample size needed per variant

    baseline_rate: Current conversion rate (0.10 = 10%)
    lift: Desired lift as decimal (0.15 = 15% lift)
    alpha: Significance level (0.05 = 5%)
    beta: Type II error rate (0.20 = 20%, power = 80%)
    """
    p1 = baseline_rate
    p2 = baseline_rate * (1 + lift)

    # Z-scores for 2-tailed test
    z_alpha = norm.ppf(1 - alpha/2)
    z_beta = norm.ppf(1 - beta)

    # Sample size formula
    pooled_p = (p1 + p2) / 2
    sample_size = (z_alpha + z_beta)**2 * (2 * pooled_p * (1 - pooled_p)) / (p2 - p1)**2

    return int(np.ceil(sample_size))

# Example
n = calculate_sample_size(baseline_rate=0.10, lift=0.15)
print(f"Need {n} users per variant")  # Output: ~2,100 per variant
```

#### Analyzing A/B Test Results
```python
import numpy as np
from scipy.stats import chi2_contingency, norm
from statsmodels.stats.proportion import proportions_ztest

# A/B Test Results
control_conversions = 45
control_total = 1000
treatment_conversions = 60
treatment_total = 1000

# Method 1: Proportion z-test
count = np.array([control_conversions, treatment_conversions])
nobs = np.array([control_total, treatment_total])
stat, pval = proportions_ztest(count, nobs)
print(f"P-value: {pval:.4f}")  # If < 0.05: statistically significant

# Method 2: Calculate confidence interval for lift
p1 = control_conversions / control_total
p2 = treatment_conversions / treatment_total
lift = (p2 - p1) / p1

# Standard error
se = np.sqrt((p1*(1-p1)/control_total) + (p2*(1-p2)/treatment_total))
z = norm.ppf(0.975)  # 95% CI
ci_lower = (p2 - p1) - z * se
ci_upper = (p2 - p1) + z * se

print(f"Baseline: {p1:.2%}")
print(f"Treatment: {p2:.2%}")
print(f"Lift: {lift:.2%}")
print(f"95% CI: [{ci_lower:.2%}, {ci_upper:.2%}]")

# Method 3: Chi-square test (alternative for categorical)
contingency = np.array([
    [control_conversions, control_total - control_conversions],
    [treatment_conversions, treatment_total - treatment_conversions]
])
chi2, p, dof, expected = chi2_contingency(contingency)
```

#### Common Experiment Mistakes
```
Mistake 1: Stopping Early
├── Problem: Increases false positive rate
├── Why: Multiple looks at data inflates Type I error
└── Solution: Pre-specify analysis plan, use sequential testing

Mistake 2: Multiple Comparisons
├── Problem: More metrics = higher chance of false positive
├── Why: Each metric has 5% false positive rate
└── Solution: Pre-specify primary metric, use correction if needed

Mistake 3: Novelty Effects
├── Problem: Users behave differently because of newness
├── Why: Initial excitement fades over time
└── Solution: Run experiment long enough (at least 1-2 weeks)

Mistake 4: Network Effects
├── Problem: Users influence each other's behavior
├── Why: Peer behavior affects decisions
└── Solution: Randomize at appropriate level (user, household, region)

Mistake 5: Peaking
├── Problem: Declaring winner before experiment ends
├── Why: Random fluctuations create false signals
└── Solution: Commit to sample size and full duration upfront

Mistake 6: Unequal Sample Sizes
├── Problem: Reduces statistical power
├── Why: Violates optimal allocation assumption
└── Solution: Maintain equal traffic split (unless using ratio tests)

Mistake 7: Survivorship Bias
├── Problem: Lost users skew results
├── Why: Worst performers drop out
└── Solution: Analyze intent-to-treat (all who started)

Mistake 8: Cannibalization
├── Problem: Treatment affects other metrics negatively
├── Why: Users switch from existing products
└── Solution: Monitor full funnel and cannibalization metrics
```

#### Experimental Design Considerations
```
Design Choice                   When to Use              Example
─────────────────────────────────────────────────────────────────
Completely Randomized           Independent units       Website redesign
                                                        (random users)

Randomized Block Design         Account for variation   E-commerce by region
                                across blocks

Matched Pairs                   Dependent units         Before/after within
                                                        same user

Factorial Design                Multiple factors        2 new features tested
                                                        simultaneously

Sequential Testing              Want to stop early      Medical trials,
                                with flexibility        urgent decisions

Clustered Randomization         Natural grouping        School/classroom
                                                        interventions
```

### Tools & Resources
- **A/B Testing Platforms**:
  - Optimizely, VWO, Convert (commercial)
  - PlanOut (open source, Facebook)
  - Statsmodels (Python)
- **Sample Size Calculators**:
  - Evan Miller's calculator (online)
  - Optimizely sample size calculator
  - Python: statsmodels.stats.proportion
- **Learning Resources**:
  - "Trustworthy Online Controlled Experiments" by Kohavi, Tang, Xu
  - Udacity A/B Testing course
  - Reforge A/B Testing course

### Key Deliverables
- [ ] Design 10+ A/B experiments with proper hypotheses
- [ ] Calculate sample sizes for 15+ scenarios
- [ ] Analyze 20+ simulated experiment results
- [ ] Create A/B testing checklist and best practices
- [ ] Document lessons learned from experiments

---

## Real-World Projects

### Project 1: Customer Conversion Analysis
**Scenario**: Analyze factors affecting customer conversion from trial to paid.

**Objectives**:
- Identify key conversion drivers through statistical analysis
- Test hypotheses about user behavior
- Calculate confidence intervals for conversion rates by segment
- Build logistic regression model for conversion prediction

**Deliverables**:
- Statistical analysis report (means, distributions, correlations)
- Hypothesis test results (5+ tests with p-values)
- Conversion rate by segment with confidence intervals
- Logistic regression model with interpretation
- Actionable recommendations

**Skills Applied**: Descriptive statistics, hypothesis testing, segmentation, statistical modeling

---

### Project 2: A/B Testing Campaign
**Scenario**: Design and analyze A/B test for website redesign.

**Objectives**:
- Design experiment with proper hypothesis
- Calculate sample size for 20% lift detection
- Run experiment and collect data
- Analyze results with significance tests
- Present findings to stakeholders

**Deliverables**:
- Experiment design document with hypothesis
- Sample size calculation and justification
- Complete results dashboard
- Statistical analysis (p-values, confidence intervals, effect size)
- Executive summary with recommendation

**Skills Applied**: Experimental design, sample size calculation, statistical testing, communication

---

### Project 3: Statistical Quality Control
**Scenario**: Implement statistical monitoring for data quality and business metrics.

**Objectives**:
- Establish baseline for key metrics
- Create control limits (statistical monitoring)
- Detect anomalies/out-of-control conditions
- Document root cause analysis process
- Implement automated monitoring

**Deliverables**:
- Control charts for 10+ key metrics
- Baseline statistics and control limits
- Anomaly detection rules
- Root cause analysis documentation
- Monitoring dashboard with alerts

**Skills Applied**: Control charts, statistical monitoring, process improvement, quality assurance

---

## Career Progression

### Timeline & Advancement
```
Months 1-2:     Basic Competency
├── Understand probability and distributions
├── Conduct simple hypothesis tests
├── Calculate basic statistics
└── Understand p-values conceptually

Months 3-4:     Intermediate Competency
├── Master multiple statistical tests
├── Design simple experiments
├── Calculate and interpret confidence intervals
├── Understand effect sizes

Months 5-8:     Advanced Competency
├── Design complex experiments
├── Avoid common statistical mistakes
├── Build statistical models
├── Mentor others on statistical thinking
└── Lead experimentation program

Months 9-12:    Expert Competency
├── Architect statistical frameworks
├── Lead statistical transformation
├── Present complex analyses to executives
├── Ready for data science roles
└── Publish statistical insights
```

### Role Opportunities
- **Analytics Specialist** (Statistics-focused)
- **Experimentation Analyst** (A/B testing-focused)
- **Data Scientist** (Broader statistics + ML)
- **Research Analyst** (Academic/research focus)
- **Quality Assurance Analyst** (SQC-focused)

### Salary Expectations (2024 US Market)
```
Entry Level (0-2 years):        $65,000 - $85,000
Mid Level (2-5 years):          $85,000 - $120,000
Advanced (5+ years):            $120,000 - $160,000
Senior/Lead (8+ years):         $160,000 - $220,000+
```

---

## Best Practices

### 1. Hypothesis Formation
```
Good Hypothesis:
✓ Specific and measurable
✓ Directional (A > B, not A ≠ B) when possible
✓ Based on existing data or theory
✓ Challenges current assumption

Bad Hypothesis:
✗ Vague ("improve engagement")
✗ Contradicts strong evidence
✗ Unfalsifiable ("something will change")
✗ Post-hoc (formed after seeing data)

Example:
Good: "Simplifying checkout process will increase conversion by 10%"
Bad: "Change checkout process" or "Conversion will change"
```

### 2. Statistical Thinking
```
Common Mistakes:
✗ Ignoring regression to the mean
  (Extreme values tend to normalize)
✗ Confusing correlation with causation
  (A and B related, but B might cause A)
✗ Over-interpreting noisy data
  (Random variation appears meaningful)
✗ P-hacking (testing until significance)
  (Increases false positive rate)
✗ Misinterpreting p-values
  (Not probability hypothesis is true)

Always:
✓ Check assumptions of statistical tests
✓ Look at effect size, not just p-value
✓ Consider practical significance
✓ Be skeptical of surprising results
✓ Validate findings with new data
```

### 3. Data Quality for Analysis
```
Before Statistical Analysis:

1. Check for missing data
   - Amount of missingness
   - Pattern of missingness (random or systematic?)
   - Handle appropriately (remove, impute, or exclude)

2. Identify outliers
   - Use box plot, IQR, or z-score
   - Investigate if real or data error
   - Handle: Remove, transform, or analyze separately

3. Verify assumptions
   - Normality (Shapiro-Wilk test)
   - Homogeneity of variance (Levene's test)
   - Independence of observations
   - Linearity (for correlation/regression)

4. Check distribution
   - Histogram or density plot
   - Consider transformation if non-normal
   - Choose appropriate statistical test

5. Document decisions
   - Record how you handled missing data
   - Document outlier decisions
   - Note any transformations applied
```

### 4. Communicating Statistical Results
```
Executive Summary Template:

1. Question Asked
   "Does the new checkout process improve conversion?"

2. Data & Methodology
   - Sample: 10,000 users per variant
   - Duration: 2 weeks (Jan 15-29)
   - Metric: Purchase conversion rate

3. Key Results
   - Control: 12.4% conversion
   - Treatment: 14.1% conversion
   - Lift: +1.7 percentage points (+13.7%)
   - P-value: 0.003 (statistically significant)
   - 95% CI: [+0.8%, +2.6%]

4. Conclusion
   - Statistical finding: Significant evidence of improvement
   - Practical finding: +13.7% lift translates to X additional revenue
   - Recommendation: Implement for all users

5. Caveats
   - Note any limitations
   - Discuss what wasn't tested
   - Suggest follow-up analyses

Don't use jargon without explaining.
Focus on business impact, not statistical details.
```

### 5. Choosing the Right Test
```
Decision Tree:

Question: Comparing groups?
├─ No → Correlation/regression
├─ Yes: 2 groups or 3+?
    ├─ 2 groups:
    │   ├─ Paired observations? (before-after, matched)
    │   │   └─ Parametric (normal) → Paired t-test
    │   │       Non-parametric → Wilcoxon signed-rank
    │   └─ Independent observations?
    │       └─ Parametric → Independent t-test
    │           Non-parametric → Mann-Whitney U
    └─ 3+ groups:
        ├─ Parametric → ANOVA
        └─ Non-parametric → Kruskal-Wallis

Question: Comparing proportions?
├─ 2 proportions → Proportion z-test or Chi-square
└─ 3+ proportions → Chi-square test of independence
```

---

## Best Tools & Resources

### Software
- **Python**:
  - SciPy (statistical tests)
  - StatsModels (regression, ANOVA)
  - Pandas (data manipulation)
  - Matplotlib/Seaborn (visualization)
- **R**: Superior statistics, many packages
- **Excel**: Basic tests via Data Analysis ToolPak
- **Online Tools**: Evan Miller's calculators

### Learning Resources
- **Books**:
  - "Statistical Rethinking" - Richard McElreath (Bayesian)
  - "The Book of Why" - Judea Pearl (causality)
  - "Thinking, Fast and Slow" - Daniel Kahneman (bias)
- **Online Courses**:
  - Coursera Statistics specialization
  - DataCamp Statistics and A/B Testing
  - MIT OpenCourseWare Statistics
  - Khan Academy (free, excellent)
- **Websites**:
  - Evan Miller statistics blog
  - Andrew Gelman's blog (statistics philosophy)
  - CrossValidated (Q&A site)

---

## Next Steps

### Immediate Actions (Next 2 Weeks)
1. **Master fundamentals**
   - Complete Khan Academy probability module
   - Learn normal distribution deeply
   - Practice calculating means, standard deviations

2. **Run first tests**
   - Set up Python/R environment
   - Conduct t-tests on sample data
   - Interpret results properly

3. **Build reference materials**
   - Create formula sheet
   - Document when to use each test
   - Build checklist for analyses

### Short-term Goals (1-3 Months)
1. **Deepen statistical knowledge**
   - Complete hypothesis testing module
   - Master ANOVA and regression
   - Understand confidence intervals deeply

2. **Design first experiment**
   - Identify experiment opportunity
   - Calculate proper sample size
   - Run experiment with control plan

3. **Avoid common mistakes**
   - Study A/B testing gotchas
   - Understand regression to the mean
   - Learn about data quality issues

### Advanced Preparation (3-6 Months)
1. **Prepare for advanced roles**
   - Deep dive into predictive modeling
   - Learn Bayesian statistics
   - Understand causal inference

2. **Lead statistical initiatives**
   - Design company-wide A/B testing program
   - Establish statistical standards
   - Mentor others on statistical rigor

### Recommended Learning Sequence
```
Current Role: Statistics Specialist ✓ (You are here)
        ↓
Option A: Deepen statistical expertise
        ↓
Option B: Move to Phase 4 - Visualization Architect
        ↓
Option C: Move to Phase 5 - Programming Expert
        ↓
Multiple Advanced Roles (4, 5, 6)
        ↓
Career Leadership Roles (7 - Career Coach)
```

---

## Key Takeaways

As a Statistics Specialist, you'll understand that:

1. **Statistical significance ≠ Practical significance** - Some differences are real but too small to matter
2. **Correlation ≠ Causation** - Associated variables may not have causal relationships
3. **Sample size matters enormously** - Too small and you can't detect real effects; too large and tiny effects seem important
4. **P-values are easily misinterpreted** - They're probability of data given null hypothesis, not probability hypothesis is true
5. **Assumptions are critical** - Statistical tests fail when assumptions violated
6. **Randomization beats intuition** - Randomized experiments prevent bias better than careful selection

Statistical rigor separates casual analysts from credible experts. Build this foundation well.

---

## FAQ

**Q: What's the difference between α = 0.05 and p-value = 0.05?**
A: α is your decision threshold (chosen before analysis). p-value is your calculated result (from data). If p < α, you reject null hypothesis.

**Q: Does p = 0.05 mean there's 5% chance my hypothesis is wrong?**
A: No. P-value is probability of data given null hypothesis is true, not probability hypothesis is wrong.

**Q: Can I use parametric tests if data isn't normal?**
A: Often yes. Central Limit Theorem makes t-tests robust with large samples. But check assumptions and consider non-parametric alternatives.

**Q: How many samples do I need?**
A: Depends on effect size, acceptable error rates, and variability. Use power analysis calculators. Generally 200-1000+ per variant for experiments.

**Q: Should I always use 95% confidence? Can I use 90%?**
A: Yes, if justified. 95% is convention. 99% for critical decisions. 90% acceptable if you explain why.

---

**Last Updated**: November 2024
**Difficulty Level**: Intermediate
**Estimated Time to Completion**: 12-16 weeks
