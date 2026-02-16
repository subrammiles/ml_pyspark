from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EndSessionExample") \
    .getOrCreate()

data = [
    ("Alice", "HR", 5000),
    ("Bob", "IT", 6000),
    ("Cathy", "HR", 5500),
    ("David", "IT", 7000)
]

columns = ["Name", "Department", "Salary"]

df_emp = spark.createDataFrame(data, columns)

df_emp.groupBy("Department").avg("Salary").show()

df_emp.filter(df_emp.Salary > 5000).show()



# uSING sql IN PYSPARK
df_emp.createOrReplaceTempView("emp")
result = spark.sql("SELECT * FROM emp WHERE Salary < 6000")
result.show()

spark.stop()


