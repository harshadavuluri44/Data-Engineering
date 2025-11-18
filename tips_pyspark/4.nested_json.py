'''

If there is nested json with struct schema, We can accesss items inside struct columns by

df.select(col("customer.city").alias("city"),
          col("item.product").alias("product")).show()


explode() works only for arrays and maps

'''