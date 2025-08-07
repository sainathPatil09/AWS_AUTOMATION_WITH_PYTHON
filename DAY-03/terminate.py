# terminate_instance.py
import boto3

ec2_client = boto3.client('ec2')

instance_id = 'i-074825a63303c678d'  # Replace with your instance ID

response = ec2_client.terminate_instances(InstanceIds=[instance_id])
print(f"Terminating EC2 instance {instance_id}...")
