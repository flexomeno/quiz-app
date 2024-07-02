import json
import boto3
from gift_parser import parse_gift_file

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('QuizQuestions')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    questions = parse_gift_file(content)
    
    with table.batch_writer() as batch:
        for question in questions:
            batch.put_item(Item=question)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Questions imported successfully')
    }
