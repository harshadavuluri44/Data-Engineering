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

2. Performance is Slower incase of PySpark due to python code should be converted to JVM bytecode
   as spark is written on java

3. Ease of use, less code, more libraries available in python

--------------------------------------------------------------------------------------------------

from pyspark.sql import sparkSession

spark = sparkSession.builder.appName('test').getOrCreate()
'''