# Databricks notebook source
# MAGIC %md
# MAGIC # Data Governance and Security
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Healthcare data contains highly sensitive patient information that must be protected.
# MAGIC
# MAGIC Databricks provides enterprise-grade governance through Unity Catalog, Role-Based Access Control (RBAC), auditing, and centralized data management.
# MAGIC
# MAGIC This notebook introduces the governance concepts applicable to the Healthcare Data Pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC ## What is Data Governance?
# MAGIC
# MAGIC Data Governance is the process of managing data securely, consistently, and responsibly throughout its lifecycle.
# MAGIC
# MAGIC Its primary objectives include:
# MAGIC
# MAGIC - Data Security
# MAGIC - Data Quality
# MAGIC - Access Control
# MAGIC - Regulatory Compliance
# MAGIC - Data Lineage
# MAGIC - Metadata Management
# MAGIC
# MAGIC Strong governance ensures that only authorized users can access sensitive healthcare information.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Unity Catalog
# MAGIC
# MAGIC Unity Catalog is Databricks' centralized governance solution.
# MAGIC
# MAGIC It provides:
# MAGIC
# MAGIC - Centralized metadata management
# MAGIC - Fine-grained access control
# MAGIC - Data lineage
# MAGIC - Table and volume management
# MAGIC - Secure data sharing
# MAGIC
# MAGIC In this project, Unity Catalog is used to organize healthcare data into Bronze, Silver, and Gold layers.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Role-Based Access Control (RBAC)
# MAGIC
# MAGIC Role-Based Access Control restricts data access according to user responsibilities.
# MAGIC
# MAGIC Example roles include:
# MAGIC
# MAGIC - Data Engineer
# MAGIC - Data Analyst
# MAGIC - Data Scientist
# MAGIC - Business Analyst
# MAGIC - Administrator
# MAGIC
# MAGIC Each role receives only the permissions required to perform its tasks.

# COMMAND ----------

print("=" * 70)

print("ROLE-BASED ACCESS CONTROL")

print("=" * 70)

roles = [
    "Administrator",
    "Data Engineer",
    "Data Scientist",
    "Data Analyst",
    "Business User"
]

for role in roles:
    print("✓", role)

print("=" * 70)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Lineage
# MAGIC
# MAGIC Data Lineage tracks the complete journey of data.
# MAGIC
# MAGIC Healthcare CSV
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
# MAGIC Data Lineage improves transparency, auditing, troubleshooting, and regulatory compliance.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Security Best Practices
# MAGIC
# MAGIC Healthcare data should be protected using:
# MAGIC
# MAGIC - Encryption at Rest
# MAGIC - Encryption in Transit
# MAGIC - Access Control
# MAGIC - Data Masking
# MAGIC - Audit Logging
# MAGIC - Secure Authentication
# MAGIC - Principle of Least Privilege
# MAGIC
# MAGIC These practices help organizations comply with healthcare regulations and protect sensitive patient information.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Healthcare Compliance
# MAGIC
# MAGIC Healthcare organizations must comply with regulations designed to protect patient data.
# MAGIC
# MAGIC Common compliance frameworks include:
# MAGIC
# MAGIC - HIPAA (United States)
# MAGIC - GDPR (European Union)
# MAGIC - Local healthcare privacy regulations
# MAGIC
# MAGIC A governed data platform helps organizations satisfy these compliance requirements.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Why Data Governance Matters
# MAGIC
# MAGIC Without governance:
# MAGIC
# MAGIC - Sensitive data may be exposed
# MAGIC - Duplicate datasets may be created
# MAGIC - Data quality decreases
# MAGIC - Regulatory compliance becomes difficult
# MAGIC
# MAGIC Databricks Unity Catalog provides centralized governance that enables secure and reliable data engineering workflows.

# COMMAND ----------

# MAGIC %md
# MAGIC # Summary
# MAGIC
# MAGIC This notebook introduced enterprise data governance concepts used in modern healthcare data platforms.
# MAGIC
# MAGIC Key topics covered include:
# MAGIC
# MAGIC - Unity Catalog
# MAGIC - RBAC
# MAGIC - Data Lineage
# MAGIC - Data Security
# MAGIC - Healthcare Compliance
# MAGIC - Governance Best Practices
# MAGIC
# MAGIC These concepts complement the Medallion Architecture and ensure that healthcare data remains secure, traceable, and compliant.