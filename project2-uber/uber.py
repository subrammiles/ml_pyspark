from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, to_timestamp, hour, sum, avg,
    count, rank, when
)
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("RideSharing_ETL") \
    .getOrCreate()

# ------------------------
# 1️⃣ EXTRACT
# ------------------------

df = spark.read.csv("trips.csv", header=True, inferSchema=True)

# ------------------------
# 2️⃣ CLEANING
# ------------------------

# Remove trips with null distance
df = df.filter(col("distance_km").isNotNull())

# Convert timestamps
df = df.withColumn("start_time", to_timestamp("start_time")) \
       .withColumn("end_time", to_timestamp("end_time"))

# Extract hour
df = df.withColumn("start_hour", hour("start_time"))

# ------------------------
# 3️⃣ TRANSFORMATIONS
# ------------------------

# Revenue per city
revenue_city = df.groupBy("city") \
    .agg(sum("fare_amount").alias("total_revenue"))

# Driver performance
driver_metrics = df.groupBy("driver_id") \
    .agg(
        count("trip_id").alias("total_trips"),
        sum("fare_amount").alias("total_earnings"),
        avg("rating").alias("avg_rating")
    )

# ------------------------
# 4️⃣ WINDOW FUNCTION
# ------------------------

window_spec = Window.orderBy(col("total_earnings").desc())

top_drivers = driver_metrics.withColumn(
    "rank",
    rank().over(window_spec)
)

# ------------------------
# 5️⃣ Peak Hour Detection
# ------------------------

peak_hours = df.groupBy("start_hour") \
    .agg(count("trip_id").alias("trip_count")) \
    .orderBy(col("trip_count").desc())

# ------------------------
# 6️⃣ ADD BONUS LOGIC
# ------------------------

# Classify drivers
driver_metrics = driver_metrics.withColumn(
    "performance_level",
    when(col("avg_rating") >= 4.5, "Excellent")
    .when(col("avg_rating") >= 4, "Good")
    .otherwise("Average")
)

# ------------------------
# 7️⃣ LOAD (Partitioned Parquet)
# ------------------------

df.write.mode("overwrite") \
    .partitionBy("city") \
    .parquet("output/trips_cleaned")

driver_metrics.write.mode("overwrite") \
    .parquet("output/driver_metrics")

revenue_city.write.mode("overwrite") \
    .parquet("output/revenue_by_city")

peak_hours.write.mode("overwrite") \
    .parquet("output/peak_hours")

spark.stop()
