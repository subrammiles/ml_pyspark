

from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("EndSessionExample") \
    .getOrCreate()

df = spark.read.csv("data.csv")
df.show()
spark.stop()





