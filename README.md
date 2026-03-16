# SaaS-Customer-Churn-Revenue-Analysis-SQL-Power-BI-Sheets-
This project analyzes a SaaS subscription dataset to understand customer churn, revenue trends, and overall business performance. 

SaaS Subscription Analysis (4-Year Review)

1. Overall Churn Rate & Monthly Trend

Overall churn rate:
52.2% of customers eventually churned

Average monthly churn rate:
4.52%
Trend (2022–2025)
Early months show high volatility due to smaller customer base.
Over time churn stabilizes around 3–5% monthly.
No strong long-term improvement trend.

Conclusion

⚠️ Churn is not clearly improving.
It stabilized but remains relatively high for SaaS, where healthy churn is typically <3% monthly.

2. Churn by Subscription Plan
Plan	Churn Rate
Starter	70.5%
Professional	47.9%
Business	41.3%
Enterprise	22.0%
Insights

Starter plan has the highest churn.
Likely reasons:
smaller companies
lower commitment
more price sensitivity
Enterprise customers are the most stable.
This is very typical in SaaS:
large companies = long contracts
higher switching costs

3. Billing Cycle Impact (Retention)
Billing Cycle	Churn Rate
Monthly	60.5%
Annual	40.3%
Insight

Annual billing significantly improves retention.
Customers paying monthly churn ~50% more often.
Business implication
Encourage:
annual contracts
discounts for yearly payment

4. Top 3 Churn Reasons
Rank	Reason	Customers
1	Budget Cuts	53
2	Price Too High	51
3	Company Closed	48
Insights

Two main categories appear:

Financial pressure
Budget cuts
Price sensitivity
Business failure
Company closure (common for startups / SMBs)

Implication:
product value may not justify price for smaller companies

5. Customer Lifetime Value (CLV)

CLV calculated as:
CLV = Average Monthly Revenue × Average Customer Lifespan

Plan	CLV
Starter	$1,755
Professional	$7,075
Business	$21,653
Enterprise	$66,589
6. Customer Acquisition Cost (CAC)

Average CAC:
$200

7. CLV : CAC Ratio
Plan	CLV	CAC	Ratio
Starter	$1,755	$200	8.8x
Professional	$7,075	$200	35x
Business	$21,653	$200	108x
Enterprise	$66,589	$200	332x
Insights
The most profitable segment is Enterprise.

Starter customers:
lowest revenue
highest churn
This segment likely creates support burden with low value.

8. High-Risk Customer Indicators

Based on the dataset fields:
Key predictors of churn likely include:
Low Feature Usage
Customers using <30% of features appear much more likely to churn.

This suggests:

👉 Poor onboarding
👉 Low product adoption

Low NPS
Customers with NPS < 6 correlate strongly with churn risk.
High Support Tickets
Many churned users also show:
high support ticket volume
possible product friction or complexity.

9. Estimated At-Risk Segment

A simple risk rule:
At-risk if:
Feature usage < 30%
NPS < 6
This segment should be monitored by Customer Success.

10. Key Business Recommendations

1. Push Annual Billing
Offer:
15–20% annual discount
This could reduce churn by ~20%.

2. Improve Starter Plan Onboarding
High churn suggests:
weak product adoption, poor onboarding

Recommended:
-Onboarding emails
-Tutorials
-Usage milestones

3. Focus Sales on Mid-Market and Enterprise
-Enterprise CLV is ~38× higher than Starter.
-Sales strategy should prioritize:
-Larger companies
-Long-term contracts

4. Create a Churn Prediction Model
Using:
-Feature usage
-NPS
-Support tickets
-Company size

Plan

Customer Success could proactively intervene.
