'''

APACHE SPARK

Apache Spark is an open-source, distributed computing framework designed for big data processing.
It supports/ allows processing large-scale data in a clustered environment with high speed using
in-memory computation.

---------------------------------------------------------------------------------------------------

PYSPARK

PySpark is Python API for Apache Spark, allowing developers to write Spark Applications using
Python instead of built-in Scala or Java

--------------------------------------------------------------------------------------------------

DIFFERENCES

1. PySpark uses Python
   Whereas Spark natively is written in Scala

2. Performance is slower incase of PySpark due to python code should be converted to JVM bytecode
   as spark runs on JVM

3. Ease of use, less code, more libraries available in python

--------------------------------------------------------------------------------------------------

from pyspark.sql import sparkSession

spark = sparkSession.builder.appName('test').getOrCreate()

--------------------------------------------------------------------------------------------------

Started career with Spark 3.3.0 (11.3 LTS DBR)

Moved to Spark 3.5.0 (15.4 LTS DBR)

Major change I observed from 3.3 to 3.5 is AQE feature in terms of performance

1. AQE automatically adjusts shuffle partitions, apply join strategies, handles skews more efficiently
   at runtime.

2. Spark 3.5.0 which comes up with python version of 3.11 made UDF's execution bit faster


'''