# E-Commerce Analytics Project: SQL, Python, and Power BI

This project walks through a full analytics workflow for a fictional e-commerce company from database creation and data generation to SQL (MySQL) analysis and Power BI report design. The goal was to uncover patterns in customer behavior, purchase trends, and product returns, all using simulated data that mimics real-world operations.

## Business Goal

**How can this (fake) e-commerce company increase revenue, reduce product returns, and improve customer retention?**

Everything in this project was built to help me answer that question.

## Project Overview

This started as a Python + MySQL project where I built a normalized database and filled it with synthetic data using the `Faker` library. I explored the data using SQL and exported the cleaned version into Excel. From there, I used Power BI to create a report that highlights key metrics like total revenue, return rates, and customer lifetime value.

### Key Tools Used

- MySQL: database schema and SQL analysis
- Python: data generation and export
- Power BI Desktop: report building and visualization
- Git/GitHub: version control and portfolio hosting

## Database Schema

```
customers      — customer_id, first_name, last_name, email, signup_date  
products       — product_id, product_name, category, price  
orders         — order_id, customer_id, order_date, total_amount  
order_items    — order_item_id, order_id, product_id, quantity, item_price  
returns        — return_id, order_item_id, return_date, reason  
```

## Folder Structure

```
ecommerce_sql_project/
│
├── generate_data.py          
├── export_data.py            
├── export_to_excel.py        
│
├── exported_data/
│   ├── ecommerce_database.xlsx     
│   ├── original_tables/            
│   └── derived_tables/             
│
├── SQL_Scripts/
│   ├── ecommerceDB_setup.sql           
│   ├── ecommerce_data_exploration.sql  
│   └── derived_tables.sql              
│
└── README.md
```

## Power BI Report Overview

This report brings together several key business questions in one visual package. Since the report is shared as a static PDF/PNG for portfolio purposes, each page was designed to tell a clear story without slicers or interactivity.

### Main Dashboard

High-level summary including:

- Total Revenue: $5.28K  
- Return Rate: 39.47%  
- Average Order Value: $108.86  
- Top Revenue Categories: Electronics led overall  
- Customer Tiers: Balanced distribution across High, Mid, and Low  
- Monthly Revenue Trends: January was highest, February the lowest  

*Note: Data spans Oct 2022–Oct 2024 (simulated), limiting long-term trend analysis.*

### Returns Deep Dive

- Top Returned Products: Noise-Cancelling Headphones, Board Games  
- Common Return Reasons: Late deliveries, damaged items  
- Return Volume: Spikes in January and July  
- Return Rate vs Product Revenue: Flags problematic products  

### Product Insights

- Price vs Quantity: Cheaper categories (Books, Toys) move quickly  
- Category Revenue Distribution: Fairly even overall  
- Outlier Detection: Return-heavy products highlighted  

### Customer Segmentation

- Top Customers by CLV: A few contribute most of the revenue  
- CLV Tiers: 70% high-value customers with low return rates  
- Units Sold by Persona: High-value buyers drive more purchases  

## Custom DAX Measures

```DAX
Customer Lifetime Value = 
CALCULATE(
    SUM(orders[total_amount]), 
    FILTER(orders, orders[customer_id] = MAX(customers[customer_id]))
)

Total Revenue = 
SUMX(order_items, order_items[quantity] * order_items[item_price])

Return Rate (%) = 
DIVIDE(COUNT(returns[return_id]), COUNT(order_items[order_item_id]))

Average Order Value = 
AVERAGEX(orders, orders[total_amount])

Revenue Tier = 
SWITCH(
    TRUE(),
    [Customer Lifetime Value] >= 1000, "High Value",
    [Customer Lifetime Value] >= 500, "Mid Value",
    [Customer Lifetime Value] >= 0, "Low Value",
    "Unknown"
)
```

## Challenges and What I Learned

### Working with Simulated Data

- Return rates were unrealistically high (~40%)
- Every customer was "active," which meant no churn modeling
- Limited timeline made trend analysis trickier
- Had to limit data size due to working on an older computer

**Lesson:** Simulated data is helpful, but I needed to clearly explain its limits and design visuals around that.

### Power BI Visual Design

- Some visual types didn’t make sense with small or skewed data—bubble charts and scatter plots didn’t work well
- Navigation buttons were hard to get working but worth it for polish

**Lesson:** Prioritize clarity and layout. Even with weird data, clean visuals can still tell a strong story.

### Designing for Static Output

Since I’m not publishing an interactive Power BI dashboard online, I had to:
- Ensure every page stood alone with its own context
- Repeat key metrics for consistency
- Use clean titles and visual order to guide readers

**Lesson:** Storytelling with data works even in a static format—it just takes more intentional design.

## Sample Insights

- Around 40% of customers fell into the High Value Tier  
- Electronics drove the most revenue  
- A small handful of customers accounted for most CLV  
- Returns were most often caused by late deliveries or wrong items

## How to Reproduce

1. Clone this repo  
2. Run `generate_data.py` to populate your MySQL database  
3. Run `export_data.py` to save CSV or Excel outputs  
4. Open `ecommerce_database.xlsx` in Power BI Desktop  
5. Clean the data, set relationships, and build visuals as shown

## Final Notes

This project helped me practice full-cycle analytics: from simulating and structuring data to building SQL queries and visualizing insights in Power BI. The static report is available on my [portfolio site](https://ahutson881.github.io/allisonh-portfolio/#), and the full `.pbix` file is available upon request.

**Author:** Allison Hutson  
**Role:** Customer Insights & Product Research Strategist
