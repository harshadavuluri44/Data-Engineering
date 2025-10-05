""" Spark DataFrame - Handling Missing / Null Values """

df = []

# 1. Detect missing / null values

df.filter(df['col_name'].isNull()).show()       # rows where col_name is null
df.filter(df['col_name'].isNotNull()).show()    # rows where col_name is not null

# --------------------------------------------------------------------------------------------

# 2. Drop missing values

df.dropna().show()                              # drop rows with at least one null
df.dropna(subset=['col1', 'col2']).show()       # drop rows where col1 or col2 is null

# --------------------------------------------------------------------------------------------

# 3. Fill missing values

df.fillna(0).show()                             # replace all numeric nulls with 0
df.fillna({'col1': 0, 'col2': "NONE"}).show()   # replace nulls with col-specific values

# --------------------------------------------------------------------------------------------

# 4. Replace specific values (not just nulls)

# Syntax: df.replace(to_replace, value=None, subset=None)
#   to_replace -> value(s) to replace (single value, list, or dict)
#   value      -> replacement value(s)
#   subset     -> columns to apply replacement on (if None, applies to all columns)

df.replace(['NA', 'null', ''], 'NONE').show()

# --------------------------------------------------------------------------------------------