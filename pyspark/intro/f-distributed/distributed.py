

from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("EndSessionExample") \
    .getOrCreate()

df = spark.read.csv("data.csv")

x=df.rdd.getNumPartitions()

print(x)

spark.stop()





