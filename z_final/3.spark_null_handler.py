'''
1. Detect missing/ null values

df.filter(df['col_name'].isNull()).show()

df.filter(df['col_name'].isNotNull()).show()
--------------------------------------------------------------------------------------------

2. Drop missing values 

df.dropna().show()  -> Returns df after dropping rows with atleast one null in row

df.dropna(subset=['col1','col2']).show() -> df after dropping rows with both col1 & col2 are null
--------------------------------------------------------------------------------------------------

3. Fill missing values

df.fillna(0).show()

df.fillna({'col1': 0, 'col2': "NONE"}).show()
-----------------------------------------------------------------------------------------------

4. REPLACE

SYNTAX :- df.replace(to_replace, value=None, subset=None)

to_replace -> the values we want to replace, it can be single value or list of values
value -> the value to be used as replacement
subset -> if None replace everywhere in all columns of dataframe, else provide specific cols

df.replace(['NA', 'null', ''], NONE).show()
'''