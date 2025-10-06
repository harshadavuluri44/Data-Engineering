'''

How data is stored inside a CSV file:

    In a CSV, data is stored in row-wise plain text format.
    Each row corresponds to a record.
    Within a row, individual column values are separated by a delimiter (commonly a comma).
    All values are stored as strings, even if they are integers or dates.

--------------------------------------------------------------------------------

How data is stored in a Parquet file:

    In Parquet, data is stored in binary columnar format.
    Data is divided into row groups, and within each row group, values are organized column by column.
    Parquet files also store metadata, which makes reading, filtering, and query execution very 
    efficient.

------------------------------------------------------------------------------------------------

'''
