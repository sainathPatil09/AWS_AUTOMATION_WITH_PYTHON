import boto3

s3_client = boto3.client("s3")

# upload = s3_client.upload_file(r"C:\Users\SAINATH PATIL\Desktop\Gen_AI.pdf", 'my-new-bucket-demo-yt', 'demo_ai.pdf')
# print("File uploaded successfully.") if upload else print("File upload failed.")



# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Sid": "AllowPublicReadAccessToPDF",
#       "Effect": "Allow",
#       "Principal": "*",
#       "Action": "s3:GetObject",
#       "Resource": "arn:aws:s3:::my-new-bucket-demo-yt/demo_ai.pdf"
#     }
#   ]
# }


# response = s3_client.download_file(
#     'my-new-bucket-demo-yt',
#     'demo_ai.pdf',  # Assuming this is the correct file name in S3
#     r'D:\work\AWS_AUTOMATION_WITH_PYTHON\DAY-02\demo_ai.pdf'  # Full path with file name
# )


# s3_client.delete_object(
#     Bucket='my-new-bucket-demo-yt',
#     Key='demo_ai.pdf'
# )

# print("Object deleted successfully.")


