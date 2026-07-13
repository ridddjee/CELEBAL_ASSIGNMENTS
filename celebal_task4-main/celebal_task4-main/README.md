# Azure Data Pipeline Development with Azure Data Factory

## 📖 Project Summary

This project showcases the design and implementation of a cloud-based data integration workflow using Microsoft Azure services. The solution leverages Azure Blob Storage and Azure Data Factory (ADF) to automate data movement, validate file metadata, and transfer datasets between storage locations in a secure and scalable manner.

---

## 🎯 Project Goals

The primary objectives of this project were:

- Gain hands-on experience with Azure cloud services.
- Configure and manage Azure Storage resources.
- Develop an automated data pipeline using Azure Data Factory.
- Validate source file information before processing.
- Perform data movement between Azure Blob Storage containers.
- Monitor and verify successful pipeline execution.

---

## 🏛️ Solution Architecture

```text
Source Blob Container
        │
        ▼
Superstore Dataset (CSV)
        │
        ▼
Azure Data Factory Pipeline
 ├── Storage Linked Service
 ├── Source Dataset
 ├── Metadata Validation
 ├── Data Copy Activity
 └── Destination Dataset
        │
        ▼
Destination Blob Container
        │
        ▼
Processed Output File
```

---

## 🔧 Azure Services Utilized

- Azure Resource Group
- Azure Storage Account
- Azure Blob Storage
- Azure Data Factory (ADF)

---

## ⚙️ Project Implementation

### Step 1: Environment Setup
Created a dedicated Azure Resource Group to organize and manage all project resources.

### Step 2: Storage Configuration
Provisioned an Azure Storage Account and enabled Blob Storage services.

### Step 3: Container Management
Configured two separate Blob Containers:
- Source Container
- Destination Container

### Step 4: Data Ingestion
Uploaded the Superstore CSV dataset to the source container.

### Step 5: Azure Data Factory Deployment
Created an Azure Data Factory instance to orchestrate the data integration workflow.

### Step 6: Storage Connectivity
Established connectivity between Azure Data Factory and Blob Storage through a Linked Service.

### Step 7: Dataset Definition
Defined:
- Source Dataset (`DS_Source`)
- Destination Dataset (`DS_Destination`)

### Step 8: Metadata Inspection
Implemented a **Get Metadata** activity to retrieve and validate:
- File availability
- File size
- Last modification details

### Step 9: Data Movement
Configured a **Copy Data** activity to transfer the dataset from the source container to the destination container.

### Step 10: Pipeline Monitoring
Executed the pipeline and monitored activity status through Azure Data Factory's monitoring interface.

### Step 11: Output Validation
Confirmed successful generation of the output file within the destination container.

---

## 🔄 Pipeline Execution Flow

```text
Source CSV File
      │
      ▼
Get Metadata
      │
      ▼
Copy Data
      │
      ▼
Destination Storage
```

---

## 📊 Project Outcomes

- Successfully connected Azure Data Factory with Azure Blob Storage.
- Retrieved and validated source file metadata.
- Automated dataset transfer between storage containers.
- Generated the output file successfully in the destination location.
- Achieved successful pipeline execution without errors.

---

## 📁 Deliverables

| Item | Description |
|--------|-------------|
| Source Dataset | Sample - Superstore.csv |
| Output Dataset | Superstore_Output.csv |
| Source Storage | ceicontainer |
| Destination Storage | ceidestinationcontainer |
| Pipeline | PL_Superstore |
| Execution Status | Successful |

---

## 📚 Key Learnings

Through this project, the following concepts were explored and implemented:

- Azure Resource Management
- Blob Storage Operations
- Azure Data Factory Configuration
- Linked Services and Dataset Management
- Metadata Extraction and Validation
- Cloud Data Integration Workflows
- Pipeline Monitoring and Execution Tracking

---

## ✅ Conclusion

The project successfully implemented an end-to-end data integration pipeline using Azure Data Factory and Azure Blob Storage. By incorporating metadata validation and automated data transfer, the solution demonstrates how Azure services can be used to build reliable, scalable, and efficient cloud-based data processing workflows. The successful execution of the pipeline and generation of the output file validate the effectiveness of the implemented architecture.
