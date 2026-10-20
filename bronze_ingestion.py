from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit

# Azure Lakehouse - Bronze Layer
# Synthetic transaction data for portfolio demonstration

def main():
    spark = (
        SparkSession.builder
        .appName("AzureLakehouseBronze")
        .getOrCreate()
    )

    data = [
        (1001, 1, 1500.00, "COMPLETED"),
        (1002, 2, 250.00, "COMPLETED"),
        (1003, 1, 750.00, "COMPLETED"),
        (1004, 3, 3200.00, "COMPLETED"),
        (1005, 4, 400.00, "FAILED"),
    ]

    columns = [
        "transaction_id",
        "customer_id",
        "amount",
        "status",
    ]

    df = spark.createDataFrame(data, columns)

    bronze_df = (
        df.withColumn("ingestion_timestamp", current_timestamp())
          .withColumn("source_system", lit("synthetic_banking"))
    )

    bronze_df.write.mode("overwrite").parquet("data/bronze/transactions")

    print("Bronze ingestion completed")
    print(f"Records ingested: {bronze_df.count()}")

    spark.stop()


if __name__ == "__main__":
    main()
