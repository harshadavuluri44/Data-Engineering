'''
Fact Table

* Stores numeric, measurable data about business events (facts)
* Facts are typically aggregates (sum, avg, count) etc.
* Each fact record is linked to dimension tables via foreign keys

Common fact table columns:

Date_Key        FK to Date dimension table
Product_Key     FK to Product dimesion table
Store_key       FK to store dimension
Units_sold      Fact measure
Revenue         Fact measure
--------------------------------------------------------------------------------------------------

Dimension Table

* Stores descriptive, textual information about business entities
* Helps to answer questions like who, what, when, where, how
--------------------------------------------------------------------------------------------------

Star Schema

* A central fact table, with multiple dimension tables directly linked
* Looks like a star shape after tables are connected
* Dimension tables are denormalized -> more redundancy but fast querying
-----------------------------------------------------------------------------------------------

Snowflake Schema

* An extension of Star Schema
* Dimension tables are normalized into multiple related tables -> less redudancy, but more joins -> 
  slightly slowly queries

-------------------------------------------------------------------------------------------------

What is Normalization?

It is the process of designing database tables in a such a way that:
    * Tables are broken into smaller related tables
    * Redundancy (repeated data) is minimized
    * Data is connected through foreign keys

Advantage    -> saves storage, avoids duplication
Disadvantage -> more joins needed during queries
-----------------------------------------------------------------------------------------------

What is Denormalization?

It is process of designing database tables by combining related data into one single wide table,
even if it causes repeated values

Advantage -> faster querying (fewer joins)
Disadvantage -> redundant data (more storage)
'''