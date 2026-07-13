# Databricks notebook source
# MAGIC %md
# MAGIC # Healthcare Data Pipeline Architecture
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC This notebook provides a high-level overview of the Healthcare Data Pipeline architecture.
# MAGIC
# MAGIC The pipeline follows the Medallion Architecture using Databricks, Delta Lake, and PySpark to transform raw healthcare data into business-ready analytical datasets.

# COMMAND ----------

# MAGIC %md
# MAGIC ## End-to-End Pipeline Flow
# MAGIC
# MAGIC Healthcare CSV Dataset
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Unity Catalog Volume
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Bronze Layer
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Silver Layer
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Gold Layer
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Business Analytics
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Power BI Dashboard
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Business Insights

# COMMAND ----------

# MAGIC %md
# MAGIC ## Architecture Components
# MAGIC
# MAGIC ### Data Source
# MAGIC Healthcare patient dataset stored as CSV.
# MAGIC
# MAGIC ### Storage
# MAGIC Unity Catalog Volume stores the raw source file.
# MAGIC
# MAGIC ### Bronze Layer
# MAGIC Stores raw healthcare data without modification.
# MAGIC
# MAGIC ### Silver Layer
# MAGIC Performs cleaning, validation, standardization, and prepares trusted datasets.
# MAGIC
# MAGIC ### Gold Layer
# MAGIC Creates business-ready analytical tables.
# MAGIC
# MAGIC ### Analytics
# MAGIC Spark SQL generates business insights from Gold tables.
# MAGIC
# MAGIC ### Visualization
# MAGIC Power BI consumes Gold tables to build executive dashboards.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Medallion Architecture
# MAGIC
# MAGIC Bronze Layer
# MAGIC
# MAGIC - Raw data
# MAGIC - No transformations
# MAGIC - Historical traceability
# MAGIC
# MAGIC Silver Layer
# MAGIC
# MAGIC - Data cleaning
# MAGIC - Duplicate removal
# MAGIC - Standardization
# MAGIC - Business rules
# MAGIC - SCD Type 2
# MAGIC
# MAGIC Gold Layer
# MAGIC
# MAGIC - Business aggregations
# MAGIC - Hospital ranking
# MAGIC - Dashboard summary
# MAGIC - Analytical datasets

# COMMAND ----------

# MAGIC %md
# MAGIC ## ETL Workflow
# MAGIC
# MAGIC Extract
# MAGIC
# MAGIC - Read Healthcare CSV
# MAGIC
# MAGIC Transform
# MAGIC
# MAGIC - Bronze
# MAGIC - Silver
# MAGIC - Gold
# MAGIC
# MAGIC Load
# MAGIC
# MAGIC - Delta Tables
# MAGIC - Business Analytics
# MAGIC - Power BI Dashboard

# COMMAND ----------

# MAGIC %md
# MAGIC ## Technologies Used
# MAGIC
# MAGIC - Databricks
# MAGIC - PySpark
# MAGIC - Spark SQL
# MAGIC - Delta Lake
# MAGIC - Delta Tables
# MAGIC - Unity Catalog
# MAGIC - Python
# MAGIC - Git
# MAGIC - GitHub
# MAGIC - Power BI

# COMMAND ----------

# MAGIC %md
# MAGIC ## Why Medallion Architecture?
# MAGIC
# MAGIC The Medallion Architecture separates raw, cleaned, and business-ready data into different layers.
# MAGIC
# MAGIC Benefits include:
# MAGIC
# MAGIC - Improved data quality
# MAGIC - Better scalability
# MAGIC - Easier maintenance
# MAGIC - Reliable analytics
# MAGIC - Support for future machine learning

# COMMAND ----------

# MAGIC %md
# MAGIC # Summary
# MAGIC
# MAGIC This notebook summarized the complete Healthcare Data Pipeline architecture.
# MAGIC
# MAGIC The project demonstrates modern Data Engineering practices including:
# MAGIC
# MAGIC - Medallion Architecture
# MAGIC - Delta Lake
# MAGIC - Incremental Loading
# MAGIC - Business Analytics
# MAGIC - Data Governance
# MAGIC - Dashboard-ready Gold tables

# COMMAND ----------

