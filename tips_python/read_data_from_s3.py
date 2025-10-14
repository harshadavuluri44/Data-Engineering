import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')

bucket_name = 'sustainability_economics'
file_key = 'path/data_ai.csv'

obj = s3.get_object(Bucket=bucket_name, Key=file_key)

df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))

print(df.head())


# Write back to s3

obj_2 = StringIO()    # empty object in python in-memory

df.to_csv(obj_2)

s3.put_object(Bucket=bucket_name, Key='path', Body=obj_2.getvalue())

# ------------------------------------------------------------------------------------------

'''

1. s3.get_object()

    Returns dictionary containing metadata and the file content.
    Key fields include:

        Body : The actual content of file as stream of bytes (Not as string)
        ContentLength: Size of the object/file
        LastModified: Timestamp of last modification

        etc,...

    Since Body is not a string yet - we need to read and decode it to get a text string


2. Reading the body

    obj['Body'].read().decode('utf-8')

        obj['Body'].read() -> reads all bytes from object returned by s3.get_object()

        .decode('utf-8') -> converts bytes to a string so Python can work on it

3. StringIO - StringIO creates an in-memory file like object


    pandas.read_csv() expects a file-like object or a file path

    wrapping the text String returned from 2nd point in StringIO treats string as file object in python
    memory

'''

