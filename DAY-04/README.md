# 🚀 AWS Lambda Automation with Boto3 (Day 4)

This guide covers how to create and deploy AWS Lambda functions manually and programmatically using Python and Boto3. You'll also learn the basics of Lambda, how it differs from EC2, what events can trigger Lambda, and how to get started with automation.

---

## Topics Covered
- What is AWS Lambda?
- Why Use Lambda?
- Lambda vs EC2
- Lambda Triggers
- Manual Lambda Function Creation
- Automate Lambda Deployment with Boto3

---

### ✅ What is AWS Lambda?

- AWS Lambda is a serverless compute service.
- It runs your code **without provisioning or managing servers**.
- You only pay for the compute time you consume.

---

### ✅ Why Use Lambda?

- Auto-scaling and cost-effective.
- Ideal for short-lived, event-driven tasks.
- Great for microservices, data processing, automation, etc.

---

### 🔄 Lambda vs EC2

| Feature         | AWS Lambda                  | Amazon EC2                      |
|-----------------|-----------------------------|----------------------------------|
| Server Management | Fully managed (serverless) | You manage the server            |
| Billing         | Per request + duration       | Per hour/second                  |
| Scaling         | Automatic                    | Manual or with auto-scaling      |
| Use Case        | Event-driven apps, automation| Web apps, custom server setups   |

---

### ⚡ Lambda Triggers (3 Common Events)

1. **S3 Event**: Trigger when a file is uploaded or deleted.
2. **API Gateway**: Trigger via REST API calls.
3. **CloudWatch Events / Scheduled Cron**: Run periodically based on a schedule.

---

## 🛠️ Manual Lambda Function Creation

1. Go to [AWS Lambda Console](https://console.aws.amazon.com/lambda/)
2. Click **Create function**
3. Choose:
   - Author from scratch
   - Name, Runtime (e.g., Python 3.9)
   - Create a new execution role or use existing
4. Add code directly or upload a `.zip`
5. Deploy and test

---

## 🛠️ Steps to Create a Lambda Function using Boto3

### 1.  Prerequisites
- Python 3.x installed
- Boto3 installed
- AWS CLI installed and configured

### 2. Create an IAM Role for Lambda
- Go to IAM Console
- Create a new role with:
    - Trusted entity: Lambda
    - Policy: AWSLambdaBasicExecutionRole
- Note the Role ARN (used in deployment script)

### 3. Write Your Lambda Function Code
- Create a file named ``lambda_function.py``

### 4. Zip the Code

- `python -m zipfile -c function.zip lambda_function.py`

### 5. Deploy Lambda Using Boto3
- Script `deploy_lambda.py`

