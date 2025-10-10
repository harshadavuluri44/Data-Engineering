-- GIVEN table

-- Add new column

ALTER TABLE table_name ADD new_col_1 INT

UPDATE TABLE
SET new_col_1 = col_1 + col_2

ALTER TABLE table_name ADD new_col_2 STRING

UPDATE TABLE
SET new_col_2 = CONCAT(col_3, '@', col_4, '.com')

ALTER TABLE table_name DROP column_name