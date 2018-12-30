import boto3

'''
	This script creates the lambda function
'''

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')

env_variables = dict() # Environment Variables

with open('cthrough_lambda.zip', 'rb') as f:
  zipped_code = f.read()

role = iam_client.get_role(RoleName='cthrough_lambda')

lambda_client.create_function(
  FunctionName='cthrough_lambda_func',
  Runtime='python3.6',
  Role=role['Role']['Arn'],
  Handler='lambda_handler.handler',
  Code=dict(ZipFile=zipped_code),
  Timeout=300, # Maximum allowable timeout
  Environment=dict(Variables=env_variables),
)
