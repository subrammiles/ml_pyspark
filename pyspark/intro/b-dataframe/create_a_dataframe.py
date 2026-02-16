from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EndSessionExample") \
    .getOrCreate()



df = spark.createDataFrame(
    [("Alice", 25), ("Bob", 30)],
    ["Name", "Age"]
)

df.show()

spark.stop()


