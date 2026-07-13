# Databricks notebook source


# COMMAND ----------

# MAGIC %md
# MAGIC # Gold Layer
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC This notebook creates business-ready analytical datasets from the Silver layer.
# MAGIC
# MAGIC The Gold layer contains aggregated data optimized for reporting, dashboards, and business decision-making.

# COMMAND ----------

# MAGIC %md
# MAGIC # Read Silver Layer
# MAGIC
# MAGIC Load the trusted Silver Delta Table before creating Gold analytical datasets.

# COMMAND ----------

# ==========================================
# Configuration
# ==========================================

CATALOG = "workspace"
SCHEMA = "healthcare"

SILVER_TABLE = f"{CATALOG}.{SCHEMA}.silver_patient_records"

print("Reading from:", SILVER_TABLE)

# COMMAND ----------

gold_df = spark.table(SILVER_TABLE)

display(gold_df)

# COMMAND ----------

from pyspark.sql.functions import *

patient_summary = (
    gold_df
    .agg(
        count("*").alias("total_patients"),
        avg("Age").alias("average_age"),
        sum("Billing_Amount").alias("total_billing"),
        avg("Billing_Amount").alias("average_billing")
    )
)

display(patient_summary)

# COMMAND ----------

patient_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.healthcare.gold_patient_summary")

# COMMAND ----------

display(
    spark.table("workspace.healthcare.gold_patient_summary")
)

# COMMAND ----------

from pyspark.sql.functions import *

hospital_summary = (
    gold_df
    .groupBy("Hospital")
    .agg(
        count("*").alias("total_patients"),
        sum("Billing_Amount").alias("total_billing"),
        avg("Billing_Amount").alias("average_billing")
    )
    .orderBy(desc("total_patients"))
)

display(hospital_summary)

# COMMAND ----------

hospital_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.healthcare.gold_hospital_summary")

# COMMAND ----------

display(
    spark.table("workspace.healthcare.gold_hospital_summary")
)

# COMMAND ----------

condition_summary = (
    gold_df
    .groupBy("Medical_Condition")
    .agg(
        count("*").alias("patient_count"),
        avg("Billing_Amount").alias("average_billing")
    )
    .orderBy(desc("patient_count"))
)

display(condition_summary)

# COMMAND ----------

condition_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.healthcare.gold_medical_condition_summary")

# COMMAND ----------

insurance_summary = (
    gold_df
    .groupBy("Insurance_Provider")
    .agg(
        count("*").alias("patient_count"),
        sum("Billing_Amount").alias("total_billing")
    )
    .orderBy(desc("patient_count"))
)

display(insurance_summary)

# COMMAND ----------

insurance_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.healthcare.gold_insurance_summary")

# COMMAND ----------

billing_summary = (
    gold_df
    .agg(
        sum("Billing_Amount").alias("total_billing"),
        avg("Billing_Amount").alias("average_billing"),
        max("Billing_Amount").alias("highest_bill"),
        min("Billing_Amount").alias("lowest_bill")
    )
)

display(billing_summary)

# COMMAND ----------

billing_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.healthcare.gold_billing_summary")

# COMMAND ----------

# MAGIC %md
# MAGIC # Gold Layer Summary
# MAGIC
# MAGIC ## Completed Gold Tables
# MAGIC
# MAGIC - Patient Summary
# MAGIC - Hospital Summary
# MAGIC - Medical Condition Summary
# MAGIC - Insurance Summary
# MAGIC - Billing Summary
# MAGIC
# MAGIC These tables are optimized for reporting, dashboards, and business analytics.

# COMMAND ----------

# MAGIC %md
# MAGIC # Hospital Ranking
# MAGIC
# MAGIC This Gold table ranks hospitals based on total revenue generated and patient count.
# MAGIC
# MAGIC The table is intended for executive reporting and dashboarding.

# COMMAND ----------

# Silver Table Name
SILVER_TABLE = "workspace.healthcare.silver_patient_records"

# Read Silver Table
silver_df = spark.table(SILVER_TABLE)

display(silver_df)

# COMMAND ----------

from pyspark.sql.functions import sum, count, dense_rank
from pyspark.sql.window import Window

# Create Hospital Ranking Table
hospital_ranking_df = (
    silver_df
    .groupBy("Hospital")
    .agg(
        count("*").alias("Patient_Count"),
        sum("Billing_Amount").alias("Total_Revenue")
    )
)

# Rank hospitals by revenue
window_spec = Window.orderBy(hospital_ranking_df["Total_Revenue"].desc())

hospital_ranking_df = (
    hospital_ranking_df
    .withColumn(
        "Hospital_Rank",
        dense_rank().over(window_spec)
    )
)

display(hospital_ranking_df)

# COMMAND ----------

hospital_ranking_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.healthcare.gold_hospital_ranking")

# COMMAND ----------

display(
    spark.table("workspace.healthcare.gold_hospital_ranking")
)

# COMMAND ----------

# MAGIC %md
# MAGIC # Executive Dashboard Summary
# MAGIC
# MAGIC This Gold table stores key business KPIs required by management dashboards.
# MAGIC
# MAGIC The summary table provides quick access to important healthcare metrics without scanning the complete dataset.

# COMMAND ----------

from pyspark.sql.functions import (
    count,
    countDistinct,
    sum,
    avg,
    max,
    first
)

dashboard_summary_df = (
    silver_df
    .agg(
        count("*").alias("Total_Patients"),
        countDistinct("Hospital").alias("Total_Hospitals"),
        countDistinct("Doctor").alias("Total_Doctors"),
        sum("Billing_Amount").alias("Total_Revenue"),
        avg("Billing_Amount").alias("Average_Billing"),
        avg("Age").alias("Average_Age")
    )
)

display(dashboard_summary_df)

# COMMAND ----------

dashboard_summary_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.healthcare.gold_dashboard_summary")

# COMMAND ----------

display(
    spark.table("workspace.healthcare.gold_dashboard_summary")
)

# COMMAND ----------

most_common_condition = (
    silver_df
    .groupBy("Medical_Condition")
    .count()
    .orderBy("count", ascending=False)
    .limit(1)
)

display(most_common_condition)

# COMMAND ----------

top_insurance_provider = (
    silver_df
    .groupBy("Insurance_Provider")
    .count()
    .orderBy("count", ascending=False)
    .limit(1)
)

display(top_insurance_provider)

# COMMAND ----------

most_common_blood_type = (
    silver_df
    .groupBy("Blood_Type")
    .count()
    .orderBy("count", ascending=False)
    .limit(1)
)

display(most_common_blood_type)

# COMMAND ----------

from pyspark.sql.functions import countDistinct

insurance_provider_count = (
    silver_df
    .agg(
        countDistinct("Insurance_Provider").alias("Total_Insurance_Providers")
    )
)

display(insurance_provider_count)

# COMMAND ----------

silver_df = spark.table(SILVER_TABLE)