# Day 1: AWS Setup & Boto3 Basics

## What You Will Learn Today
- What is Boto3, Why Boto3
- Install Boto3
- What is AWS CLI (Command Line Interface)
- Install AWS CLI
- List S3 Buckets(Manually and Programatically)

## What is Boto3, Why Boto3 ?

- Boto3 is the **AWS SDK** for Python.
- It allows you to interact with AWS services programmatically using Python.
- Example use cases: uploading files to S3, launching EC2 instances, managing IAM users, etc.

## Why Use Boto3

- Automate tasks in Python scripts (e.g., daily backup to S3).
- Write custom logic for AWS workflows (e.g., conditionally create resources).
- Good for application-level automation or scripts that interact with AWS dynamically.

## Install Boto3

To install Boto3, use pip:

```bash
pip install boto3
```

## What is AWS CLI

**AWS CLI (Command Line Interface)** is a tool that lets you control AWS services from your terminal or command prompt using simple commands.

- Create, manage, and delete AWS resources using terminal commands
- Script repetitive operations.

## Install AWS CLI
To install the AWS CLI, follow these steps:

### On Windows

1. Download the AWS CLI MSI installer from the [official AWS CLI page](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
2. Run the installer and follow the on-screen instructions.

### On macOS

```bash
brew install awscli
```
Or use pip:
```bash
pip install awscli
```

### On Linux

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

After installation, verify with:
```bash
aws --version
```

## AWS Configure
```bash
aws configure
```
You'll be asked for:

- AWS Access Key ID
- AWS Secret Access Key
- Default region
- Output format

