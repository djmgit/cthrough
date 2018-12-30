import boto3

lambda_client = boto3.client('lambda')

with open('cthrough_lambda.zip', 'rb') as f:
  zipped_code = f.read()

lambda_client.update_function_code(
  FunctionName='cthrough_lambda_func',
  ZipFile=zipped_code,
)
