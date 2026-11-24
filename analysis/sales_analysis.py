from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

Path("output").mkdir(exist_ok=True)
df = pd.read_csv("data/retail_sales.csv", parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

overall = {
    "total_revenue_eur": round(df["revenue_eur"].sum(), 2),
    "total_orders": df["order_id"].nunique(),
    "total_units_sold": int(df["quantity"].sum()),
    "average_order_value_eur": round(df.groupby("order_id")["revenue_eur"].sum().mean(), 2)
}
print("Overall KPIs:", overall)

monthly = df.groupby("month").agg(revenue=("revenue_eur", "sum"), orders=("order_id", "nunique")).reset_index()
monthly["revenue"] = monthly["revenue"].round(2)
monthly.to_csv("output/monthly_revenue.csv", index=False)

category_kpis = df.groupby("product_category").agg(
    revenue=("revenue_eur", "sum"),
    orders=("order_id", "nunique"),
    units_sold=("quantity", "sum")
).reset_index().sort_values("revenue", ascending=False)
category_kpis["revenue"] = category_kpis["revenue"].round(2)
category_kpis.to_csv("output/category_kpis.csv", index=False)

region_kpis = df.groupby("region").agg(
    revenue=("revenue_eur", "sum"),
    orders=("order_id", "nunique"),
    average_order_value=("revenue_eur", "mean")
).reset_index().sort_values("revenue", ascending=False)
region_kpis["revenue"] = region_kpis["revenue"].round(2)
region_kpis["average_order_value"] = region_kpis["average_order_value"].round(2)
region_kpis.to_csv("output/region_kpis.csv", index=False)

top_products = df.groupby("product_name").agg(
    revenue=("revenue_eur", "sum"),
    units_sold=("quantity", "sum")
).reset_index().sort_values("revenue", ascending=False).head(10)
top_products["revenue"] = top_products["revenue"].round(2)
top_products.to_csv("output/top_products.csv", index=False)

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
axes[0, 0].plot(monthly["month"], monthly["revenue"], marker="o", color="#4C72B0")
axes[0, 0].set_title("Monthly Revenue Trend")
axes[0, 0].tick_params(axis="x", rotation=60)

axes[0, 1].bar(category_kpis["product_category"], category_kpis["revenue"], color="#55A868")
axes[0, 1].set_title("Revenue by Product Category")
axes[0, 1].tick_params(axis="x", rotation=30)

axes[1, 0].bar(region_kpis["region"], region_kpis["revenue"], color="#C44E52")
axes[1, 0].set_title("Revenue by Region")
axes[1, 0].tick_params(axis="x", rotation=30)

axes[1, 1].barh(top_products["product_name"], top_products["revenue"], color="#8172B2")
axes[1, 1].set_title("Top 10 Products by Revenue")
axes[1, 1].invert_yaxis()

plt.tight_layout()
plt.savefig("output/retail_sales_dashboard.png", dpi=150)
print("Saved KPI tables and dashboard to output/.")
