
# 🏥 Healthcare Data Pipeline using Databricks

> End-to-End Healthcare Data Engineering Pipeline using Databricks, PySpark, Delta Lake, Medallion Architecture and Power BI.

![Architecture](architecture/healthcare_architecture.png)

---

# 📌 Project Overview

This project demonstrates the implementation of a modern Healthcare Data Pipeline following the **Medallion Architecture (Bronze → Silver → Gold)** using **Databricks Lakehouse Platform**.

The pipeline ingests raw healthcare patient records, performs data cleaning and transformation using PySpark, creates business-ready analytical tables using Spark SQL, and visualizes insights through an interactive Power BI Dashboard.

This project was developed as the **Final Project** for the **Celebal Technologies Data Engineering Internship**.

---

# 🎯 Objectives

- Build an end-to-end healthcare data pipeline
- Implement Medallion Architecture
- Process healthcare records using PySpark
- Store data in Delta Lake
- Build Bronze, Silver and Gold tables
- Perform Business Analytics using Spark SQL
- Implement Incremental Data Loading
- Demonstrate Slowly Changing Dimension (SCD Type 2)
- Export Gold Layer data for Power BI
- Create an Executive Analytics Dashboard

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Databricks | Data Engineering Platform |
| PySpark | Data Processing |
| Spark SQL | Analytics |
| Delta Lake | Storage Layer |
| Unity Catalog | Data Governance |
| Python | ETL Development |
| Power BI | Dashboard & Visualization |

---

# 🏗 Project Architecture

The project follows the **Medallion Architecture**.

```
Raw Dataset
      │
      ▼
Bronze Layer
(Raw Delta Table)
      │
      ▼
Silver Layer
(Cleaned Data)
      │
      ▼
Gold Layer
(Business Tables)
      │
      ▼
Power BI Dashboard
```

---

# 📂 Project Structure

```
Healthcare_Data_Pipeline/
│
├── architecture/
│   └── healthcare_architecture.png
│
├── dashboard/
│   └── healthcare.pbix
│
├── dataset/
│   └── patient_records.csv
│
├── docs/
│   └── Healthcare_Data_Pipeline_Report.pdf
│
├── notebooks/
│   ├── 01_Project_Setup.ipynb
│   ├── 02_Bronze_Layer.ipynb
│   ├── 03_Silver_Layer.ipynb
│   ├── 04_SCD_Type2.ipynb
│   ├── 05_Gold_Layer.ipynb
│   ├── 06_Business_Analytics.ipynb
│   ├── 07_Incremental_Loading.ipynb
│   ├── 08_Delta_Live_Tables.ipynb
│   ├── 09_Data_Governance_and_Security.ipynb
│   ├── 10_Architecture_Overview.ipynb
│   └── 11_Export_For_PowerBI.ipynb
│
├── output/
│   ├── billing_summary.csv
│   ├── dashboard_summary.csv
│   ├── hospital_ranking.csv
│   ├── hospital_summary.csv
│   ├── insurance_summary.csv
│   ├── medical_condition_summary.csv
│   └── patient_summary.csv
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 📊 Medallion Layers

## 🥉 Bronze Layer

- Raw healthcare data ingestion
- Delta Table creation
- Schema validation
- Data storage without transformation

---

## 🥈 Silver Layer

- Null value handling
- Duplicate removal
- Data validation
- Data standardization
- Clean Delta table generation

---

## 🥇 Gold Layer

Business-ready analytical tables:

- Dashboard Summary
- Hospital Summary
- Hospital Ranking
- Insurance Summary
- Medical Condition Summary
- Patient Summary
- Billing Summary

---

# 🔄 Incremental Data Loading

The project demonstrates Incremental Loading using **Delta Lake MERGE**.

Features:

- Detects new records
- Updates existing records
- Prevents duplicate loading
- Supports scalable ETL workflows

---

# 🗂 Slowly Changing Dimension (SCD Type 2)

Implemented using Delta Lake to preserve historical records.

Features:

- Version history
- Effective dates
- Current record tracking
- Historical analysis support

---

# 🔒 Data Governance

Implemented using Unity Catalog.

Features:

- Centralized Metadata
- Table Management
- Data Governance
- Secure Data Access

---

# 📈 Business Analytics

Generated Gold Layer analytical tables:

- Hospital Revenue Analysis
- Insurance Provider Analysis
- Medical Condition Analysis
- Patient Summary
- Billing Summary
- Executive Dashboard Summary

---

# 📊 Power BI Dashboard

The Executive Dashboard includes:

✅ KPI Cards

- Total Patients
- Total Hospitals
- Total Doctors
- Total Revenue
- Average Billing
- Average Age

---

### 📉 Visualizations

- Top Hospitals by Revenue
- Revenue by Insurance Provider
- Patients by Medical Condition
- Hospital Billing Summary

Interactive Filters:

- Hospital
- Medical Condition
- Insurance Provider

---

# 📷 Project Screenshots

## Architecture

![Architecture](architecture/healthcare_architecture.png)

---

## Bronze Layer

![Bronze](screenshots/bronze_layer.png)

---

## Silver Layer

![Silver](screenshots/silver_layer.png)

---

## Gold Layer

![Gold](screenshots/gold_layer.png)

---

## Unity Catalog

![Catalog](screenshots/unity_catalog.png)

---

## Databricks Workspace

![Workspace](screenshots/workspace.png)

---

## Power BI Dashboard

![Dashboard](screenshots/executive_dashboard.png)

---

# 🚀 Key Features

- End-to-End ETL Pipeline
- Medallion Architecture
- Delta Lake
- PySpark Transformations
- Spark SQL Analytics
- Unity Catalog
- Incremental Loading
- SCD Type 2
- Power BI Dashboard
- Industry-standard Project Structure

---

# 📈 Business Outcomes

The pipeline transforms raw healthcare data into trusted business-ready datasets that help analyze:

- Hospital Performance
- Revenue Trends
- Patient Demographics
- Insurance Provider Distribution
- Medical Condition Statistics
- Executive KPIs

---

# 🔮 Future Enhancements

- Azure Data Factory Integration
- Databricks Workflows
- Real-time Streaming using Kafka
- ML/MLOps for Disease Prediction
- Automated Data Quality Monitoring
- CI/CD Deployment Pipeline

---

# ▶️ How to Run

1. Upload `patient_records.csv` to Databricks.
2. Execute notebooks in sequence:

```
01_Project_Setup
02_Bronze_Layer
03_Silver_Layer
04_SCD_Type2
05_Gold_Layer
06_Business_Analytics
07_Incremental_Loading
08_Delta_Live_Tables
09_Data_Governance_and_Security
10_Architecture_Overview
11_Export_For_PowerBI
```

3. Export Gold Layer CSV files.
4. Open `healthcare.pbix`.
5. Refresh data to view the dashboard.

---

# 📚 Internship Information

**Organization:** Celebal Technologies

**Domain:** Data Engineering

**Project:** Healthcare Data Pipeline using Databricks

**Architecture:** Medallion Architecture

---

# 👨‍💻 Author

**Ridam Agrawal**

**B.Tech (jecrc foundation )**

**Data Engineering Intern | Celebal Technologies**

---

⭐ If you found this project useful, consider giving this repository a star.
