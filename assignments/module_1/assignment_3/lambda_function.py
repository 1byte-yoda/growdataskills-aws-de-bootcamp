import json

import boto3
import pandas as pd

s3 = boto3.client('s3')
sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:ap-southeast-1:557690618849:doordash-file-processing'

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(bucket, key)

    try:
        obj = s3.get_object(Bucket=bucket, Key=key)

        df = pd.read_json(obj['Body'].read().decode('utf-8'), lines=True)
        df = df[df["status"] == 'delivered']
        print(df.head())

        s3.put_object(Body=df.to_json(), Bucket="doordash-target-zn-assignment-3", Key=key.split('/')[-1])

        message = f"Successully processed {key} in bucket {bucket}"
        sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject='DoorDash File Processing Success'
        )
        return {
            'statusCode': 200,
            'message': message
        }
    except Exception as e:
        message = f"Error processing file {key} in bucket {bucket}: {str(e)}"
        sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject='DoorDash File Processing Failed'
        )
        return {
            'statusCode': 400,
            'message': message
        }


