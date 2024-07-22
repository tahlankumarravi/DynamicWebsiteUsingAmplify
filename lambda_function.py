import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Initialize a session using Amazon DynamoDB
    dynamodb = boto3.resource('dynamodb')
    
    # Select your DynamoDB table
    table = dynamodb.Table('NMITHackathonRegistrationTable')
    
    # Extracting data from the event
    registration_number = event.get('registrationNumber')
    name = event.get('name')
    branch = event.get('branch')
    
    # Prepare the data for insertion
    item = {
        'registrationNumber': registration_number,
        'name': name,
        'branch': branch
    }
    
    # Insert the data into the DynamoDB table
    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps('Registration successful!')
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error saving the data: {e.response["Error"]["Message"]}')
        }
