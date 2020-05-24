import json
import time
import boto3
import os

sqs = boto3.client("sqs")

def lambda_handler(event, context):
    message = event["body"]
    ip_address = event["requestContext"]["identity"]["sourceIp"]

    sqs.send_message(
        QueueUrl=os.environ["QUEUE_URL"],
        MessageBody=(
            json.dumps({
                "ip_address": ip_address,
                "message": message
            })
        )
    )

    return {
        "statusCode": 202,
        "body": json.dumps({
            "ip_address": ip_address,
            "timestamp": int(time.time()),
        })
    }
