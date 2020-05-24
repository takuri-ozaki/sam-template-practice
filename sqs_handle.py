import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Table")

def lambda_handler(event, context):
    body = json.loads(event["Records"][0]["body"])
    ip_address = body["ip_address"]
    message = body["message"]

    table.put_item(
        Item={
            "ipAddress": ip_address,
            "message": message
        }
    )
