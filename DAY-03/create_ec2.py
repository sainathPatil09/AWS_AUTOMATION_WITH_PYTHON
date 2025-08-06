import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.run_instances(
    ImageId='ami-0f918f7e67a3323f0',
    InstanceType='t2.micro',
    KeyName='demo-vpckey',
    MinCount=1,
    MaxCount=1,
    # SecurityGroupIds=['sg-0abc123def456ghij'],
    # BlockDeviceMappings=[
    #     {
    #         'DeviceName': '/dev/xvda',  # Default root volume device name
    #         'Ebs': {
    #             'VolumeSize': 15,         # Size in GiB
    #             'VolumeType': 'gp3',      # General Purpose SSD
    #             'DeleteOnTermination': True
    #         }
    #     }
    # ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyEC2Instance'}]
        }
    ]
)


instance_id = response['Instances'][0]['InstanceId']
print(f"Launched EC2 instance with ID: {instance_id}")