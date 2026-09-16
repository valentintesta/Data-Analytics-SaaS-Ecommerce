import mysql.connector
from faker import Faker
import random
import logging

# --------------------------------
# Config
# --------------------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'AlliJennaBrad94!!',
    'database': 'ecommerce_analytics'
}

CUSTOMER_COUNT = 250
ORDER_COUNT = 1000
RETURN_RATE = 0.1  # 10% of order items

# --------------------------------
# Logging Setup
# --------------------------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
fake = Faker()

# --------------------------------
# Connecting to MySQL
# --------------------------------
try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    logging.info("Connected to MySQL database.")
except mysql.connector.Error as err:
    logging.error(f"Failed to connect: {err}")
    exit(1)

# --------------------------------
# Product List
# --------------------------------
product_list = [
    ("Wireless Mouse", "Electronics", 25.00),
    ("Mechanical Keyboard", "Electronics", 75.00),
    ("Standing Desk", "Furniture", 250.00),
    ("Office Chair", "Furniture", 150.00),
    ("Notebook Set", "Stationery", 10.00),
    ("Pen Pack", "Stationery", 5.00),
    ("Noise Cancelling Headphones", "Electronics", 200.00),
    ("Monitor Arm", "Furniture", 90.00),
    ("USB-C Hub", "Electronics", 40.00),
    ("Planner", "Stationery", 12.00)
]

# --------------------------------
# Inserting Products
# --------------------------------
def insert_products():
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        for name, category, price in product_list:
            cursor.execute(
                "INSERT INTO products (product_name, category, price) VALUES (%s, %s, %s)",
                (name, category, price)
            )
        conn.commit()
        logging.info(f"Inserted {len(product_list)} products.")

# --------------------------------
# Inserting Customers
# --------------------------------
def insert_customers(n):
    for _ in range(n):
        first = fake.first_name()
        last = fake.last_name()
        email = fake.email()
        signup = fake.date_between(start_date='-2y', end_date='today')
        cursor.execute(
            "INSERT INTO customers (first_name, last_name, email, signup_date) VALUES (%s, %s, %s, %s)",
            (first, last, email, signup)
        )
    conn.commit()
    logging.info(f"Inserted {n} customers.")

# --------------------------------
# Inserting Orders & Order Itemss
# --------------------------------
def insert_orders_and_items(n_orders):
    cursor.execute("SELECT customer_id FROM customers")
    customers = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT product_id, price FROM products")
    products = cursor.fetchall()

    for _ in range(n_orders):
        customer_id = random.choice(customers)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        items = random.randint(1, 4)
        total = 0.0
        item_data = []

        for _ in range(items):
            product_id, price = random.choice(products)
            qty = random.randint(1, 3)
            total += float(qty * price)
            item_data.append((product_id, qty, price))

        cursor.execute(
            "INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)",
            (customer_id, order_date, total)
        )
        order_id = cursor.lastrowid

        for product_id, qty, price in item_data:
            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, item_price) VALUES (%s, %s, %s, %s)",
                (order_id, product_id, qty, price)
            )

    conn.commit()
    logging.info(f"Inserted {n_orders} orders and related order items.")

# --------------------------------
# Inserting Returns ( around 10%)
# --------------------------------
def insert_returns(rate):
    cursor.execute("SELECT order_item_id FROM order_items")
    order_items = [row[0] for row in cursor.fetchall()]
    returned_items = random.sample(order_items, int(len(order_items) * rate))

    reasons = [
        "Item damaged", "Wrong item delivered", "No longer needed",
        "Too expensive", "Item arrived late"
    ]

    for item_id in returned_items:
        reason = random.choice(reasons)
        return_date = fake.date_between(start_date='-6mo', end_date='today')
        cursor.execute(
            "INSERT INTO returns (order_item_id, return_date, reason) VALUES (%s, %s, %s)",
            (item_id, return_date, reason)
        )

    conn.commit()
    logging.info(f"Inserted {len(returned_items)} returns.")

# --------------------------------
# Running Full Insert Routine
# --------------------------------
try:
    insert_products()
    insert_customers(CUSTOMER_COUNT)
    insert_orders_and_items(ORDER_COUNT)
    insert_returns(RETURN_RATE)
except Exception as e:
    logging.error(f"Error during insertion: {e}")
finally:
    cursor.close()
    conn.close()
    logging.info("Database population complete.")
