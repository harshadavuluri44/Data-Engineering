"""
UDF = User Defined Function in PySpark

    A UDF is a custom Python function that we teach Spark to run on each row of a DataFrame column.

When to use UDF?
    If we need a transformation on a DataFrame that Spark does not provide as a built-in function,
    we can create a UDF and apply it.

Example: ML-related custom transformations.

NOTE:
    UDFs can be slower than Spark built-in functions because they run Python code row by row 
    and break Spark's Catalyst optimizer.
    
    Always prefer Spark built-in functions whenever possible.

-------------------------------------------------------------------------------------------------
Example: Convert a number to its English words

Spark doesn't have a built-in function to turn 123 into "one hundred twenty-three".
We can do this with a UDF.

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
import inflect

spark = SparkSession.builder.appName("udf_example").getOrCreate()

p = inflect.engine()

# Step 1: Write a normal Python function
def func(num: int) -> str:
    if num is None:
        return None
    return p.number_to_words(num)


# Step 2: Register it as a Spark UDF
func_registered = udf(func, str)


# Example DataFrame
data = [(123,), (45,), (None,), (1001,)]
df = spark.createDataFrame(data, ["num"])


# Step 3: Apply UDF on a column
df.withColumn("num_in_words", func_registered("num")).show(truncate=False)

# -----------------------------------------------------------------------------------------

"""
Summary:
    UDF is powerful for custom logic not available in Spark.
    But UDFs are slower because they cannot be optimized by Spark's Catalyst optimizer.
"""
