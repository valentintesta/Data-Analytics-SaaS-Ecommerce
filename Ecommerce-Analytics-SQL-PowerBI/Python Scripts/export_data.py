import mysql.connector
import pandas as pd
import os

# checking folder
os.makedirs("exported_data", exist_ok=True)

# Connecting to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root', 
    password='AlliJennaBrad94!!',
    database='ecommerce_analytics'
)

# Defining my base and derived tables I want to export
queries = {
    # Base tables
    "customers": "SELECT * FROM customers",
    "products": "SELECT * FROM products",
    "orders": "SELECT * FROM orders",
    "order_items": "SELECT * FROM order_items",
    "returns": "SELECT * FROM returns",

    # Derived/analysis result tables
    "total_revenue_by_category": "SELECT * FROM total_revenue_by_category",
    "top_customers_by_spend": "SELECT * FROM top_customers_by_spend",
    "return_rate_by_product": "SELECT * FROM return_rate_by_product",
    "customer_lifetime_value": "SELECT * FROM customer_lifetime_value",
    "monthly_revenue_trend": "SELECT * FROM monthly_revenue_trend",
    "top_returned_products": "SELECT * FROM top_returned_products",
    "return_rate_by_category": "SELECT * FROM return_rate_by_category"
}

# Exporting tables to CSV
for name, query in queries.items():
    try:
        df = pd.read_sql(query, conn)
        file_path = os.path.join("exported_data", f"{name}.csv")
        df.to_csv(file_path, index=False)
        print(f"✅ Exported: {name}.csv")
    except Exception as e:
        print(f"❌ Failed to export {name}: {e}")

conn.close()
print("📦 All exports complete.")
