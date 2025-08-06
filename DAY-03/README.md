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

| Concept            | Description                                                                         |
| ------------------ | ----------------------------------------------------------------------------------- |
| **AMI ID**         | Amazon Machine Image ID (e.g., `ami-0abcdef12345`) – required to launch an instance |
| **Instance Type**  | e.g., `t2.micro` (free-tier eligible)                                               |
| **Key Pair Name**  | Required for SSH access                                                             |
| **Security Group** | Firewall rules                                                                      |
| **Instance ID**    | Unique identifier for your EC2 instance                                             |
| **Tags**           | Metadata for better management                                                      |

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
