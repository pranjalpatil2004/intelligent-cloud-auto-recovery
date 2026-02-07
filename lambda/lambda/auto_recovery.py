import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    instance_id = "YOUR_INSTANCE_ID"

    ec2.reboot_instances(InstanceIds=[instance_id])

    return {
        "statusCode": 200,
        "body": "Recovery action executed"
    }
