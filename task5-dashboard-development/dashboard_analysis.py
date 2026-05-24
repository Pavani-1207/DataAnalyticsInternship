import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATASET
# =========================

print("Loading Dashboard Dataset...")

df = pd.read_csv("Global_Superstore2.csv", encoding='latin1')

# =========================
# DISPLAY BASIC INFORMATION
# =========================

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

# =========================
# SALES BY REGION
# =========================

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

plt.title("Sales by Region")

plt.xlabel("Region")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("sales_by_region.png")

plt.show()

# =========================
# PROFIT BY CATEGORY
# =========================

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=category_profit.index,
    y=category_profit.values
)

plt.title("Profit by Category")

plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("profit_by_category.png")

plt.show()

# =========================
# MARKET DISTRIBUTION
# =========================

market_sales = df.groupby("Market")["Sales"].sum()

plt.figure(figsize=(8,6))

market_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Market Sales Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig("market_sales_distribution.png")

plt.show()

# =========================
# TOP 10 PRODUCTS
# =========================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 10 Products by Sales")

plt.xlabel("Sales")
plt.ylabel("Product Name")

plt.tight_layout()

plt.savefig("top_products.png")

plt.show()

# =========================
# PROJECT INSIGHTS
# =========================

print("\n======================")
print("PROJECT INSIGHTS")
print("======================")

print("""
1. Some regions generate higher sales than others.

2. Product categories contribute differently to profits.

3. Certain markets dominate total sales distribution.

4. Top-selling products generate significant revenue.

5. Dashboards help businesses monitor performance effectively.
""")

print("\nInteractive Dashboard Analysis Completed Successfully!")