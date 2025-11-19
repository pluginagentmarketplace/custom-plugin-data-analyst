---
name: "Probability"
description: "Understand probability basics, distributions, Bayes theorem, and sampling methods for predictive analysis"
category: "Statistics"
level: "Intermediate"
duration: "4-5 weeks"
---

# Probability

## Quick Start

Probability is the foundation for all statistical inference. In your first week, you'll understand basic probability rules and calculate simple probabilities. By week three, you'll work with distributions and apply Bayes theorem to real business problems.

**First Task (25 minutes):**
1. Calculate simple probabilities (coin flips, dice rolls)
2. Understand conditional probability with a real scenario
3. Apply Bayes theorem to a classification problem
4. Identify which distribution fits your data

## Key Concepts

### 1. Probability Fundamentals
**What it is:** Measure of likelihood that an event occurs (0 to 1, or 0% to 100%).

**Basic Rules:**
```
Probability of an event:
P(A) = Number of favorable outcomes / Total possible outcomes

Example (fair coin):
P(heads) = 1 / 2 = 0.5

Complement Rule:
P(not A) = 1 - P(A)
P(not heads) = 1 - 0.5 = 0.5

Addition Rule (either A or B):
P(A or B) = P(A) + P(B) - P(A and B)
P(red or face card) = P(red) + P(face) - P(red face)
                    = 26/52 + 12/52 - 6/52 = 32/52

Multiplication Rule (both A and B):
P(A and B) = P(A) × P(B) [if independent]
P(two heads) = 0.5 × 0.5 = 0.25
```

**Conditional Probability:**
```
P(A | B) = Probability of A given B occurred
         = P(A and B) / P(B)

Example:
P(buy again | happy customer) = P(happy and buy) / P(happy)

If 60% of happy customers buy again, and 75% are happy:
P(buy | happy) = 0.60 / 0.75 = 0.80
```

### 2. Probability Distributions
**What it is:** Mathematical functions describing how values are distributed.

**Discrete Distributions (count data):**
```
Binomial Distribution:
- Fixed number of trials (n)
- Each trial has probability p of success
- Examples: coin flips, customer conversion rate

Formula: P(X = k) = C(n,k) × p^k × (1-p)^(n-k)

Example: 10 customers, 30% conversion rate
What's probability exactly 3 convert?
P(X=3) = C(10,3) × 0.3^3 × 0.7^7 = 0.267

Poisson Distribution:
- Events occurring at constant rate (λ)
- Examples: emails per hour, website visits per minute

Formula: P(X = k) = (e^-λ × λ^k) / k!

Example: 5 support tickets per hour on average
What's probability of 8 tickets in next hour?
P(X=8) = (e^-5 × 5^8) / 8! = 0.065
```

**Continuous Distributions:**
```
Normal Distribution (Bell Curve):
- Symmetric, continuous
- Defined by mean (μ) and std dev (σ)
- 68% within 1σ, 95% within 2σ

Standard Normal (Z-distribution):
- Mean = 0, Std Dev = 1
- Used to standardize any normal distribution
- Z = (X - μ) / σ

Example: IQ normally distributed, μ=100, σ=15
What % have IQ > 130?
Z = (130 - 100) / 15 = 2.0
P(Z > 2.0) ≈ 0.023 = 2.3%

Uniform Distribution:
- All values equally likely
- Examples: random number generator, uniform waiting time

Exponential Distribution:
- Time until next event (continuous version of Poisson)
- Examples: time to equipment failure, customer lifetime
```

### 3. Bayes Theorem
**What it is:** Method to update probabilities based on new evidence.

**Formula:**
```
P(A | B) = P(B | A) × P(A) / P(B)

Where:
P(A | B) = Posterior probability (what we want)
P(B | A) = Likelihood (probability of evidence given hypothesis)
P(A) = Prior probability (initial belief)
P(B) = Evidence probability (total probability of observing evidence)
```

**Business Example:**
```
Scenario: Email spam detection
Prior: 2% of emails are spam
Likelihood: Spam emails have "BUY NOW" 80% of time
Likelihood: Legitimate emails have "BUY NOW" 5% of time

An email contains "BUY NOW". What's probability it's spam?

P(spam | "BUY NOW") = P("BUY NOW" | spam) × P(spam) / P("BUY NOW")

P("BUY NOW") = P("BUY NOW"|spam)×P(spam) + P("BUY NOW"|legit)×P(legit)
             = 0.80 × 0.02 + 0.05 × 0.98
             = 0.016 + 0.049 = 0.065

P(spam | "BUY NOW") = 0.80 × 0.02 / 0.065 = 0.246 ≈ 25%

Interpretation: Seeing "BUY NOW" increases spam probability from 2% to 25%
```

**Medical Example:**
```
Disease prevalence: 1% of population
Test sensitivity (true positive rate): 95%
Test specificity (true negative rate): 90%

If test is positive, what's probability patient has disease?

P(disease | positive) = P(positive | disease) × P(disease) / P(positive)

P(positive) = 0.95 × 0.01 + 0.10 × 0.99 = 0.0095 + 0.099 = 0.1085

P(disease | positive) = 0.95 × 0.01 / 0.1085 = 0.0875 ≈ 8.75%

Even with positive test, only 8.75% probability of disease (due to low prevalence)
```

### 4. Sampling Methods
**What it is:** Techniques for selecting representative subset of population.

**Random Sampling:**
```
Simple Random Sampling:
- Each population member equally likely to be selected
- Most unbiased method
- Tools: random number generator, lottery method

Stratified Sampling:
- Divide population into strata (groups)
- Sample from each stratum proportionally
- Example: Sample 100 customers (40 from North, 30 from South, 30 from West)
- Ensures representation of each group

Cluster Sampling:
- Divide population into clusters
- Randomly select clusters, sample all within them
- More efficient for geographic data

Systematic Sampling:
- Select every nth item (e.g., every 10th customer)
- Easy to implement, watch for periodic patterns

Importance Sampling:
- Oversample underrepresented groups
- Useful for rare events (fraud detection, equipment failure)
```

**Sampling Distribution:**
```
Sample Mean Distribution:
- If sampling repeatedly, sample means follow normal distribution
- Standard Error (SE) = σ / √n
- Larger sample → smaller SE → more precise estimates

68% confidence interval for sample mean:
[Sample Mean - SE, Sample Mean + SE]

95% confidence interval:
[Sample Mean - 1.96×SE, Sample Mean + 1.96×SE]

Example:
Population SD = $1000
Sample size = 100
SE = $1000 / √100 = $100

95% CI = [mean - 196, mean + 196]
```

### 5. Expected Value & Decision Making
**What it is:** Average outcome considering probabilities and values.

**Formula:**
```
E(X) = Σ(probability × outcome)
```

**Business Decision Example:**
```
Marketing Campaign Decision:
Option A: Cost $10,000
  - 30% chance of $100,000 revenue
  - 70% chance of $0 revenue
  E(A) = 0.30 × $90,000 + 0.70 × (-$10,000) = $27,000 - $7,000 = $20,000

Option B: Cost $5,000
  - 60% chance of $30,000 revenue
  - 40% chance of $0 revenue
  E(B) = 0.60 × $25,000 + 0.40 × (-$5,000) = $15,000 - $2,000 = $13,000

Decision: Choose Option A (higher expected value)
```

## Tools and Resources

**Python Libraries:**
- scipy.stats: All probability distributions
- numpy: Random number generation
- pandas: Sampling utilities

**Statistical Tables:**
- Z-table: Standard normal probabilities
- t-table: t-distribution probabilities
- Chi-square table: Chi-square probabilities

**Online Tools:**
- StatKey.io: Interactive probability visualization
- Desmos: Distribution grapher
- Wolfram Alpha: Probability calculations

**Learning Resources:**
- "Introduction to Probability" by MIT OpenCourseWare
- 3Blue1Brown: YouTube Bayes theorem visual explanation
- StatQuest with Josh Starmer: YouTube probability tutorials

## Best Practices

1. **Understand Prior Probabilities:** Bayes theorem only works with proper priors
2. **Use Large Samples:** Sampling error decreases with larger samples
3. **Check Distribution Fit:** Don't assume normal; test your data
4. **Consider Conditional Dependencies:** Events often aren't independent
5. **Communicate Uncertainty:** Always discuss confidence/probability ranges
6. **Avoid Base Rate Fallacy:** Remember prior probability when interpreting results
7. **Account for Multiple Testing:** Adjust significance when running many tests
8. **Document Assumptions:** Probability calculations depend on stated assumptions

## Next Steps

1. **Week 1:** Master basic probability rules and conditional probability
2. **Week 2:** Learn major probability distributions and their applications
3. **Week 3:** Apply Bayes theorem to real business scenarios
4. **Week 4:** Understand sampling distributions and confidence intervals
5. **Week 5:** Use expected value for decision-making
6. **After:** Move to Inferential Statistics (hypothesis testing)
7. **Progression:** Probability → Inferential Statistics → Predictive Modeling
