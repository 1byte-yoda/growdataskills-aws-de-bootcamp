import json
from matrix_utils import transpose_matrix


def lambda_handler(event, context):
    print(transpose_matrix(event["array"]))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
