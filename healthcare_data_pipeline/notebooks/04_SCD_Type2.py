# Databricks notebook source
# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Patient Dimension - SCD Type 2
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC This notebook creates the Patient Dimension table from the Silver layer.
# MAGIC
# MAGIC It demonstrates Delta Lake MERGE and Slowly Changing Dimension (SCD Type 2) by preserving historical patient records whenever changes occur.

# COMMAND ----------

# ==========================================
# Configuration
# ==========================================

CATALOG = "workspace"
SCHEMA = "healthcare"

SILVER_TABLE = f"{CATALOG}.{SCHEMA}.silver_patient_records"
DIM_PATIENT_TABLE = f"{CATALOG}.{SCHEMA}.dim_patient"

print("Silver :", SILVER_TABLE)
print("Dimension :", DIM_PATIENT_TABLE)

# COMMAND ----------

silver_df = spark.table(SILVER_TABLE)

display(silver_df)

# COMMAND ----------

from pyspark.sql.functions import current_timestamp, lit

dim_patient_df = (
    silver_df
    .withColumn("effective_start_date", current_timestamp())
    .withColumn("effective_end_date", lit(None).cast("timestamp"))
    .withColumn("is_current", lit(True))
)

display(dim_patient_df)

# COMMAND ----------

from pyspark.sql.functions import monotonically_increasing_id

dim_patient_df = (
    dim_patient_df
    .withColumn(
        "patient_key",
        monotonically_increasing_id()
    )
)

display(dim_patient_df)

# COMMAND ----------

from pyspark.sql.functions import sha2, concat_ws

dim_patient_df = (
    dim_patient_df
    .withColumn(
        "patient_business_key",
        sha2(
            concat_ws(
                "|",
                "Name",
                "Gender",
                "Blood_Type"
            ),
            256
        )
    )
)

display(dim_patient_df)

# COMMAND ----------

# Save the Patient Dimension Table

dim_patient_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(DIM_PATIENT_TABLE)

# COMMAND ----------

display(
    spark.table(DIM_PATIENT_TABLE)
)

# COMMAND ----------

spark.table(DIM_PATIENT_TABLE).printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Simulate Incoming Patient Updates
# MAGIC
# MAGIC To demonstrate incremental processing, we simulate a new batch of patient records with updated billing information.

# COMMAND ----------

from pyspark.sql.functions import col

# Simulate an incoming batch (3 existing patients)
updates_df = (
    dim_patient_df
    .limit(3)
    .withColumn(
        "Billing_Amount",
        col("Billing_Amount") + 2000
    )
)

display(updates_df)

# COMMAND ----------

from delta.tables import DeltaTable

print("Delta Lake is available!")

# COMMAND ----------

from delta.tables import DeltaTable

print("Delta Lake is available!")

# COMMAND ----------

updates_df.createOrReplaceTempView("patient_updates")

print("Temporary View Created Successfully!")

# COMMAND ----------

display(spark.sql("""
SELECT
    patient_business_key,
    Name,
    Billing_Amount,
    is_current
FROM patient_updates
"""))

# COMMAND ----------

spark.version