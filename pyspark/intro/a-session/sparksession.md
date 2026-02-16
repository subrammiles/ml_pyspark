
# Spark Session

A SparkSession is the entry point to PySpark.

It is the object that:

(i).Connects your Python program to Spark

(ii).Starts the Spark engine

(iii).Lets you create DataFrames

(iv).Lets you run SQL queries

(v).Manages Spark configuration

Think of it like this:

🔑 SparkSession = the door to the Spark engine

Without it → you cannot use Spark.

This does:

1.Starts Spark engine (if not already running)
2.Creates SparkContext (low-level engine)
3.Sets app name
4.Prepares environment to work with DataFrames