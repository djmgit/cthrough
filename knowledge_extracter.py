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
		return entity_data

	def extract_keywords(self):
		keyword_data = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
		return keyword_data

	def determine_sentiment(self):
		sentiment_data = comprehend.detect_sentiment(Text=text, LanguageCode='en')
		return sentiment_data
		
