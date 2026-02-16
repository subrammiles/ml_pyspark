from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("AdvancedExamples").getOrCreate()

employees = [
    (1, "Alice", 101),
    (2, "Bob", 102),
    (3, "Cathy", 103),
    (4, "David", None)
]

departments = [
    (101, "HR"),
    (102, "IT"),
    (104, "Finance")
]

df_emp = spark.createDataFrame(employees, ["emp_id", "name", "dept_id"])
df_dept = spark.createDataFrame(departments, ["dept_id", "dept_name"])

# Left Join
df_join = df_emp.join(df_dept, on="dept_id", how="left")
df_join.show()
