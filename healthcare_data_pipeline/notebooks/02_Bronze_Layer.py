# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze Layer
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC This notebook ingests the raw healthcare dataset from Unity Catalog Volume and stores it as a Bronze Delta Table.
# MAGIC
# MAGIC No transformations are performed in this layer.
# MAGIC
# MAGIC The data is stored exactly as received from the source.

# COMMAND ----------

CATALOG = "workspace"
SCHEMA = "healthcare"

BRONZE_TABLE = f"{CATALOG}.{SCHEMA}.bronze_patient_records"
SILVER_TABLE = f"{CATALOG}.{SCHEMA}.silver_patient_records"

# COMMAND ----------

# Bronze Layer

DATA_PATH = "/Volumes/workspace/healthcare/raw_data/patients_records.csv"

print(DATA_PATH)

# COMMAND ----------

bronze_df = (
    spark.read
         .option("header", "true")
         .option("inferSchema", "true")
         .csv(DATA_PATH)
)

display(bronze_df)

# COMMAND ----------

print("Total Rows :", bronze_df.count())
print("Total Columns :", len(bronze_df.columns))

# COMMAND ----------

bronze_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col

# Replace spaces with underscores in column names
bronze_df = bronze_df.toDF(
    *[column.replace(" ", "_") for column in bronze_df.columns]
)

# COMMAND ----------

bronze_df.columns

# COMMAND ----------

bronze_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.healthcare.bronze_patient_records")

# COMMAND ----------

display(spark.table("workspace.healthcare.bronze_patient_records"))

# COMMAND ----------

bronze_df = spark.table("workspace.healthcare.bronze_patient_records")

# COMMAND ----------

bronze_df = spark.table(BRONZE_TABLE)

# COMMAND ----------

# MAGIC %md
# MAGIC # Bronze Layer Summary
# MAGIC
# MAGIC ## Completed Tasks
# MAGIC
# MAGIC - Successfully ingested raw healthcare dataset
# MAGIC - Preserved original data
# MAGIC - Standardized column names
# MAGIC - Stored data as Delta Table
# MAGIC - Validated successful ingestion
# MAGIC
# MAGIC The Bronze layer serves as the raw data foundation of the Healthcare Data Pipeline.