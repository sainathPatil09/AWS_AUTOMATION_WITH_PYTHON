# Day 2: Create & Manage S3 Buckets with Python (Boto3)

This module demonstrates how to automate common Amazon S3 operations using **Boto3**, the AWS SDK for Python.

---

##  Tasks Covered

1. **Bucket Operations**
2. **Object/File Operations**
3. **Access Control Operations**

---

## Bucket Operations

| File Name           | Purpose                                |
|---------------------|----------------------------------------|
| `create_bucket()`  | Create a new S3 bucket                 |
| `delete_bucket()`    | Delete Bucket From S3    |
| `head_bucket()`  | Check wheater Bucket exists     |


## Object/File Operations

| File Name           | Purpose                                |
|---------------------|----------------------------------------|
| `upload_file()`  | Upload file to S3 from local                 |
| `download_file()`    | Download file from S3 to local    |
| `delete_object()`  | Delete an existing object from S3     |

## Access Control Operations

| File Name           | Purpose                                |
|---------------------|----------------------------------------|
| `get_bucket_acl()`  | Get Permissions of Bucket                 |
<!-- | `download_file()`    | Download file from S3 to local    |
| `delete_object()`  | Delete an existing object from S3     | -->

---

## 📘 Prerequisites

- Python 3.x
- AWS credentials configured via `aws configure`
- Boto3 installed

```bash
pip install boto3
```

# Note: 
- Prerequisites are covered in DAY 1
