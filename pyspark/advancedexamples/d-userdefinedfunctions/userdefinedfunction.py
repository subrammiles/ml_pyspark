from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.sql.functions import col
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("AdvancedExamples").getOrCreate()

data = [
    ("HR", "Alice", 5000),
    ("HR", "Cathy", 6000),
    ("IT", "Bob", 7000),
    ("IT", "David", 6500)
]

def salary_category(salary):
    if salary >= 7000:
        return "High"
    elif salary >= 6000:
        return "Medium"
    else:
        return "Low"

salary_udf = udf(salary_category, StringType())

df = spark.createDataFrame(data, ["Department", "Name", "Salary"])

df.withColumn("Category", salary_udf(col("Salary"))).show()
