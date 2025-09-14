'''
How data is stored actually inside a CSV file?

In a csv, data is stored in row-wise, plain text format

Each row in the file corresponds a record.

Within a row, individual column values are separated by delimiter (mainly comma)

All values are stored as strings, even if they are int or dates


------------------------------------------------------------------------------------

How data is stored in parquet file?

In parquet, data is stored in binary columnar format

Data is divided into row groups, and within each row groups, values are organized column by
column

parquet files also store metdata, that makes reading, filterning very efficient

'''