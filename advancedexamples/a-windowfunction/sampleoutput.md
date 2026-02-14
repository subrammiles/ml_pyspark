
+----------+-----+------+----+
|Department| Name|Salary|Rank|
+----------+-----+------+----+
|        HR|Cathy|  6000|   1|
|        HR|Alice|  5000|   2|
|        IT|  Bob|  7000|   1|
|        IT|David|  6500|   2|
+----------+-----+------+----+



Explination :
partitionBy("Department")

👉 Spark splits the data into separate groups:
HR group
IT group
Each department is processed independently.



orderBy(col("Salary").desc())

👉 Inside each department:
Rows are sorted by Salary
Highest salary comes first


rank().over(window_spec)
👉 Assigns ranking based on that order.
So inside each department: