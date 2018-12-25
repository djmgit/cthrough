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

		# count occurences
		count_vect = {}
		for word in word_list:
			count_vect[word] = count_vect.get(word, 0) += 1

		return count_vect

	def get_cos_vector(self, all_words, word_vect):
		vector = []
		index = 0

		for word in all_words:
			vector[index] = word_vect.get(word, 0)
			index += 1

		return vector

	def get_mod(self, vect):
		sum_square = sum([v*v for v in vect])
		return float(sum_square**0.5)

	def get_cos_sim(self, vect1, vect2):
		# calculate 

	def findsim(self):
		kextractor = KnowledgeExtractor()
		kextractor.set_text_and_extract(doc1)
		resource1 = kextractor.get_response()

		kextractor.set_text_and_extract(doc2)
		resource2 = kextractor.get_response()

		word_vect_doc1 = self.get_word_vector(resource1)
		word_vect_doc2 = self.get_word_vector(resource2)

		all_words = word_vect_doc1.keys() + word_vect_doc2.keys()
		all_words = list(set(all_words))

		cos_vect1 = self.get_cos_vector(all_words, word_vect_doc1)
		cos_vect2 = self.get_cos_vector(all_words, word_vect_doc2)

		cos_sim = self.get_cos_sim(cos_vect1, cos_vect2)





