# Using Boto3 on AWS display the Buckets list


## Short Description 

This template will you the flavour of boto3 where you will find how to get the names or list of buckets and EC2 instances without using UI of AWS. 

## Getting Started with Installation

* Install python
* Install pip

### Commands 

`sudo apt-get update`

`sudo apt-get install python3 -y`

`sudo apt-get install ansible -y`

`sudo apt-get -y install python3-pip`

`pip3 --version`

#### Note : To configure AWS IAM User

`sudo apt install awscli`

Then configure using , `aws configure`

<img alt="s4.png" height="80" src="assests/s4.png" title="AWS configuration" width="400"/>

Find you AWS Access KEY and Secret in your AWS account 

### Steps to Kick Start

First , create an Instance on AWS

<img alt="s1.png" height="100" src="assests/s1.png" title="AWS Instance Created" width="500"/>

Create some S3 bucket 

<img alt="s2.png" height="200" src="assests/s2.png" title="S3 bucket Created" width="500"/>

Name the bucket 

<img alt="s3.png" height="200" src="assests/s3.png" title="Naming S3 buckets" width="500"/>

Run the *file.py* file using the command

`python3 file.py`

It will provide you with the list of buckets.

`listing_EC2_Instances`

It will provide you with the list of EC2 instances.

#### OUTPUT

<img alt="s3.png" height="80" src="assests/s5.png" title="Display all buckets" width="500"/>


<img alt="s5.png" height="200" src="assests/instance check boto3.png" title="Display all buckets" width="500"/>

