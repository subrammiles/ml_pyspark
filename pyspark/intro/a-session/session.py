from pyspark.sql import SparkSession

print("Spark started")

spark = SparkSession.builder \
    .appName("BasicExamples") \
    .getOrCreate()

spark.stop()

print("Spark stopped")