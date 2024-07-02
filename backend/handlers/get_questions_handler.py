import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('QuizQuestions')

def lambda_handler(event, context):
    response = table.scan()
    questions = response.get('Items', [])
    
    return {
        'statusCode': 200,
        'body': json.dumps(questions)
    }
