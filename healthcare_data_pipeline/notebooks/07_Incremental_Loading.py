# Databricks notebook source
# MAGIC %md
# MAGIC # Incremental Data Loading using Delta Lake
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC In production environments, new healthcare records arrive continuously.
# MAGIC
# MAGIC Instead of reprocessing the complete dataset, Delta Lake supports incremental data loading by processing only newly arrived or updated records.
# MAGIC
# MAGIC This notebook demonstrates a simulated incremental load using a static healthcare dataset.

# COMMAND ----------

# Silver Table Name
SILVER_TABLE = "workspace.healthcare.silver_patient_records"

# Read Silver Table
silver_df = spark.table(SILVER_TABLE)

display(silver_df.limit(5))

# COMMAND ----------

SILVER_TABLE = "workspace.healthcare.silver_patient_records"

silver_df = spark.table(SILVER_TABLE)

display(silver_df.limit(10))

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

incremental_df = (
    silver_df
    .limit(5)
    .withColumn("processed_timestamp", current_timestamp())
)

display(incremental_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Simulated Incoming Batch
# MAGIC
# MAGIC Since the project uses a static CSV dataset, a small subset of records is selected to represent newly arrived patient data.
# MAGIC
# MAGIC In a real production pipeline, these records would originate from cloud storage (AWS S3 or Azure ADLS), APIs, Kafka streams, or hospital information systems.

# COMMAND ----------

# MAGIC %md
# MAGIC # Delta Lake MERGE Workflow
# MAGIC
# MAGIC The MERGE operation is one of the most powerful features of Delta Lake.
# MAGIC
# MAGIC It combines INSERT and UPDATE operations into a single transaction.
# MAGIC
# MAGIC This allows the pipeline to efficiently synchronize incoming records with existing data while maintaining ACID properties.

# COMMAND ----------

print("=" * 70)

print("DELTA MERGE WORKFLOW")

print("=" * 70)

print("Step 1 : Read Existing Silver Table")

print("Step 2 : Read Incoming Incremental Batch")

print("Step 3 : Match Records Using Business Key")

print("Step 4 : Update Existing Records")

print("Step 5 : Insert New Records")

print("Step 6 : Commit Changes Atomically")

print("=" * 70)

# COMMAND ----------

# MAGIC %md
# MAGIC ## MERGE Decision Logic
# MAGIC
# MAGIC For every incoming record:
# MAGIC
# MAGIC - If the patient already exists → Update the existing record.
# MAGIC - If the patient is new → Insert a new record.
# MAGIC
# MAGIC This minimizes processing time and avoids reloading the complete dataset.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Preparing the Source Batch
# MAGIC
# MAGIC To demonstrate Delta Lake MERGE, a small incoming batch is created.
# MAGIC
# MAGIC This batch represents new or updated patient records that need to be synchronized with the Silver table.

# COMMAND ----------

print(globals().keys())

# COMMAND ----------

print(globals().keys())

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

incremental_df = (
    silver_df
        .limit(5)
        .withColumn("processed_timestamp", current_timestamp())
)

display(incremental_df)

# COMMAND ----------

from pyspark.sql.functions import col

updated_batch_df = (
    incremental_df
        .withColumn(
            "Billing_Amount",
            col("Billing_Amount") + 5000
        )
)

display(updated_batch_df)

# COMMAND ----------

merge_source_df = updated_batch_df

display(merge_source_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Existing Silver Data
# MAGIC
# MAGIC The Silver table represents the cleaned and validated healthcare records.
# MAGIC
# MAGIC The incoming batch will be compared against this dataset during the MERGE process.

# COMMAND ----------

display(
    silver_df.select(
        "Name",
        "Billing_Amount",
        "Medical_Condition"
    ).limit(5)
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Incoming Incremental Batch
# MAGIC
# MAGIC The following records represent newly arrived or updated healthcare data that needs to be synchronized with the Silver table.

# COMMAND ----------

display(
    merge_source_df.select(
        "Name",
        "Billing_Amount",
        "Medical_Condition"
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Delta Lake MERGE Logic
# MAGIC
# MAGIC During the MERGE operation:
# MAGIC
# MAGIC - Existing records are updated.
# MAGIC - New records are inserted.
# MAGIC - Delta Lake performs both actions in a single ACID transaction.
# MAGIC
# MAGIC This approach avoids full table reloads and supports efficient incremental processing.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Benefits of Delta Lake MERGE
# MAGIC
# MAGIC - Processes only new or changed records
# MAGIC - Reduces processing time
# MAGIC - Avoids full data reloads
# MAGIC - Supports ACID transactions
# MAGIC - Enables scalable incremental pipelines

# COMMAND ----------

# MAGIC %md
# MAGIC # Summary
# MAGIC
# MAGIC This notebook demonstrated:
# MAGIC
# MAGIC - Reading the Silver table
# MAGIC - Simulating an incremental batch
# MAGIC - Preparing updated records
# MAGIC - Understanding Delta Lake MERGE
# MAGIC - Incremental processing concepts
# MAGIC
# MAGIC In production, this workflow would process only newly arrived or modified healthcare records, improving performance and scalability.