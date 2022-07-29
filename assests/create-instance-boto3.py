import boto3

ec2 = boto3.resource(
    service_name='ec2',
    region_name='us-east-2'
)
instances = ec2.create_instances(
    ImageId='ami-0aeb7c931a5a61206',
    InstanceType='t2.micro',
    KeyName='awskeypair',
    MinCount=1,
    MaxCount=1
)