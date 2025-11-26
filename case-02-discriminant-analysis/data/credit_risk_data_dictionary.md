# Credit Risk Data Dictionary

## LendSmart Financial Services - Loan Default Prediction Dataset

**File**: `credit_risk_data.csv`  
**Observations**: 10,000+ loan records  
**Target Variable**: loan_status (0=Good, 1=Default)  
**Time Period**: Historical portfolio data  
**Data Type**: Loan applications with payment outcomes  

---

## Variable Descriptions

### Identification Variables

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `application_id` | String | Unique loan application identifier | APP_001001 |
| `application_date` | Date | Date of loan application | 2022-01-15 |

### Financial Characteristics (7 variables)

#### Credit & Payment Indicators

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `credit_score` | Numeric | 300-850 | FICO credit score; higher=lower risk |
| `payment_history_score` | Numeric | 0-100 | Score based on on-time payment history |
| `credit_utilization` | Numeric | 0-100 | Percentage of available credit currently used |

#### Income & Debt Indicators

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `annual_income` | Numeric | $20K-$500K+ | Gross annual household income |
| `debt_to_income_ratio` | Numeric | 0.0-1.0 | Total monthly debt / monthly gross income |
| `asset_value` | Numeric | $0-$10M+ | Total reported assets (savings, investments, property) |

#### Loan Characteristics

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `loan_amount` | Numeric | $1K-$500K | Amount of loan requested/approved |

### Demographic Characteristics (4 variables)

#### Education & Marital Status

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `education_level` | Categorical | High School, Bachelor, Master, PhD | Highest level of education completed |
| `marital_status` | Categorical | Single, Married, Divorced, Widowed | Current marital status |

#### Employment Status

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `employment_status` | Categorical | Employed, Self-Employed, Unemployed, Retired | Current employment classification |

#### Age

| Variable | Type | Range | Description |
|----------|------|-------|-------------|
| `age_group` | Categorical | 18-25, 26-35, 36-45, 46-55, 56-65, 65+ | Applicant age group |

### Target Variable

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `loan_status` | Binary | 0, 1 | 0 = Good (loan paid successfully), 1 = Default (payment failure) |

---

## Data Quality Notes

### Missing Values Treatment

| Variable | Handling |
|----------|----------|
| Numeric variables | Filled with median of class |
| Categorical variables | Filled with mode of class |
| Identification (id, date) | Dropped before modeling |

### Encoding Strategy

- **Categorical Variables**: One-hot encoded with `drop_first=True` to avoid multicollinearity
- **Numeric Variables**: Standardized (Z-score) for fair contribution to discriminant functions

### Class Distribution

Expected approximately:
- **Class 0 (Good)**: 75-85% of sample
- **Class 1 (Default)**: 15-25% of sample

Imbalance addressed via stratified train/test split to maintain class proportions.

---

## Analytical Notes for Discriminant Analysis

### Why These Features?

1. **credit_score**: Most predictive; inversely related to default risk
2. **payment_history_score**: Captures behavioral pattern
3. **debt_to_income_ratio**: Capacity indicator; higher ratio = higher risk
4. **annual_income**: Ability to repay
5. **asset_value**: Collateral/cushion for financial stress
6. **loan_amount**: Risk exposure
7. **education_level, marital_status**: Demographic correlates of financial responsibility
8. **employment_status, age_group**: Stability indicators

### LDA Assumptions

1. **Multivariate Normality**: Features within each class (Good/Default) approximately normally distributed
2. **Homogeneity of Covariance**: Covariance matrices similar across classes
3. **Linear Decision Boundary**: Optimal if above assumptions hold

### QDA Advantages

- Relaxes homogeneity assumption; allows class-specific covariances
- Better captures non-linear patterns if distributions differ between classes
- May overfit if sample size small relative to feature count (not an issue here with n=10,000)

---

## References & Business Context

- **Regulatory Background**: Models must comply with Fair Lending Act and FCRA
- **Fair Lending Considerations**: Protected classes (race, gender, national origin) not included; focus on financial indicators
- **Threshold Tuning**: Classification threshold can be adjusted to balance precision (false positives) vs recall (false negatives) based on business costs
