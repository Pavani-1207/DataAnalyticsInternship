import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATASET
# =========================

print("Loading Website Traffic Dataset...")

df = pd.read_csv("website_traffic.csv")

# =========================
# DISPLAY BASIC INFORMATION
# =========================

print("\n==============================")
print("FIRST 5 ROWS")
print("==============================")
print(df.head())

print("\n==============================")
print("DATASET INFORMATION")
print("==============================")
print(df.info())

print("\n==============================")
print("DATASET SHAPE")
print("==============================")
print(df.shape)

# =========================
# CHECK MISSING VALUES
# =========================

print("\n==============================")
print("MISSING VALUES")
print("==============================")
print(df.isnull().sum())

# =========================
# REMOVE MISSING VALUES
# =========================

df = df.dropna()

print("\nMissing values removed successfully!")

# =========================
# DISPLAY CLEANED DATA
# =========================

print("\n==============================")
print("CLEANED DATASET SHAPE")
print("==============================")
print(df.shape)

# =========================
# BASIC STATISTICS
# =========================

print("\n==============================")
print("BASIC STATISTICS")
print("==============================")
print(df.describe())

# =========================
# TRAFFIC TREND GRAPH
# =========================

plt.figure(figsize=(12,5))

plt.plot(df["Date"], df["Visits"])

plt.title("Website Traffic Trend")

plt.xlabel("Date")
plt.ylabel("Number of Visits")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("traffic_trend.png")

plt.show()

# =========================
# TRAFFIC DISTRIBUTION GRAPH
# =========================

plt.figure(figsize=(8,5))

sns.histplot(df["Visits"], bins=20)

plt.title("Traffic Distribution")

plt.xlabel("Number of Visits")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("traffic_distribution.png")

plt.show()

# =========================
# AVERAGE TRAFFIC
# =========================

average_traffic = df["Visits"].mean()

print("\n==============================")
print("AVERAGE DAILY TRAFFIC")
print("==============================")
print(average_traffic)

# =========================
# MAXIMUM TRAFFIC
# =========================

max_traffic = df["Visits"].max()

print("\n==============================")
print("MAXIMUM DAILY TRAFFIC")
print("==============================")
print(max_traffic)

# =========================
# MINIMUM TRAFFIC
# =========================

min_traffic = df["Visits"].min()

print("\n==============================")
print("MINIMUM DAILY TRAFFIC")
print("==============================")
print(min_traffic)

# =========================
# PROJECT INSIGHTS
# =========================

print("\n==============================")
print("PROJECT INSIGHTS")
print("==============================")

print("""
1. Website traffic changes across different days.

2. Some days receive significantly higher visitor counts.

3. Traffic distribution helps understand visitor behavior.

4. Businesses can identify peak traffic periods.

5. Website analytics helps improve engagement and marketing strategies.
""")

# =========================
# FINAL MESSAGE
# =========================

print("\n==============================")
print("WEB TRAFFIC ANALYTICS COMPLETED SUCCESSFULLY!")
print("==============================")