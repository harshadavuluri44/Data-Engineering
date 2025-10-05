"""

OLTP (Online Transaction Processing):

    A system or database designed to manage and process day-to-day transactional data in real-time,
    supporting operations like insert, update, delete, and read while ensuring data integrity and 
    fast transaction processing.

Examples: MySQL, PostgreSQL, Oracle, SQL Server.

---------------------------------------------------------------------------------------------------

OLAP (Online Analytical Processing):

    A system or tool designed to store and analyze large volumes of historical data, supporting 
    complex queries, aggregations, and multi-dimensional analysis to aid business decision-making.

Examples: AWS Redshift, Google BigQuery, Snowflake.

--------------------------------------------------------------------------------------------------

Key Differences:

Feature           | OLTP                                   | OLAP
----------------  | -------------------------------------  | -------------------------------------------
Purpose           | Manage daily transactional data        | Analyze historical data for business decisions
Schema            | Highly normalized (reduces redundancy) | Denormalized, often star or snowflake schema
Updates           | Frequent, real-time                    | Batch updates via ETL
Query Type        | Simple, short, fast                    | Complex, long-running analytical queries
Data Volume       | Smaller                                | Very large
Performance       | Optimized for fast inserts/updates     | Optimized for aggregations and analysis
Data Type         | Current, operational data              | Historical, aggregated data
Database Examples | MySQL, PostgreSQL, Oracle, SQL Server  | AWS Redshift, Google BigQuery, Snowflake

----------------------------------------------------------------------------------------------

Data Flow:
OLTP systems --> ETL process --> OLAP systems


"""
