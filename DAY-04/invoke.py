import boto3
import json

# Initialize Lambda client
lambda_client = boto3.client('lambda')

# Invoke the Lambda function
response = lambda_client.invoke(
    FunctionName='MyAutomatedLambda',
    InvocationType='RequestResponse', 
    Payload=json.dumps({"key": "value"})  
)

# Read the response
response_payload = response['Payload'].read().decode('utf-8')
print("Lambda Output:", response_payload)
