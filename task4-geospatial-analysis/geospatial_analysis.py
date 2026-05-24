import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATASET
# =========================

print("Loading Geospatial Dataset...")

df = pd.read_csv("Global_Superstore2.csv", encoding='latin1')

# =========================
# DISPLAY BASIC INFORMATION
# =========================

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

print("\nDATASET SHAPE")
print(df.shape)

# =========================
# CHECK MISSING VALUES
# =========================

print("\nMISSING VALUES")
print(df.isnull().sum())

# =========================
# COUNTRY SALES ANALYSIS
# =========================

country_sales = df.groupby("Country")["Sales"].sum().sort_values(ascending=False)

print("\nTOP COUNTRY SALES")
print(country_sales.head(10))

# =========================
# TOP 10 COUNTRIES GRAPH
# =========================

top_10 = country_sales.head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_10.values,
    y=top_10.index
)

plt.title("Top 10 Countries by Sales")

plt.xlabel("Total Sales")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig("top_country_sales.png")

plt.show()

# =========================
# REGION SALES ANALYSIS
# =========================

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\nREGION SALES")
print(region_sales)

# =========================
# REGION SALES GRAPH
# =========================

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

plt.savefig("region_sales.png")

plt.show()

# =========================
# MARKET ANALYSIS
# =========================

market_sales = df.groupby("Market")["Sales"].sum()

plt.figure(figsize=(8,5))

market_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Market Sales Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig("market_distribution.png")

plt.show()

# =========================
# PROJECT INSIGHTS
# =========================

print("\n======================")
print("PROJECT INSIGHTS")
print("======================")

print("""
1. Some countries generate significantly higher sales.

2. Regional sales performance varies across markets.

3. Market distribution helps identify business opportunities.

4. Businesses can target high-performing regions for expansion.

5. Geospatial analysis supports strategic decision-making.
""")

print("\nGeospatial Data Analysis Completed Successfully!")