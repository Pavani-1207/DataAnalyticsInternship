# Customer Churn Analysis Project

## Project Overview

This project focuses on analyzing customer churn data to identify patterns and factors that influence customer cancellations.

Customer churn refers to customers discontinuing a company's service. Understanding churn behavior helps businesses improve customer retention strategies and enhance customer satisfaction.

The project uses a telecom customer dataset to analyze customer behavior, subscription patterns, monthly charges, internet services, and contract types.

The analysis was performed using Python, Pandas, Matplotlib, and Seaborn.

---

# Objective

The main objectives of this project are:

- Analyze customer churn behavior
- Identify factors affecting churn
- Visualize customer trends
- Generate business insights
- Understand customer retention patterns

---

# Dataset Information

## Dataset Used
Telco Customer Churn Dataset

## Source
Kaggle Customer Churn Dataset

## File Name
WA_Fn-UseC_-Telco-Customer-Churn.csv

---

# Dataset Features

The dataset contains customer-related information including:

- Customer ID
- Gender
- Senior Citizen Status
- Tenure
- Contract Type
- Internet Service
- Monthly Charges
- Total Charges
- Payment Method
- Churn Status

---

# Technologies Used

| Tool | Purpose |
|------|----------|
| Python | Programming Language |
| Pandas | Data Analysis |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| VS Code | Code Editor |

---

# Project Workflow

The project was completed in several stages:

---

## 1. Loading the Dataset

The dataset was loaded using the Pandas library.

```python
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

## 2. Understanding the Dataset

Basic dataset exploration was performed using:

head()
info()
shape

This helped in understanding:

number of rows and columns
data types
dataset structure

## 3. Checking Missing Values

Missing values were checked using:

df.isnull().sum()

This ensures data quality before analysis.

## 4. Customer Churn Analysis

Customer churn count was analyzed to determine:

how many customers left the service
how many customers remained

Visualization:

Customer churn count graph

## 5. Monthly Charges Analysis

Monthly charges were analyzed against churn status to understand whether pricing affects customer retention.

Visualization:

Boxplot of Monthly Charges vs Churn

## 6. Contract Type Analysis

Customer contract types were analyzed to identify which contract plans experience higher churn.

Visualization:

Contract Type vs Churn chart

## 7. Internet Service Analysis

Internet service categories were analyzed to understand churn behavior among different service users.

Visualization:

Internet Service vs Churn chart

## Conclusion

This project demonstrates how customer data can be analyzed to identify churn patterns and customer retention factors.

The generated insights can help businesses:

improve customer satisfaction
reduce churn rates
design better subscription plans
increase customer loyalty