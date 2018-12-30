'''
  This script creates an IAM role for our lambda function
'''

import json, boto3

role_policy_document = {
    "Version": "2018-12-30",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Action": [
                "comprehend:DetectDominantLanguage",
                "comprehend:DetectSentiment",
                "comprehend:DetectEntities",
                "comprehend:DetectKeyPhrases"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}


iam_client = boto3.client(service_name='iam', region_name='us-east-1')

iam_client.create_role(
  RoleName='CthroughLambda',
  AssumeRolePolicyDocument=json.dumps(role_policy_document),
)