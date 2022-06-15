import base64
import json
from typing import Any, Dict

from ex08 import aws


def save_file(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    body = json.loads(event["body"])

    data = base64.b64decode(body["data"])
    content_type = body["content_type"]
    key = body["filename"]
    bucket = "my-bucket"
    acl = "private"

    aws.s3().put_object(
        Body=data,
        Bucket=bucket,
        Key=key,
        ContentType=content_type,
        ACL=acl,
    )

    cliente_token = event["headers"]["x-api-key"]
    queue_url = "https://sqs.us-east-1.amazonaws.com/123/callback"
    payload = {"cliente_token": cliente_token, "bucket": bucket, "key": key}

    aws.sqs().send_message(QueueUrl=queue_url, MessageBody=json.dumps(payload))

    topic_arn = "arn:aws:sns:us-east-1:123:file_uploaded"
    message = {"message": "new-file", "bucket": bucket, "key": key}

    aws.sns().publish(
        TargetArn=topic_arn,
        Message=json.dumps(message),
        MessageStructure="json",
        MessageAttributes={},
    )

    response = {"statusCode": 201, "body": json.dumps({"message": "created"})}

    return response
