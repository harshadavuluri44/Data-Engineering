'''

How do you optimize pyspark code in production pipelines?

------------------------------------------------------------------------------------------------
   
1) Use efficient file formats like parquet instead of csv/json for better compression and columnar
   storage (ex: while writing)

2) Use caching and persistence to access or reuse dataframe further in code
3) Use df.rdd.getNumPartitions() to check number of partitions
   repartition or coalsece to wisely balance load across cluster nodes

4) Minimize shuffle operations by using 
   broadcast joins for small tables (<200MB)

5) Use dataframes over rdds, to get benifit from catalyst optimizer, better performance

6) Use built-in functions instead of UDF when possible

7) Predicate Pushdown and Column pruning

8) Monitor and Tuning
   Find slow jobs and skewed tasks

'''