'''

.contains('shr')  -   LIKE '%shr%' in SQL
.startsWith('shr')    LIKE 'shr%' in SQL
.endsWith('shr')      LIKE '%shr' in SQL



df.filter(df['name'].contains('shr'))
'''