import json
import unittest
from unittest.mock import patch

from ex08 import handlers


class TestSaveFile(unittest.TestCase):
    def setUp(self):
        self.s3_patcher = patch("ex08.aws.s3")
        self.sqs_patcher = patch("ex08.aws.sqs")
        self.sns_patcher = patch("ex08.aws.sns")

        self.m_s3 = self.s3_patcher.start()
        self.m_sqs = self.sqs_patcher.start()
        self.m_sns = self.sns_patcher.start()

    def tearDown(self):
        # self.s3_patcher.stop()
        # self.sqs_patcher.stop()
        # self.sns_patcher.stop()
        patch.stopall()

    def test_save_file(self):
        event = {
            "headers": {"x-api-key": "xxx"},
            "body": json.dumps(
                {
                    "data": "Zm9v",
                    "content_type": "text/plain",
                    "filename": "foo.txt",
                }
            ),
        }

        expected = {"statusCode": 201, "body": json.dumps({"message": "created"})}

        response = handlers.save_file(event, None)

        self.assertDictEqual(response, expected)

        self.m_s3.return_value.put_object.assert_called_once()

        queue_url = "https://sqs.us-east-1.amazonaws.com/123/callback"
        payload = {"cliente_token": "xxx", "bucket": "my-bucket", "key": "foo.txt"}

        self.m_sqs.return_value.send_message.assert_called_once_with(
            QueueUrl=queue_url, MessageBody=json.dumps(payload)
        )

        self.assertEqual(self.m_sns.return_value.publish.call_count, 1)
