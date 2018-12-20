import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text = "I want to eat a burger. I like burger more that pizza. I love burgers from McDonalds. However Domino's pizza is good."

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectEntities\n')