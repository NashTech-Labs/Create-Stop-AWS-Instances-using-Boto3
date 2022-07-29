# Create and Stop Instances on AWS using Boto3

---

## Short Description 

This template will you the flavour of boto3 where you will be able to create and stop the instances using boto3 without using UI of AWS.

---
### Commands 

`python3 filename.py`

#### Note : To configure AWS IAM User

`sudo apt install awscli`

Then configure using , `aws configure`

<img alt="aws-config.png" height="80" src="assests/aws-config.png" title="AWS configuration" width="400"/>

Find you AWS Access KEY and Secret in your AWS account 

---
### Steps to Kick Start

First , create an Instance using boto3, before the instance present 

`create-instance-boto3.py`

<img alt="before.png" height="100" src="assests/before.png" title="AWS Instance List before Instance" width="500"/>

Instance is created using Boto3,

<img alt="instance-up.png" height="200" src="assests/instance-up.png" title="S3 bucket Created" width="500"/>

`stop-instance-boto3.py`

List after the Instance is Stop file called,

<img alt="s3.png" height="200" src="assests/stop-instance.png" title="Naming S3 buckets" width="500"/>

