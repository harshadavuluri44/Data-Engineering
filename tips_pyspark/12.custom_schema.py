'''

How to define a custom schema while reading data?

------------------------------------------------------------------------------------------------

from pyspark.sql.types import StructField, StructType, IntegerType, StringType


custom_schema = StructType(
                        [StructField('col_1',IntegerType()),
                         StructField('col_2',StringType()),
                         StructField('col_7',IntegerType())
                        ]
                )


df = spark.read.schema(custom_schema).parquet(file_path)

'''

