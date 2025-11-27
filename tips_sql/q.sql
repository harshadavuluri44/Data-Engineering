Section 3 – SQL Question: Top Products by Segment (Last 90 Days)
You are given the following tables:
Table: customers
    column	type	description
    customer_id	int	Primary key
    customer_name	varchar	Customer name
    segment	varchar	e.g. 'Retail', 'Wholesale'
    country	varchar	Country name
 
Table: orders
    column	type	description
    order_id	int	Primary key
    customer_id	int	FK to customers.customer_id
    order_date	date	Date the order was placed
 
Table: order_items
    column	type	description
    order_id	int	FK to orders.order_id
    product_id	int	FK to products.product_id
    quantity	int	Quantity ordered
    unit_price	decimal	Price per unit at time of order
 
Table: products 
    column	type	description
    product_id	int	Primary key
    product_name	varchar	Product name
    category	varchar	e.g. 'Yogurt', 'Milk', 'Snacks'
 
Write a single SQL query that returns, for the last 90 days (relative to today):
•	segment  -- customers
•	product_name  -- products --t2
•	total_revenue (sum of quantity × unit_price) --t1
•	segment_product_rank (1 = highest revenue product within that segment over the last 90 days)
Only include products that are in the top 3 by revenue within their segment in that period.
 
Assume the current date can be referenced as CURRENT_DATE.
You can use standard SQL or a Snowflake/Postgres-style dialect (CTEs allowed).