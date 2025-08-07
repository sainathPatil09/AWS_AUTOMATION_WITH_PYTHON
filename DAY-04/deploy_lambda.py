import boto3

# Initialize Lambda client
lambda_client = boto3.client('lambda')

# Replace with your actual IAM Role ARN
role_arn = 'arn:aws:iam::3966090362:role/service-role/test-lambda-role-aic4uwiv'

# Read the zip file
with open('function.zip', 'rb') as f:
    zipped_code = f.read()

# Create Lambda Function
response = lambda_client.create_function(
    FunctionName='MyAutomatedLambda',
    Runtime='python3.9',
    Role=role_arn,
    Handler='lambda_function.lambda_handler',
    Code={'ZipFile': zipped_code},
    Description='Lambda deployed using Boto3',
    Timeout=15,
    MemorySize=128,
    Publish=True
)

print("✅ Lambda Function ARN:", response['FunctionArn'])
