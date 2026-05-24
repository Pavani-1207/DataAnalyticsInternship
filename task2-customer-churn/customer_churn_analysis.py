import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATASET
# =========================

print("Loading Dataset...")

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

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
# CUSTOMER CHURN COUNT
# =========================

print("\nCHURN COUNT")
print(df["Churn"].value_counts())

# =========================
# CREATE CHURN COUNT GRAPH
# =========================

plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)

plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.savefig("churn_count.png")
plt.show()

# =========================
# MONTHLY CHARGES VS CHURN
# =========================

plt.figure(figsize=(8,5))

sns.boxplot(x="Churn", y="MonthlyCharges", data=df)

plt.title("Monthly Charges vs Churn")

plt.savefig("monthly_charges_vs_churn.png")
plt.show()

# =========================
# CONTRACT TYPE ANALYSIS
# =========================

plt.figure(figsize=(8,5))

sns.countplot(x="Contract", hue="Churn", data=df)

plt.title("Contract Type vs Churn")

plt.xticks(rotation=10)

plt.savefig("contract_vs_churn.png")
plt.show()

# =========================
# INTERNET SERVICE ANALYSIS
# =========================

plt.figure(figsize=(8,5))

sns.countplot(x="InternetService", hue="Churn", data=df)

plt.title("Internet Service vs Churn")

plt.savefig("internet_service_vs_churn.png")
plt.show()

# =========================
# GENERATE INSIGHTS
# =========================

print("\n======================")
print("PROJECT INSIGHTS")
print("======================")

print("""
1. Customers with month-to-month contracts have higher churn.

2. Customers with higher monthly charges tend to leave more.

3. Fiber optic users show higher churn compared to DSL users.

4. Long-term contract customers are more loyal.
""")

print("\nCustomer Churn Analysis Completed Successfully!")