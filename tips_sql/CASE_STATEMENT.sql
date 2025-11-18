CASE WHEN THEN ELSE END statement in SQL is 
    used to create conditional logic inside your quries, similar
    to if-else statements in python.

SYNTAX :

        CASE
            WHEN condition1 THEN result1
            WHEN condition2 THEN result2
            .....
            ELSE default_result
        END

SELECT customer_id, order_date, CASE WHEN order_date=first_date THEN 1 
                                     ELSE 0 
                                END as is_new 
FROM customer table;