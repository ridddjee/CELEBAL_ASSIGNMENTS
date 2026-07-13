# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Layer
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC This notebook reads data from the Bronze Delta table, performs data cleaning,
# MAGIC validation, standardization, and creates a Silver Delta Table.
# MAGIC
# MAGIC This layer improves data quality while preserving the original business information.

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# ==========================================
# Configuration
# ==========================================

CATALOG = "workspace"
SCHEMA = "healthcare"

BRONZE_TABLE = f"{CATALOG}.{SCHEMA}.bronze_patient_records"
SILVER_TABLE = f"{CATALOG}.{SCHEMA}.silver_patient_records"

print("Bronze Table :", BRONZE_TABLE)
print("Silver Table :", SILVER_TABLE)

# COMMAND ----------

silver_df = spark.table(BRONZE_TABLE)

display(silver_df)

# COMMAND ----------

print(f"Total Rows    : {silver_df.count()}")
print(f"Total Columns : {len(silver_df.columns)}")

# COMMAND ----------

from pyspark.sql.functions import col, count, when

null_df = silver_df.select(
    [
        count(
            when(col(c).isNull(), c)
        ).alias(c)
        for c in silver_df.columns
    ]
)

display(null_df)

# COMMAND ----------

# Check duplicate records

total_rows = silver_df.count()
unique_rows = silver_df.dropDuplicates().count()

print(f"Total Rows      : {total_rows}")
print(f"Unique Rows     : {unique_rows}")
print(f"Duplicate Rows  : {total_rows - unique_rows}")

# COMMAND ----------

silver_df.describe().display()

# COMMAND ----------

silver_df.select("Gender").distinct().display()

# COMMAND ----------

silver_df.select("Test_Results").distinct().display()

# COMMAND ----------

# Remove duplicate records

silver_df = silver_df.dropDuplicates()

print("Rows After Removing Duplicates :", silver_df.count())

# COMMAND ----------

from pyspark.sql.functions import to_date

silver_df = (
    silver_df
        .withColumn(
            "Date_of_Admission",
            to_date("Date_of_Admission")
        )
        .withColumn(
            "Discharge_Date",
            to_date("Discharge_Date")
        )
)

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

silver_df = silver_df.withColumn(
    "processed_timestamp",
    current_timestamp()
)

# COMMAND ----------

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(SILVER_TABLE)

# COMMAND ----------

display(
    spark.table(SILVER_TABLE)
)

# COMMAND ----------

# MAGIC %md
# MAGIC # Incremental Processing using Delta MERGE (SCD Type 2)
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC In a production environment, new healthcare records arrive every day.
# MAGIC
# MAGIC Instead of overwriting the Silver table, we use Delta Lake MERGE with SCD Type 2 to preserve historical records while inserting updated records.
# MAGIC
# MAGIC Since this project uses a static dataset, we simulate a new batch of incoming records.

# COMMAND ----------

print(globals().keys())

# COMMAND ----------

# ==========================================
# Configuration
# ==========================================

CATALOG = "workspace"
SCHEMA = "healthcare"

BRONZE_TABLE = f"{CATALOG}.{SCHEMA}.bronze_patient_records"
SILVER_TABLE = f"{CATALOG}.{SCHEMA}.silver_patient_records"

print(BRONZE_TABLE)
print(SILVER_TABLE)

# COMMAND ----------

silver_df = spark.table(SILVER_TABLE)

display(silver_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Silver Layer Summary
# MAGIC
# MAGIC ## Completed Tasks
# MAGIC
# MAGIC - Read Bronze Delta Table
# MAGIC - Performed data quality validation
# MAGIC - Removed duplicate records
# MAGIC - Converted date columns
# MAGIC - Added processing timestamp
# MAGIC - Created Silver Delta Table
# MAGIC
# MAGIC The Silver layer provides trusted and cleaned healthcare data for downstream analytics.