from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def run_etl():
    spark = SparkSession.builder \
        .appName("SimpleETL") \
        .master("local[*]") \
        .getOrCreate()

    # Read CSV
    df = spark.read.csv("data/raw.csv", header=True, inferSchema=True)

    # Transform: Keep only adults
    df_filtered = df.filter(col("age") >= 18)

    # Transform: Increase salary by 10%
    df_transformed = df_filtered.withColumn(
        "salary",
        col("salary") * 1.1
    )

    # Save output
    df_transformed.write.mode("overwrite").csv(
        "data/processed.csv",
        header=True
    )

    spark.stop()

if __name__ == "__main__":
    run_etl()
