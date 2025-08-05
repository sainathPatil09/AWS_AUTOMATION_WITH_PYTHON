import boto3

s3_client = boto3.client("s3")

response = s3_client.get_bucket_acl(Bucket='my-new-bucket-demo-yt')
print("Bucket ACL:", response['Grants']) if 'Grants' in response else print("Failed to retrieve bucket ACL.")

