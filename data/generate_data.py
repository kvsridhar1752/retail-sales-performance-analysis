import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(7)

n = 8000
dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(np.random.randint(0, 365, n), unit="D")
categories = ["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Sports"]
category = np.random.choice(categories, n, p=[0.25, 0.25, 0.20, 0.15, 0.15])
regions = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]
region = np.random.choice(regions, n)
payments = ["Credit Card", "PayPal", "Bank Transfer", "Cash on Delivery"]
payment = np.random.choice(payments, n, p=[0.45, 0.30, 0.15, 0.10])

price_map = {
    "Electronics": (25, 500),
    "Clothing": (10, 120),
    "Home & Kitchen": (15, 250),
    "Beauty": (5, 80),
    "Sports": (12, 200)
}

unit_price = np.array([np.random.uniform(*price_map[c]) for c in category])
quantity = np.random.choice([1, 2, 3, 4], n, p=[0.55, 0.25, 0.13, 0.07])
revenue = np.round(unit_price * quantity, 2)

product_names = {
    "Electronics": ["Wireless Earbuds", "Smart Watch", "Bluetooth Speaker", "USB-C Charger"],
    "Clothing": ["Cotton T-Shirt", "Denim Jacket", "Running Shoes", "Hoodie"],
    "Home & Kitchen": ["Air Fryer", "Coffee Maker", "Storage Box", "LED Lamp"],
    "Beauty": ["Face Serum", "Shampoo", "Lipstick", "Moisturizer"],
    "Sports": ["Yoga Mat", "Dumbbell Set", "Water Bottle", "Fitness Band"]
}

product = [np.random.choice(product_names[c]) for c in category]

df = pd.DataFrame({
    "order_id": [f"SO{i:06d}" for i in range(1, n + 1)],
    "order_date": dates.strftime("%Y-%m-%d"),
    "customer_id": [f"CUST{np.random.randint(1000, 5000)}" for _ in range(n)],
    "product_category": category,
    "product_name": product,
    "region": region,
    "quantity": quantity,
    "unit_price_eur": np.round(unit_price, 2),
    "revenue_eur": revenue,
    "payment_method": payment
})

Path("data").mkdir(exist_ok=True)
df.to_csv("data/retail_sales.csv", index=False)
print(f"Created data/retail_sales.csv with {len(df)} records.")
