"""
Slowly Changing Dimensions (SCD)

SCDs are strategies used in Data Warehousing to handle changes in dimension table attributes over
time (such as customer address, product description, etc.).

Although dimension data doesn't change frequently, it does change slowly — and how we choose to 
store that history is critical for accurate analytics.

Why is SCD important?
    In analytics, sometimes we:
        Only care about the latest dimension values.
        Often want to track historical changes to understand how data looked at a specific point in 
        time.

-----------------------------------------------------------------------------------------------
SCD Types:

1. SCD Type 1 - Overwrite
        Simply update the existing row; old data is lost.
        Used when historical values are not required.
    
Example: Customer changes city -> update the city column directly.

    Implementation in PySpark/Databricks:
        Use Delta Lake MERGE INTO to overwrite the existing record.

-----------------------------------------------------------------------------------------------

2. SCD Type 2 - Maintain Full History
        Add a new row when a change happens.
        Maintain columns like: start_date, end_date, is_current.
        Keeps the entire lifecycle and history of each dimension record.
    
    Example:
        id   name   location  start_date    end_date      is_current
        101  John   Hyd       2023-01-01    2024-05-10    N
        101  John   London    2024-05-11    NULL          Y

    Implementation in PySpark/Databricks:
        Delta Lake MERGE + insert new record + update old record's metadata.
    
    Example SQL:
    MERGE INTO target AS t
    USING source AS s
    ON t.id = s.id AND t.is_current = 'true'
    WHEN MATCHED AND t.location <> s.location THEN
        UPDATE SET t.end_date = CURRENT_DATE(),
                   t.is_current = 'false'
    WHEN NOT MATCHED THEN
        INSERT (id, name, location, start_date, end_date, is_current)
        VALUES (s.id, s.name, s.location, CURRENT_DATE(), NULL, 'true')

-----------------------------------------------------------------------------------------------

3. SCD Type 3 - Limited History
        No new rows; new columns are added to hold previous values.
        Only keeps current and one previous version.
        Useful when limited history is enough and we don't want the table to grow.

Example columns: current_city, previous_city

-----------------------------------------------------------------------------------------------

Summary: SCD Implementation in PySpark & Databricks
    Type 1 -> Overwrite the matched row
    Type 2 -> Insert a new row version + mark old row as expired (is_current)
    Type 3 -> Update additional columns to capture old value

"""
