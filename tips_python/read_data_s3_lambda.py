'''
Reading and writing Data to/from S3 using Lambda
'''

import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']
    file_key = event['Records'][0]['s3']['object']


    obj = s3.get_object(Bucket=bucket, Key=file_key)
    data = obj['Body'].read().decode('utf-8')

    df = pd.read_csv(StringIO(data))
    print(df.head())

# Writing to s3

obj2 = StringIO()
df.to_csv(obj2, index=False)
s3.put_object(Bucket='', Key='', Body=obj2.getValue())
