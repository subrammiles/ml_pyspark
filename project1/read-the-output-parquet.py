from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ReadParquet") \
    .getOrCreate()

df = spark.read.parquet("output/clean_orders")

df.show()
df.printSchema()


# Important: Parquet Is a Folder, Not a Single File

# When Spark writes Parquet, it creates a folder like this:

# output/
#    clean_orders/
#        part-00000-xxxxx.snappy.parquet
#        part-00001-xxxxx.snappy.parquet
#        _SUCCESS


# You must read the folder, not individual part files.