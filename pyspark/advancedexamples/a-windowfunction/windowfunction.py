from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("AdvancedExamples").getOrCreate()

data = [
    ("HR", "Alice", 5000),
    ("HR", "Cathy", 6000),
    ("IT", "Bob", 7000),
    ("IT", "David", 6500)
]

df = spark.createDataFrame(data, ["Department", "Name", "Salary"])

window_spec = Window.partitionBy("Department").orderBy(col("Salary").desc())

df.withColumn("Rank", rank().over(window_spec)).show()
