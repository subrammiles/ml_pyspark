# Data frame

A DataFrame is a distributed table of data with rows and columns.It  is Spark’s structured way of storing and processing large-scale tabular data.

It looks like an Excel sheet or SQL table.

Example:

Name	Age
Alice	25
Bob	    30

df = spark.createDataFrame(
    [("Alice", 25), ("Bob", 30)],
    ["Name", "Age"]
)
In PySpark ,Everything revolves around DataFrames.If you understand DataFrames well → you understand 70% of Spark.


# what it contains
A DataFrame contains:

(i).Data

(ii).Schema (column names + types)

(iii).Execution plan

# 🏗 Why Do We Create a DataFrame?

Because Spark processes data using DataFrames.
We create them to:
✅ Store structured data
✅ Perform transformations
✅ Filter rows
✅ Aggregate data
✅ Join tables
✅ Run SQL queries
✅ Handle large datasets


🚀 Why Not Just Use Python Lists?

Good question.
Python list:
data = [("Alice", 25), ("Bob", 30)]
❌ Not distributed
❌ No schema
❌ No optimization
❌ Cannot process big data

Spark DataFrame:

✔ Distributed across cluster
✔ Has schema (column names + types)
✔ Optimized by Spark engine
✔ Can process terabytes of data