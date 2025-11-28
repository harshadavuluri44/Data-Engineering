from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType
from pyspark.sql.functions import col, explode

# ---------------------------
# 1. Nested JSON data
# ---------------------------
data = [
    {
        "id": 1,
        "name": "Alice",
        "contact": {
            "email": "alice@example.com",
            "phones": [
                {"type": "home", "number": "111-111"},
                {"type": "work", "number": "222-222"}
            ]
        },
        "orders": [
            {"order_id": 101, "amount": 250},
            {"order_id": 102, "amount": 450}
        ]
    },
    {
        "id": 2,
        "name": "Bob",
        "contact": {
            "email": "bob@example.com",
            "phones": [
                {"type": "home", "number": "333-333"}
            ]
        },
        "orders": [
            {"order_id": 103, "amount": 300}
        ]
    }
]

# ---------------------------
# 2. Define explicit schema
# ---------------------------
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("contact", StructType([
        StructField("email", StringType(), True),
        StructField("phones", ArrayType(
            StructType([
                StructField("type", StringType(), True),
                StructField("number", StringType(), True)
            ])
        ), True)
    ]), True),
    StructField("orders", ArrayType(
        StructType([
            StructField("order_id", IntegerType(), True),
            StructField("amount", IntegerType(), True)
        ])
    ), True)
])

# ---------------------------
# 3. Create SparkSession and DataFrame
# ---------------------------
spark = SparkSession.builder.appName("FlattenNestedJSON").getOrCreate()
df = spark.createDataFrame(data, schema=schema)

df.show(truncate=False)

df_1=df.select('id', 'name', col('contact.email'), col('contact.phones'),'orders')
df_2 = df_1.withColumn('phone',explode(col('phones')))\
            .withColumn('order',explode(col('orders')))
df_2 = df_2.select('id','name','email','phone','order')
df_2.show(truncate=False)