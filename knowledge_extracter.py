import boto3
import json

class KnowledgeExtractor:
	def __init__(self, text=""):
		self.comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
		self.response = {}
		if text:
			self.text = text
			self.extract_knowledge()

	def extract_entities(self):
		entity_data = self.comprehend.detect_entities(Text=self.text, LanguageCode='en')
		return json.dumps(entity_data, sort_keys=True, indent=4)

	
