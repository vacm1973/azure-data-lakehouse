# Azure Data Lakehouse Architecture

**PySpark | Azure Databricks | Medallion Architecture | Data Engineering | CI/CD**

## Project Overview

This portfolio project demonstrates a data processing pipeline based on the Medallion Architecture (Bronze, Silver, and Gold).

It showcases data ingestion, transformation, quality validation, and analytics using PySpark and synthetic banking transaction data.

The implementation runs locally with Apache Spark and is designed as a foundation for an Azure Databricks and Azure Data Lake Storage solution.

**All data is fictional. No confidential or proprietary information is used.**

## Architecture

**Bronze → Silver → Gold**

### Bronze Layer — Data Ingestion

File: `bronze_ingestion.py`

- Creates synthetic banking transaction records.
- Adds ingestion timestamps and source metadata.
- Stores raw transaction data in Parquet format.

### Silver Layer — Data Transformation

File: `silver_transformation.py`

- Reads data from the Bronze layer.
- Standardizes transaction statuses.
- Validates transaction identifiers and amounts.
- Filters invalid records.
- Removes duplicate transaction identifiers.
- Writes validated data to the Silver layer.

### Gold Layer — Business Analytics

File: `gold_analytics.py`

- Reads validated Silver data.
- Filters completed transactions.
- Aggregates transaction counts by customer.
- Calculates total transaction amounts.
- Produces analytics-ready datasets in Parquet format.

## Technology Stack

- Python 3.11
- Apache Spark / PySpark 3.5.3
- Parquet
- GitHub Actions
- Java 17
- Medallion Architecture

**Azure deployment targets:** Azure Databricks and Azure Data Lake Storage (ADLS Gen2).

These Azure services are architectural targets; the current implementation has been validated using a GitHub-hosted environment, not deployed to Azure.

## Repository Structure

```text
azure-data-lakehouse/
├── bronze_ingestion.py
├── silver_transformation.py
├── gold_analytics.py
├── README.md
└── .github/
    └── workflows/
        └── lakehouse-tests.yml
```

## Running the Pipeline

Install Python 3.11, Java 17, and PySpark 3.5.3.

```bash
pip install pyspark==3.5.3
```

Run the three layers in sequence:

```bash
python bronze_ingestion.py
python silver_transformation.py
python gold_analytics.py
```

The pipeline writes Parquet datasets to local directories under `data/bronze`, `data/silver`, and `data/gold`.

## Automated Validation

GitHub Actions runs the complete Bronze → Silver → Gold pipeline and verifies the Gold-layer output.

The workflow includes:

- Automated environment setup
- PySpark installation
- Sequential execution of all three layers
- Validation of customer-level analytics results

**Validation status: Passed in GitHub Actions.**

## Future Enhancements

- Integration with Azure Data Lake Storage Gen2
- Deployment to Azure Databricks
- Delta Lake support
- Incremental data ingestion
- Additional data quality rules
- Pipeline monitoring and orchestration

## About the Author

**Victor Andres Costa Molina**

Senior Data Engineer | Business Intelligence | Data Architecture

Experienced in enterprise data engineering, cloud data platforms, complex data migrations, ETL/ELT, and business intelligence solutions.

**Location:** Buenos Aires, Argentina

**Open to:** Remote Senior Data Engineering, Data Architecture, and BI Engineering opportunities.
