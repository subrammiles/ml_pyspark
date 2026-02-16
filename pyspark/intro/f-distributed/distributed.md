# Spark Is Distributed

Spark does NOT run like normal Python.

It runs in a cluster architecture:

🧠 Driver (your Python program)

⚙️ Executors (worker processes)

💾 Cluster (multiple machines or cores)

Your Python code runs only on the Driver.

The actual data processing happens on Executors.

🧠 Think of It Like Google Docs

Python list = Word document on your computer.

Spark DataFrame = Google Doc:

Data stored across servers

You just see a reference

Multiple workers operate on different sections