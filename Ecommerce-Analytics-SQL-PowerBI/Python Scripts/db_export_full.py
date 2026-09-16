import mysql.connector
import pandas as pd
import os

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='AlliJennaBrad94!!',
    database='ecommerce_analytics'
)

base_tables = [
    "customers",
    "products",
    "orders",
    "order_items",
    "returns"
]

# Creating the Excel from tables
output_path = "exported_data/ecommerce_database.xlsx"
os.makedirs("exported_data", exist_ok=True)

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    for table in base_tables:
        try:
            df = pd.read_sql(f"SELECT * FROM {table}", conn)
            df.to_excel(writer, sheet_name=table, index=False)
            print(f"✅ Wrote {table} to Excel.")
        except Exception as e:
            print(f"❌ Failed on {table}: {e}")

conn.close()
print(f"📦 Excel file saved: {output_path}")
