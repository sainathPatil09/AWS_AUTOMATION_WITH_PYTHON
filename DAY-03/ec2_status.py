# check_status.py
import boto3

ec2_client = boto3.client('ec2')

instance_id = 'i-0870f5b354dc38443'  # Replace with your instance ID

response = ec2_client.describe_instance_status(InstanceIds=[instance_id])

statuses = response.get("InstanceStatuses", [])

if not statuses:
    print(f"Instance {instance_id} is pending or not found.")
else:
    state = statuses[0]['InstanceState']['Name']
    print(f"Instance {instance_id} is {state}.")
