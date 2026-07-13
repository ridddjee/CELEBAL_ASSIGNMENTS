# Databricks notebook source
# MAGIC %md
# MAGIC # Export Gold Layer for Power BI
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC This notebook exports the Gold Layer tables into CSV format.
# MAGIC
# MAGIC These exported datasets will be used to build an interactive Power BI dashboard for business reporting and visualization.
# MAGIC
# MAGIC The Gold Layer contains business-ready analytical datasets generated from the Healthcare Data Pipeline.

# COMMAND ----------

EXPORT_PATH = "/Volumes/workspace/healthcare/raw_data/powerbi_exports"

dbutils.fs.mkdirs(EXPORT_PATH)

print("Export folder created successfully.")

# COMMAND ----------

hospital_df = spark.table("workspace.healthcare.gold_hospital_ranking")

(
    hospital_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(f"{EXPORT_PATH}/hospital_ranking")
)

print("Hospital Ranking exported successfully.")

# COMMAND ----------

spark.sql("""
SHOW TABLES IN workspace.healthcare
""").display()

# COMMAND ----------

display(spark.sql("SHOW TABLES IN workspace.healthcare"))

# COMMAND ----------

insurance_df = spark.table("workspace.healthcare.gold_insurance_summary")

(
    insurance_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(f"{EXPORT_PATH}/insurance_summary")
)

print("Insurance Summary exported successfully.")

# COMMAND ----------

billing_df = spark.table("workspace.healthcare.gold_billing_summary")

(
    billing_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(f"{EXPORT_PATH}/billing_summary")
)

print("Billing Summary exported successfully.")

# COMMAND ----------

patient_df = spark.table("workspace.healthcare.gold_patient_summary")

(
    patient_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(f"{EXPORT_PATH}/patient_summary")
)

print("Patient Summary exported successfully.")

# COMMAND ----------

hospital_summary_df = spark.table("workspace.healthcare.gold_hospital_summary")

(
    hospital_summary_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(f"{EXPORT_PATH}/hospital_summary")
)

print("Hospital Summary exported successfully.")

# COMMAND ----------

condition_df = spark.table("workspace.healthcare.gold_medical_condition_summary")

(
    condition_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(f"{EXPORT_PATH}/medical_condition_summary")
)

print("Medical Condition Summary exported successfully.")

# COMMAND ----------

dashboard_df = spark.table("workspace.healthcare.gold_dashboard_summary")

(
    dashboard_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(f"{EXPORT_PATH}/dashboard_summary")
)

print("Dashboard Summary exported successfully.")

# COMMAND ----------

display(dbutils.fs.ls(EXPORT_PATH))

# COMMAND ----------

EXPORT_PATH = "/Volumes/workspace/healthcare/raw_data/powerbi_exports"

dbutils.fs.mkdirs(EXPORT_PATH)

print(EXPORT_PATH)

# COMMAND ----------

dashboard_df = spark.table("workspace.healthcare.gold_dashboard_summary")

(
    dashboard_df
    .coalesce(1)
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(f"{EXPORT_PATH}/dashboard_summary")
)

print("Dashboard Summary exported successfully.")

# COMMAND ----------

display(dbutils.fs.ls(f"{EXPORT_PATH}/dashboard_summary"))