from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, to_date

spark = SparkSession.builder \
    .appName("Ecommerce_ETL") \
    .getOrCreate()

# -----------------------
# 1️⃣ EXTRACT
# -----------------------

orders = spark.read.csv("orders.csv", header=True, inferSchema=True)
customers = spark.read.csv("customers.csv", header=True, inferSchema=True)
products = spark.read.csv("products.csv", header=True, inferSchema=True)

# -----------------------
# 2️⃣ TRANSFORM
# -----------------------

# Clean null quantities
orders = orders.fillna({"quantity": 1})

# Convert order_date to date type
orders = orders.withColumn("order_date", to_date("order_date"))

# Join with customers
df = orders.join(customers, "customer_id", "left")

# Join with products
df = df.join(products, "product_id", "left")

# Calculate total amount
df = df.withColumn("total_amount", col("quantity") * col("price"))

# -----------------------
# 3️⃣ BUSINESS AGGREGATION
# -----------------------

# Total revenue per city
revenue_by_city = df.groupBy("city") \
    .agg(sum("total_amount").alias("total_revenue"))

revenue_by_city.show()

# -----------------------
# 4️⃣ LOAD (Write Output)
# -----------------------

df.write.mode("overwrite").parquet("output/clean_orders")
revenue_by_city.write.mode("overwrite").parquet("output/revenue_by_city")

spark.stop()
