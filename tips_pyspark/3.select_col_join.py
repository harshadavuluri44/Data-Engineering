'''

During Spark joins, it's a good practice to select only the columns you need 
from the other DataFrame to avoid unnecessary data in the final result.

Example: join orders with customer info, but select only 'name' and 'city' from customers

df = orders_df.join(
                customers_df.select('id', 'name', 'city'),  # select only required columns
                on='id',
                how='left'
)

df.show()

'''