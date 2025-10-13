date_column = 2023-08-19

IN SQL YEAR(date_column) returns only year, i.e 2023
       MONTH(date_column) returns only month i.e 08

Write a SQL query to find customers who placed orders in every month of the year 2024

SELECT customer_id FROM orders WHERE YEAR(order_date)=2024 
GROUP BY customer_id HAVING COUNT(DISTINCT MONTH(order_date))=12