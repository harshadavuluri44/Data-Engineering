"""
Fact Table

Stores numeric, measurable data about business events (facts)
Facts are typically aggregates like sum, avg, count, etc.
Each fact record is linked to dimension tables via foreign keys

Common fact table columns:
    Date_Key      Foreign key to Date dimension table
    Product_Key   Foreign key to Product dimension table
    Store_Key     Foreign key to Store dimension table
    Units_Sold    Fact measure
    Revenue       Fact measure

-----------------------------------------------------------------------------------------------
Dimension Table

Stores descriptive, textual information about business entities
Helps to answer questions like who, what, when, where, how

------------------------------------------------------------------------------------------------

Star Schema

A central fact table with multiple dimension tables directly linked
Dimension tables are denormalized, which increases redundancy but enables fast querying

-------------------------------------------------------------------------------------------------

Snowflake Schema

An extension of Star Schema
Dimension tables are normalized into multiple related tables
Reduces redundancy but requires more joins, which may slow down queries

-------------------------------------------------------------------------------------------------

Normalization

The process of designing database tables to:
    Break tables into smaller related tables
    Minimize redundancy (repeated data)
    Connect data through foreign keys

Advantages: saves storage, avoids duplication
Disadvantages: requires more joins during queries

---------------------------------------------------------------------------------------------------

Denormalization

The process of designing database tables by combining related data into one wide table
This may cause repeated values but simplifies queries

Advantages: faster querying (fewer joins)
Disadvantages: redundant data (more storage)

-----------------------------------------------------------------------------------------------

When to Use Each (star vs snowflake)

Star schema:
    When query performance and simplicity(simple structure) are priorities
    Best suited for OLAP systems when denormalization speeds up aggregations and joins

Snowflake Schema:
    When storage optimization or data consistency is more important
    Used when dimensions are large(many columns or many rows) or have hierarchical relationships


"""
