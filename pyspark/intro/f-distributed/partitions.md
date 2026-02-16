📊 How DataFrame Distribution Works

When you create a DataFrame:

df = spark.read.csv("big_file.csv")


Here’s what happens:

Step 1: File is split into partitions

Spark splits the data into chunks called partitions.

Example:

1GB file

4 cores available

Spark creates 4 partitions

Each core processes one partition

So data is divided like this:

Partition 1 → Executor 1
Partition 2 → Executor 2
Partition 3 → Executor 3
Partition 4 → Executor 4


Each executor processes its chunk independently.

🧠 Important Concept: Partition

A partition is:

A chunk of distributed data stored and processed independently.

You can check partitions:

df.rdd.getNumPartitions()