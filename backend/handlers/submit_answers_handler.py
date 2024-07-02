import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('QuizQuestions')

def lambda_handler(event, context):
    answers = json.loads(event['body'])
    score = 0
    
    for answer in answers:
        question_id = answer['questionId']
        user_answer = answer['text']
        response = table.get_item(Key={'id': question_id})
        question = response.get('Item', {})
        correct_answer = next((ans for ans in question['answers'] if ans['correct']), None)
        
        if correct_answer and correct_answer['text'] == user_answer:
            score += 1
    
    return {
        'statusCode': 200,
        'body': json.dumps({'score': score})
    }
