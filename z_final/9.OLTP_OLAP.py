'''
OLTP : A system or database designed to manage and process day-to-day transactional data in real
time, supporting operations like insert, update, delete and read while ensuring data integrity
and fast transaction processing.

Ex: MySql database

OLAP : A system or tool designed to analyze large volumes of historical data warehouse, supporting
complex queries, aggregations and multi-dimensional analysis to aid business decision-making.

Ex: AWS Redshift

--------------------------------------------------------------------------------------------

DIFFERENCES BETWEEN OLTP and OLAP SYSTEMS

Purpose
    OLTP systems manage day-to-day transactional operations data
    OLAP systems manage historical data and can analyze analyze for business decisions

Data Type
    OLTP contains current, operational data
    OLAP contains historical, aggregate data

Schema
    Highly Normalized (to reduce redundancy)
    De-normalized, often star or snowflake schema

Query Type
    Simple, short, fast
    Complex, long-running, analytical queries

Data Volume
    OLAP > OLTP

Perfromance
    Fast incase of basic operations
    Fast incase of big aggregations 

Updates
    Frequent
    Batch updates

Database Examples
    MySQL, PostgreSQL, Oracle, SQL Server
    AWS Redshift, Google BigQuery, Snowflake


Data From OLTP systems -> ETL -> OLAP
'''