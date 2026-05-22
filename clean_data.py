import pandas as pd

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Show first 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing Age values with average age
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing Embarked values
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Remove Cabin column because too many missing values
df.drop(columns=["Cabin"], inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_titanic_data.csv", index=False)

print("\nDATA CLEANING COMPLETED")
print("\nCleaned dataset saved successfully!")