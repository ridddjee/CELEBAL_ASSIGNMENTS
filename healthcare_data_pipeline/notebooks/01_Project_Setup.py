# Databricks notebook source
# MAGIC %md
# MAGIC # Healthcare Data Pipeline
# MAGIC
# MAGIC ## Notebook 01 : Project Setup
# MAGIC
# MAGIC ### Objective
# MAGIC
# MAGIC This notebook initializes the Healthcare Data Pipeline project.
# MAGIC
# MAGIC It verifies the Databricks environment and prepares the project for the Medallion Architecture implementation.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Technology Stack
# MAGIC
# MAGIC - Databricks
# MAGIC - PySpark
# MAGIC - Spark SQL
# MAGIC - Delta Lake
# MAGIC - Python
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Project Layers
# MAGIC
# MAGIC - Bronze Layer (Raw Data)
# MAGIC - Silver Layer (Clean Data)
# MAGIC - Gold Layer (Business Analytics)

# COMMAND ----------

print("=" * 60)
print("Healthcare Data Pipeline")
print("Notebook : 01_Project_Setup")
print("Status   : Started Successfully")
print("=" * 60)

# COMMAND ----------

import sys

print("Python Version:", sys.version)

# COMMAND ----------

print("Spark Version:", spark.version)

# COMMAND ----------

print(spark)