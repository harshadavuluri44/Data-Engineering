'''

trim() -> removes leading & trailing whitespaces from string column
rtim() -> removes trailing whitespaces only
ltrim() -> removes leading whitespaces only


df = df.withColumn('updated_name', trim(col('name')))

'''