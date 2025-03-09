import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    records = event["Records"]
    _FILE_SIZE_THRESHOLD = 10**8  # 100MB
    for record in records:
        file_size = record["s3"]["object"]["size"]
        file_name = record["s3"]["object"]["key"]
        if file_size >= _FILE_SIZE_THRESHOLD:
            logger.info(f"File Size Exceeded Threshold: {file_name}")
            logger.info(f"File Size: {file_size}")

    return {
        'statusCode': 200,
        'body': json.dumps('AWS_Lambda_Assignment_1')
    }
