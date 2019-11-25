import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    response = ec2.ec2.describe_regions()
    return {"statusCode": 200, "body": json.dumps(response)}
