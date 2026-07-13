# Databricks notebook source
# MAGIC %md
# MAGIC # Business Analytics
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC This notebook performs business analysis using the Gold Layer tables.
# MAGIC
# MAGIC The analysis helps healthcare management understand patient trends, hospital performance, insurance coverage, and billing insights.

# COMMAND ----------

CATALOG = "workspace"
SCHEMA = "healthcare"

print("Healthcare Business Analytics Started")

# COMMAND ----------

display(spark.sql("""

SELECT *
FROM workspace.healthcare.gold_patient_summary

"""))

# COMMAND ----------

display(spark.sql("""

SELECT
Hospital,
total_patients,
total_billing

FROM workspace.healthcare.gold_hospital_summary

ORDER BY total_patients DESC
LIMIT 10

"""))

# COMMAND ----------

display(spark.sql("""

SELECT
Medical_Condition,
patient_count

FROM workspace.healthcare.gold_medical_condition_summary

ORDER BY patient_count DESC

"""))

# COMMAND ----------

display(spark.sql("""

SELECT
Insurance_Provider,
patient_count,
total_billing

FROM workspace.healthcare.gold_insurance_summary

ORDER BY patient_count DESC

"""))

# COMMAND ----------

display(spark.sql("""

SELECT *

FROM workspace.healthcare.gold_billing_summary

"""))

# COMMAND ----------

display(

spark.sql("""

SELECT

Admission_Type,

ROUND(AVG(Billing_Amount),2) AS Average_Billing,

COUNT(*) AS Total_Patients

FROM workspace.healthcare.silver_patient_records

GROUP BY Admission_Type

ORDER BY Average_Billing DESC

""")

)

# COMMAND ----------

display(

spark.sql("""

SELECT

Gender,

COUNT(*) AS Total_Patients

FROM workspace.healthcare.silver_patient_records

GROUP BY Gender

ORDER BY Total_Patients DESC

""")

)

# COMMAND ----------

display(

spark.sql("""

SELECT

Medical_Condition,

ROUND(AVG(Billing_Amount),2) AS Average_Billing

FROM workspace.healthcare.silver_patient_records

GROUP BY Medical_Condition

ORDER BY Average_Billing DESC

""")

)

# COMMAND ----------

display(

spark.sql("""

SELECT

Doctor,

COUNT(*) AS Total_Patients

FROM workspace.healthcare.silver_patient_records

GROUP BY Doctor

ORDER BY Total_Patients DESC

LIMIT 10

""")

)

# COMMAND ----------

display(

spark.sql("""

SELECT

Insurance_Provider,

SUM(Billing_Amount) AS Total_Revenue

FROM workspace.healthcare.silver_patient_records

GROUP BY Insurance_Provider

ORDER BY Total_Revenue DESC

LIMIT 10

""")

)

# COMMAND ----------

# MAGIC %md
# MAGIC # Business Analytics Completed
# MAGIC
# MAGIC The Healthcare Data Pipeline successfully transformed raw healthcare data into business-ready analytical datasets using the Medallion Architecture.
# MAGIC
# MAGIC The generated Gold Layer supports reporting, dashboard creation, and decision-making for healthcare stakeholders.