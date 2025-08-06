# Day 3: Automate EC2 (Launch, Stop, Terminate Instances) using Boto3

In this session you will learn how to automate the **lifecycle of an AWS EC2** instance using Python and Boto3. 
It covers: 
-  launching an instance
-  checking its status
-  stopping it
-  and finally terminating it.

 **all via code and manual**.

---

##  Key EC2 Concepts to Know

| **Concept**        | **Description**                                                                                                                                                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AMI ID**         | **Amazon Machine Image ID** (e.g., `ami-0abcdef12345`) <br> It is a template that contains the software configuration (OS, application server, applications) required to launch an instance. You must specify an AMI when launching an EC2 instance. |
| **Instance Type**  | Defines the **hardware configuration** of your EC2 instance. <br> For example, `t2.micro` is a **free-tier eligible** instance type with limited CPU and memory – suitable for light workloads.                                                      |
| **Key Pair Name**  | Used for **SSH access** to your EC2 instance. <br> A key pair consists of a public key (stored by AWS) and a private key (downloaded by you). It allows you to securely connect to your instance.                                                    |
| **Security Group** | Acts as a **virtual firewall** for your EC2 instance. <br> It controls **inbound and outbound traffic** (e.g., allow port 22 for SSH or port 80 for HTTP).                                                                                           |
| **Instance ID**    | A **unique identifier** (e.g., `i-1234567890abcdef0`) automatically assigned by AWS to your running instance. Used to manage and track the instance.                                                                                                 |
| **Tags**           | **Key-value pairs** you can assign to AWS resources (e.g., Name = "WebServer") for **easier organization, search, automation, and billing management**.                                                                                              |


---

##  Automation Tasks You’ll Learn
**1. Launch EC2 Instance**
- Use run_instances() from boto3.client('ec2')
- Required parameters: AMI ID, instance type, key name, min/max count, etc.

**2. Check Instance Status**
- Use describe_instances() to get current status
- Parse the response for state (pending, running, stopped, terminated)

**3. Stop Instance**
- Use stop_instances(InstanceIds=[...])

**4. Terminate Instance**
- Use terminate_instances(InstanceIds=[...])


> **Note:**  
> Always terminate test instances after use to avoid unwanted AWS charges.
