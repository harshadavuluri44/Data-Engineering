'''

SCD 1

MERGE INTO target t
USING source s
ON t.id=s.id
WHEN MATCHED THEN
    UPDATE SET t.col_3 = s.col_3
WHEN NOT MATCHED BY SOURCE THEN
    INSERT (col_1,col_2,col_3)
    VALUES (s.col_1, s.col_2, s.col_3)

MERGE INTO target t
USING source s
ON t.id = s.id
WHEN MATCHED THEN
  UPDATE SET t.col_3 = s.col_3
WHEN NOT MATCHED THEN
  INSERT (col_1, col_2, col_3)
  VALUES (s.col_1, s.col_2, s.col_3)
'''