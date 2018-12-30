'''
  This script creates an IAM role for our lambda function
'''

import json, boto3

role_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "sts:AssumeRole"
            ]
        },
        {
            "Action": [
                "comprehend:*",
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "iam:ListRoles",
                "iam:GetRole",
                "sts:AssumeRole"
            ],
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            }
        }
    ]
}


iam_client = boto3.client('iam')

iam_client.create_role(
  RoleName='CthroughLambda',
  AssumeRolePolicyDocument=json.dumps(role_policy_document),
)