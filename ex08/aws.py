from typing import Any

try:
    import boto3
except ImportError:
    from ex08 import fake_boto3 as boto3


def s3() -> Any:
    return boto3.client("s3")


def sqs() -> Any:
    return boto3.client("sqs")


def sns() -> Any:
    return boto3.client("sns")
