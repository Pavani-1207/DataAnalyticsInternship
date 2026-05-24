# Interactive Dashboard Development Project

## Project Overview

This project focuses on developing a dashboard-style analytics system using sales and business data.

Dashboards help businesses:
- monitor performance
- visualize trends
- track key metrics
- support decision-making

The project uses Python libraries to generate visual charts and business insights from the Global Superstore dataset.

---

# Objective

The main objectives of this project are:

- Create dashboard visualizations
- Analyze sales performance
- Evaluate profit trends
- Identify top-performing products
- Generate business insights

---

# Dataset Information

## Dataset Used
Global Superstore Dataset

## File Name
Global_Superstore2.csv

---

# Dataset Features

The dataset contains:

- Region
- Market
- Sales
- Profit
- Product Name
- Category
- Customer Details
- Order Information

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

The dashboard project was completed through several stages:

---

## Loading the Dataset

The dataset was loaded using Pandas.

```python
df = pd.read_csv("Global_Superstore2.csv", encoding='latin1')


## Sales by Region Analysis

Sales data was grouped by region to identify high-performing business areas.

Visualization:

Sales by Region Chart

This helps businesses:

compare regional performance
identify profitable regions
## Profit by Category Analysis

Profit analysis was performed for different product categories.

Visualization:

Profit by Category Chart

This helps identify:

profitable categories
weak-performing categories
## Market Distribution Analysis

Market-wise sales contribution was visualized using pie charts.

Visualization:

Market Sales Distribution Chart

This helps understand:

market dominance
sales contribution by market
## Top Products Analysis

Top-performing products were identified based on total sales.

Visualization:

Top 10 Products by Sales

This helps businesses:

identify high-demand products
improve inventory planning...