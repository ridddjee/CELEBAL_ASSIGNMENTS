
# SQL-Based Data Analysis Using Filtering, Aggregation, and Business Queries

##  About This Project
This project focuses on analyzing sales data using SQL and solving real-world business problems through data analysis techniques.  
The main goal of this project is to strengthen SQL concepts like filtering, aggregation, joins, sorting, and business query analysis using a Superstore sales dataset.

The project demonstrates how SQL can be used to extract meaningful insights from raw business data and support data-driven decision-making.

---

#  Project Objectives
- Load and work with a real-world sales dataset
- Understand table structure and schema
- Perform data filtering using `WHERE`
- Use aggregation functions for analysis
- Generate business insights from sales data
- Practice SQL queries used in industry-level analytics
- Validate and clean data records

---

#  Tools & Technologies
- SQL
- MySQL / PostgreSQL / SQLite
- Kaggle Superstore Dataset
- Jupyter Notebook (Optional)

---

#  Dataset Information
This project uses the popular **Superstore Dataset** available on Kaggle.

The dataset includes:
- Customer information
- Product categories
- Sales records
- Profit and quantity data
- Regional business performance

### Dataset Link
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

---

# 📊 SQL Concepts Used
During this project, the following SQL concepts were implemented:

- `SELECT`
- `WHERE`
- `ORDER BY`
- `GROUP BY`
- `HAVING`
- `LIMIT`
- Aggregate Functions:
  - `SUM()`
  - `AVG()`
  - `COUNT()`
  - `MAX()`
  - `MIN()`
- Joins:
  - `INNER JOIN`
  - `LEFT JOIN`
- CASE Statements
- Duplicate Detection Queries
- Data Validation Techniques

---

#  Business Problems Solved
This project includes different business-related analytical queries such as:

- Finding top-selling products
- Identifying high-profit categories
- Regional sales analysis
- Monthly sales trend analysis
- Top customers by revenue
- Duplicate record detection
- Average order value calculation
- Category-wise performance comparison

---

#  Project Structure
```bash
SQL-Data-Analysis/
│
├── dataset/
│   └── superstore.csv
│
├── queries/
│   ├── filtering_queries.sql
│   ├── aggregation_queries.sql
│   ├── joins_queries.sql
│   └── business_case_queries.sql
│
├── notebooks/
│   └── analysis.ipynb
│
└── README.md
```

---

# 🚀 Steps Performed
1. Imported the dataset into SQL database
2. Explored schema and sample records
3. Applied filtering conditions using SQL
4. Performed aggregation and grouping
5. Generated business insights
6. Validated data quality and duplicates
7. Executed analytical SQL queries

---

#  Sample SQL Queries

## Total Sales by Region
```sql
SELECT Region, SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY Region;
```

## Top 5 Customers by Revenue
```sql
SELECT Customer_Name, SUM(Sales) AS Revenue
FROM Orders
GROUP BY Customer_Name
ORDER BY Revenue DESC
LIMIT 5;
```

---

#  Key Insights
- Identified regions with highest sales
- Analyzed profitable product categories
- Tracked monthly sales growth patterns
- Detected duplicate records for data validation
- Compared customer purchasing behavior

---

#  Learning Outcomes
Through this project, I gained practical experience in:

- Writing optimized SQL queries
- Business-oriented data analysis
- Data aggregation and filtering
- Solving real-world analytical problems
- Understanding sales and customer trends

---

 # Author

## Ridam Agrawal
---
