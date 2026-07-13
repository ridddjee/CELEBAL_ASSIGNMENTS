## Overview

This project is part of the Celebal Technologies Internship Program. The objective is to perform sales data analysis using SQL by applying aggregate functions, Common Table Expressions (CTEs), JOIN operations, and Window Functions to extract meaningful business insights from customer order data.

## Dataset

The dataset consists of two tables:

### Customers Table

* customer_id
* customer_name
* segment
* region

### Orders Table

* order_id
* customer_id
* order_date
* ship_date
* sales
* quantity
* discount
* profit

## Objectives

The project aims to:

1. Analyze customer purchasing behavior.
2. Calculate total and average sales.
3. Identify highest-value customers.
4. Rank customers based on sales performance.
5. Find customers with above-average sales.
6. Determine highest order values per customer.
7. Apply SQL Window Functions for advanced analytics.

## SQL Concepts Used

### Aggregate Functions

* SUM()
* AVG()
* MAX()
* COUNT()

### Common Table Expressions (CTEs)

* Used to create temporary result sets for reusable sales calculations.

### Window Functions

* DENSE_RANK()
* ROW_NUMBER()

### JOIN Operations

* INNER JOIN between Customers and Orders tables.

## Tasks Performed

### 1. Average Sales Calculation

Calculated the average sales value across all orders.

### 2. Highest Sales Order per Customer

Identified the order with the maximum sales value for every customer.

### 3. Customer Sales Summary

Generated total sales for each customer using a CTE.

### 4. Customer Ranking

Ranked customers according to their total sales using DENSE_RANK().

### 5. Order Sequencing

Assigned sequential numbers to orders for each customer using ROW_NUMBER().

### 6. Top 5 Customers

Retrieved customers with the highest total sales.

### 7. Bottom 5 Customers

Retrieved customers with the lowest total sales.

### 8. Single-Order Customers

Identified customers who placed only one order.

### 9. Above-Average Customers

Found customers whose total sales exceeded the average customer sales.

### 10. Highest Order Value per Customer

Calculated the maximum order value achieved by each customer.

## Key Learnings

* Writing efficient SQL queries.
* Using CTEs for modular query design.
* Applying Window Functions for ranking and sequencing.
* Combining multiple tables using JOINs.
* Performing business-oriented data analysis using SQL.

## Tools Used

* MySQL Workbench
* SQL
* Relational Database Concepts

## Outcome

This project demonstrates practical SQL skills for data analysis and business reporting. It showcases the ability to work with real-world sales datasets, generate customer insights, and use advanced SQL features commonly required in Data Analyst and Data Engineering roles.

## Author

**Ridam Agrawal**


This README is professional enough for GitHub, internship submission, and resume project links.
