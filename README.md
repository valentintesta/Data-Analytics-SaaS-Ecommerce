# SaaS Subscription Analysis (4-Year Review)

## 📊 Project Overview

This project analyzes **4 years of SaaS subscription data** to identify churn patterns, customer behavior, and key business insights.

The analysis focuses on:

- Customer churn trends
- Subscription plan performance
- Billing cycle impact
- Customer Lifetime Value (CLV)
- Customer Acquisition Cost (CAC)
- Churn drivers and risk indicators
- Strategic business recommendations

---

# 1. Overall Churn Rate & Monthly Trend

### Overall churn rate
- **52.2%** of customers eventually churned

### Average monthly churn rate
- **4.52%**

### Trend (2022–2025)

- Early months show **high volatility** due to a smaller customer base.
- Over time, churn stabilizes around **3–5% monthly**.
- No strong long-term improvement trend.

### Conclusion

⚠️ **Churn is not clearly improving.**

It has stabilized but remains relatively high for SaaS companies, where **healthy churn is typically < 3% per month.**

---

# 2. Churn by Subscription Plan

| Plan | Churn Rate |
|-----|-----------|
| Starter | 70.5% |
| Professional | 47.9% |
| Business | 41.3% |
| Enterprise | 22.0% |

### Insights

- **Starter plan has the highest churn rate.**

Possible reasons:

- Smaller companies
- Lower commitment
- Higher price sensitivity

- **Enterprise customers are the most stable.**

This is typical in SaaS:

- Large companies → long contracts  
- Higher switching costs

---

# 3. Billing Cycle Impact (Retention)

| Billing Cycle | Churn Rate |
|--------------|-----------|
| Monthly | 60.5% |
| Annual | 40.3% |

### Insight

Annual billing **significantly improves retention**.

Customers paying **monthly churn ~50% more often**.

### Business Implication

Encourage:

- **Annual contracts**
- **Discounts for yearly payments**

---

# 4. Top 3 Churn Reasons

| Rank | Reason | Customers |
|-----|------|----------|
| 1 | Budget Cuts | 53 |
| 2 | Price Too High | 51 |
| 3 | Company Closed | 48 |

### Insights

Two main churn categories appear:

**1️⃣ Financial Pressure**

- Budget cuts  
- Price sensitivity  

**2️⃣ Business Failure**

- Company closure (common for startups / SMBs)

### Implication

Product value **may not justify the price for smaller companies.**

---

# 5. Customer Lifetime Value (CLV)

CLV calculated as:

```
CLV = Average Monthly Revenue × Average Customer Lifespan
```

| Plan | CLV |
|-----|------|
| Starter | $1,755 |
| Professional | $7,075 |
| Business | $21,653 |
| Enterprise | $66,589 |

---

# 6. Customer Acquisition Cost (CAC)

Average CAC:

```
$200
```

---

# 7. CLV : CAC Ratio

| Plan | CLV | CAC | Ratio |
|-----|-----|-----|------|
| Starter | $1,755 | $200 | 8.8x |
| Professional | $7,075 | $200 | 35x |
| Business | $21,653 | $200 | 108x |
| Enterprise | $66,589 | $200 | 332x |

### Insights

- The **most profitable segment is Enterprise**.
- Starter customers generate:

  - Lowest revenue
  - Highest churn

This segment likely creates **high support cost with low business value.**

---

# 8. High-Risk Customer Indicators

Based on the dataset fields, key predictors of churn include:

### 📉 Low Feature Usage

Customers using **< 30% of features** are significantly more likely to churn.

Possible causes:

- Poor onboarding
- Low product adoption

---

### ⭐ Low NPS

Customers with **NPS < 6** strongly correlate with **churn risk**.

---

### 🎫 High Support Tickets

Many churned users show:

- High support ticket volume
- Possible product friction or complexity

---

# 9. Estimated At-Risk Segment

A simple churn risk rule:

```
At-risk if:

Feature Usage < 30%
AND
NPS < 6
```

This segment should be monitored by the **Customer Success team**.

---

# 10. Key Business Recommendations

## 1️⃣ Push Annual Billing

Offer:

- **15–20% annual discount**

This could potentially **reduce churn by ~20%.**

---

## 2️⃣ Improve Starter Plan Onboarding

High churn suggests:

- Weak product adoption
- Poor onboarding

Recommended actions:

- Onboarding email sequences
- Product tutorials
- Usage milestones

---

## 3️⃣ Focus Sales on Mid-Market and Enterprise

Enterprise CLV is **~38× higher** than Starter.

Sales strategy should prioritize:

- Larger companies
- Long-term contracts

---

## 4️⃣ Build a Churn Prediction Model

Using variables such as:

- Feature usage
- NPS
- Support tickets
- Company size
- Subscription plan

This would allow **Customer Success teams to proactively intervene before churn occurs.**

---

# 📌 Tools Used

- SQL (data cleaning & analysis)
- Power BI / Visualization
- Excel / Data preparation

---

# 🚀 Portfolio Project

This project demonstrates practical skills in:

- SaaS metrics analysis
- Churn analysis
- CLV & CAC evaluation
- Business insight generation
- Data storytelling for decision making
