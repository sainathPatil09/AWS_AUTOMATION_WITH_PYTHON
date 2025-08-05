import boto3

s3_client = boto3.client("s3")

response = s3_client.create_bucket(
    Bucket="my-new-bucket-demo-yt",
    CreateBucketConfiguration={
        "LocationConstraint": "ap-south-1"
    }
)

print("Bucket created successfully:", response['Location']) if 'Location' in response else print("Bucket creation failed.")

# Check if a bucket exists
# response = s3_client.head_bucket(
#     Bucket='models-sagemaker-iris'
# )

# print("Bucket exists and is accessible.") if response else print("Bucket does not exist or is not accessible.")


# Bucket Deletion
# response = s3_client.delete_bucket(
#     Bucket='my-new-bucket-demo-yt',
# )
# if response:
#     print("Bucket deleted successfully.")
# else:
#     print("Bucket deletion failed or bucket does not exist.")

