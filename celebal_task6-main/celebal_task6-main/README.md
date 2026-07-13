# Apache Spark - Week 6 Assignment

## Overview

This assignment focuses on learning the fundamentals of Apache Spark and implementing basic data processing tasks using PySpark. It covers Spark architecture, DataFrame operations, schema management, filtering, transformations, and working with different storage formats.

## Tools and Environment

- Python
- PySpark
- Apache Spark
- Google Colab

## Work Completed

- Studied the core components of Spark architecture.
- Explored Lazy Evaluation and DAG execution.
- Imported datasets from CSV and Parquet files.
- Performed DataFrame operations such as filtering and column selection.
- Renamed columns and converted data types where required.
- Created new calculated columns.
- Removed records containing null values.
- Compared the performance of CSV and Parquet file formats.
- Implemented a complete data pipeline from reading data to saving the processed output.

## Key Learnings

- Spark delays execution until an action is called, which helps optimize the execution plan.
- The DAG keeps track of all transformations, allowing Spark to recover data if a failure occurs.
- Parquet is more efficient than CSV because it is a compressed columnar storage format.
- Proper filtering and schema handling improve the overall performance of Spark applications.
- Functions like `show()` are better suited for previewing large datasets than `collect()`, which loads all data into the Driver.

## Conclusion

The assignment provided practical experience with Spark DataFrames and common data processing operations. It also demonstrated how Spark optimizes execution using lazy evaluation and efficient storage formats, making it suitable for handling large-scale datasets.
