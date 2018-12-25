from knowledge_extractor import KnowledgeExtractor
from stopwords import stopwords

class SimLib:
	def __init__(self, doc1="", doc2=""):
		if doc1 and doc2:
			self.doc1 = doc1
			self.doc2 = doc2
	
			self.findsim()

	def set_data_and_find_sim(self, doc1, doc2):
		self.doc1 = doc1
		self.doc2 = doc2

		self.findsim()

	def get_word_vector(self, resource):
		word_list = []

		keyword_data = resource.get('keyword_data').get('KeyPhrases')
		for key_obj in keyword_data:
			keyword = key_obj['Text']

			# keyword might consists of more than one word
			# we need to split it and add it to list as separate words
			keywords = keyword.split()
			word_list += keywords

		# remove stopwords
		word_list = [w if w not in stopwords]

		return word_list

	def findsim(self):
		kextractor = KnowledgeExtractor()
		kextractor.set_text_and_extract(doc1)
		resource1 = kextractor.get_response()

		kextractor.set_text_and_extract(doc2)
		resource2 = kextractor.get_response()

		word_vect_doc1 = self.get_word_vector(resource1)
		word_vect_doc2 = self.get_word_vector(resource2)

		all_words = word_vect_doc1 + word_vect_doc2
		all_words = list(set(all_words))

		count_vect1 = self.get_count_vects(all_words, doc1)



