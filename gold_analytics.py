
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    count,
    sum as spark_sum,
    round as spark_round
)

# Gold Layer - Banking Analytics
# Synthetic data demonstration


def main():
    spark = (
        SparkSession.builder
        .appName("AzureLakehouseGold")
        .getOrCreate()
    )

    # Read validated Silver transactions
    silver_df = spark.read.parquet(
        "data/silver/transactions"
    )

    # Include only completed transactions
    completed_df = silver_df.filter(
        col("status") == "COMPLETED"
    )

    # Calculate customer-level KPIs
    gold_df = (
        completed_df
        .groupBy("customer_id")
        .agg(
            count("transaction_id").alias(
                "total_transactions"
            ),
            spark_round(
                spark_sum("amount"), 2
            ).alias("total_amount")
        )
        .orderBy("customer_id")
    )

    # Store analytics-ready data
    gold_df.write.mode("overwrite").parquet(
        "data/gold/customer_analytics"
    )

    print("Gold analytics completed")
    gold_df.show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()
