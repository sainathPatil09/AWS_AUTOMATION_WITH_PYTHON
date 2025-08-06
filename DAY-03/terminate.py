# terminate_instance.py
import boto3

ec2_client = boto3.client('ec2')

instance_id = 'i-0870f5b354dc38443'  # Replace with your instance ID

response = ec2_client.terminate_instances(InstanceIds=[instance_id])
print(f"Terminating EC2 instance {instance_id}...")
