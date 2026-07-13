# Databricks notebook source
# MAGIC %md
# MAGIC # Delta Live Tables (DLT)
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Delta Live Tables (DLT) is a declarative data engineering framework provided by Databricks for building reliable, maintainable, and automated data pipelines.
# MAGIC
# MAGIC This notebook explains how the Healthcare Data Pipeline can be implemented using Delta Live Tables.

# COMMAND ----------

# MAGIC %md
# MAGIC ## What is Delta Live Tables?
# MAGIC
# MAGIC Delta Live Tables (DLT) simplifies ETL development by automatically managing:
# MAGIC
# MAGIC - Data dependencies
# MAGIC - Pipeline orchestration
# MAGIC - Data quality validation
# MAGIC - Error handling
# MAGIC - Incremental processing
# MAGIC - Pipeline monitoring
# MAGIC
# MAGIC DLT enables Data Engineers to build reliable production pipelines with minimal operational overhead.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Benefits of Delta Live Tables
# MAGIC
# MAGIC - Automated ETL pipelines
# MAGIC - Built-in monitoring
# MAGIC - Automatic dependency management
# MAGIC - Data quality enforcement
# MAGIC - Incremental processing
# MAGIC - Reliable production workloads
# MAGIC - Simplified maintenance

# COMMAND ----------

# MAGIC %md
# MAGIC ## Healthcare Pipeline using Delta Live Tables
# MAGIC
# MAGIC Healthcare CSV
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Bronze Live Table
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Silver Live Table
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Gold Live Table
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Business Analytics
# MAGIC
# MAGIC ↓
# MAGIC
# MAGIC Power BI Dashboard

# COMMAND ----------

print("=" * 70)
print("DELTA LIVE TABLES PIPELINE")
print("=" * 70)

print("Bronze Layer  -> Raw Healthcare Data")
print("Silver Layer  -> Cleaned Healthcare Data")
print("Gold Layer    -> Business Analytics")
print("Power BI      -> Dashboard")

print("=" * 70)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Quality Expectations
# MAGIC
# MAGIC Delta Live Tables allows developers to define expectations that automatically validate incoming data.
# MAGIC
# MAGIC Examples include:
# MAGIC
# MAGIC - Age must be greater than 0
# MAGIC - Billing Amount must be positive
# MAGIC - Name cannot be NULL
# MAGIC - Hospital cannot be NULL
# MAGIC
# MAGIC Invalid records can be dropped, quarantined, or reported for further investigation.

# COMMAND ----------

print("=" * 70)

print("DELTA LIVE TABLES EXPECTATIONS")

print("=" * 70)

print("✓ Name IS NOT NULL")

print("✓ Age > 0")

print("✓ Billing_Amount > 0")

print("✓ Hospital IS NOT NULL")

print("=" * 70)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example Delta Live Table Pipeline
# MAGIC
# MAGIC The following example demonstrates how a Silver table could be created using Delta Live Tables.
# MAGIC
# MAGIC ```python
# MAGIC import dlt
# MAGIC
# MAGIC @dlt.table(
# MAGIC     name="silver_patient_records"
# MAGIC )
# MAGIC def silver_table():
# MAGIC
# MAGIC     return (
# MAGIC         spark.read.table("bronze_patient_records")
# MAGIC     )
# MAGIC ```
# MAGIC
# MAGIC The above example is provided for learning purposes. This project uses standard Databricks notebooks because Delta Live Tables are not available in the Databricks Free Edition.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Pipeline Monitoring
# MAGIC
# MAGIC Delta Live Tables automatically provides:
# MAGIC
# MAGIC - Pipeline execution history
# MAGIC - Data lineage
# MAGIC - Pipeline monitoring
# MAGIC - Error reporting
# MAGIC - Automatic retries
# MAGIC - Performance metrics
# MAGIC
# MAGIC These capabilities simplify production-grade pipeline management.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Why Delta Live Tables?
# MAGIC
# MAGIC Compared to traditional ETL notebooks, Delta Live Tables provide:
# MAGIC
# MAGIC - Less manual coding
# MAGIC - Automatic dependency resolution
# MAGIC - Better monitoring
# MAGIC - Simplified maintenance
# MAGIC - Production-ready workflows
# MAGIC - Built-in data quality validation
# MAGIC
# MAGIC DLT enables scalable and reliable modern data engineering pipelines.

# COMMAND ----------

# MAGIC %md
# MAGIC # Summary
# MAGIC
# MAGIC This notebook introduced Delta Live Tables (DLT) and explained how they can be used to automate modern data engineering workflows.
# MAGIC
# MAGIC Although this project was implemented using Databricks notebooks, the same Medallion Architecture can be deployed using Delta Live Tables in enterprise environments.