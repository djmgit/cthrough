import boto3
import json

class KnowledgeExtractor:
	def __init__(self, text=""):
		self.comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
		self.response = {}
		if text:
			self.text = text
			self.extract_knowledge()

	def set_text(self, text):
		self.text = text

	def set_text_and_extract(self, text):
		self.text = text
		self.extract_knowledge()

	def extract_entities(self):
		entity_data = self.comprehend.detect_entities(Text=self.text, LanguageCode='en')
		return entity_data

	def extract_keywords(self):
		keyword_data = self.comprehend.detect_key_phrases(Text=self.text, LanguageCode='en')
		return keyword_data

	def determine_sentiment(self):
		sentiment_data = self.comprehend.detect_sentiment(Text=self.text, LanguageCode='en')
		return sentiment_data

	def extract_knowledge(self):
		self.response = {
			"entity_data": self.extract_entities(),
			"keyword_data": self.extract_keywords(),
			"sentiment_data": self.determine_sentiment()
		}

	def get_response(self):
		return self.response

if __name__ == "__main__":
	#sample_text = '''
		#Nowadays Artificial Intelligence in India is also making a change in IT industry. It is an area of Machine Learning algorithms having multiple layers for feature extraction and transformation of each successive layer using output from previous layer as an input.
		#Deep Learning and Data science includes learning of deep structured and unstructured representation of data and allow to build a solution optimized from algorithm to solve Machine Learning problems. It is fastest-growing field in machine learning using deep neural networks to abstract data such as images, sound and text. Thus Deep Learning has become growing trend in Artificial Intelligence to abstract better results when data is large and complex. Deep Learning consists of an artificial neural network which refers to the depth of the network. Neural networks are inspired by structure of cerebral cortex. Perceptron is the basic model of neural network.
	#'''

	sample_text = "I live in India. My parents are also from India. I like to eat burgers. Burger King is where you get burgers."

	extractor = KnowledgeExtractor(sample_text)
	response = extractor.get_response()
	print (json.dumps(response, sort_keys=True, indent=4))
