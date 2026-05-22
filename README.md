# Data Cleaning & Structural Validation Project

## Project Overview

This project focuses on cleaning and validating a raw dataset using Python and Pandas.  
The dataset used for this project is the Titanic Dataset, which contains passenger information such as age, gender, ticket class, fare, and survival status.

Raw datasets often contain:
- Missing values
- Duplicate records
- Unstructured data
- Inconsistent formatting

The goal of this project is to transform the raw dataset into a clean and structured format that can be used for further data analysis and visualization.

---

# Objective

The main objectives of this project are:

- Identify and handle missing values
- Detect and remove duplicate records
- Improve dataset consistency
- Remove unnecessary columns
- Prepare the dataset for analysis
- Save the cleaned dataset into a new CSV file

---

# Dataset Information

## Dataset Used
Titanic Dataset

## Source
Kaggle Titanic Dataset

## File Name
Titanic-Dataset.csv

## Dataset Features
The dataset contains information about Titanic passengers including:

- Passenger ID
- Passenger Class
- Name
- Gender
- Age
- Fare
- Cabin
- Embarked Location
- Survival Status

---

# Technologies Used

The following tools and technologies were used in this project:

| Tool | Purpose |
|------|----------|
| Python | Programming Language |
| Pandas | Data Cleaning and Analysis |
| VS Code | Code Editor |
| CSV File | Dataset Format |

---

# Project Workflow

The project was completed in several steps:

## 1. Loading the Dataset
The Titanic dataset was loaded using the Pandas library.

```python
df = pd.read_csv("Titanic-Dataset.csv")


## 2. Understanding the Dataset

The following checks were performed:

Displayed first 5 rows
Checked dataset shape
Viewed column details
Examined data types

Functions used:

head()
info()
shape

## 3. Checking Missing Values

Missing values were identified using:

df.isnull().sum()

Columns with missing values included:

Age
Cabin
Embarked


## 4. Removing Duplicate Records

Duplicate rows were identified and removed using:

df.drop_duplicates(inplace=True)

This improves data quality and avoids repeated information.

## 5. Handling Missing Values
Age Column

Missing age values were filled using the average age value.

df["Age"] = df["Age"].fillna(df["Age"].mean())
Embarked Column

Missing embarkation values were filled using the most common value.

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
Fare Column

Missing fare values were filled using the average fare.

df["Fare"] = df["Fare"].fillna(df["Fare"].mean())


## 6. Removing Unnecessary Columns

The Cabin column contained too many missing values, so it was removed from the dataset.

df.drop(columns=["Cabin"], inplace=True)


## 7. Saving the Cleaned Dataset

After cleaning, the dataset was saved into a new CSV file.

df.to_csv("cleaned_titanic_data.csv", index=False)

Hence, these are the steps we have followed to clean the dataset.