/* Question 1: Running Totals
   Given a sales table with columns date, amount, write a query to calculate the running total 
   of sales for each day, ordered by date */

SELECT date, amount, SUM(amount) OVER(ORDER BY date) as running_total FROM sales;

-- Update to above Q, there are multiple sales on same day(more than 1 row with same date)

SELECT date, daily_total, SUM(daily_total) OVER(ORDER BY date) as running_total FROM (
    SELECT date, SUM(amount) as daily_total FROM sales GROUP BY date) as daily_sales;

    /* Alias (as daily_sales) is mandatory, bcz every derived table(i.e from subquery) must have
       an alias even if you dont reference it later*/

----------------------------------------------------------------------------------------------
