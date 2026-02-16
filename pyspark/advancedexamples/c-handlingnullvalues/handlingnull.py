from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Alice", 10),
    (2, "Bob", None),
    (3, "Cathy", 20),
    (4, "David", None)
]

df_emp = spark.createDataFrame(data, ["emp_id", "name", "dept_id"])
df_filled = df_emp.fillna({"dept_id": 999})
df_filled.show()

