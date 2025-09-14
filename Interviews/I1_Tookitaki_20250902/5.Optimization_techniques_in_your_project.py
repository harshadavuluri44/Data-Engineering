''' 
    Before diving into answer let's get clarified on
    UPSERT concept/operation
    MERGE INTO is implementation to acheive UPSERT


UPSERT = UPDATE + INSERT

Means :
    * If a row with given PK exists in the target table -> Then UPDATE the row with source data
    * If it doesn't exist -> INSERT it


UPSERT does not affect non-matching rows in target table (unless we explicitly add DELETE clause
in MERGE INTO statement)

MERGE INTO

It is a SQL statement that can implementation UPSERT

MERGE INTO target t
USING source s
on t.id = s.id
WHEN MATCHED THEN 
    UPDATE SET t.name = s.name
WHEN NOT MATCHED THEN
    INSERT (id, name) VALUES (s.id, s.name)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE

'''