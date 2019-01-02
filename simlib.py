from knowledge_extractor import KnowledgeExtractor
from imageinfo_extractor import ImageInfoExtractor
from stopwords import stopwords
import imp
import sys
import json
import tokenizer
'''
	hack for aws lambda sqlite issue
'''
sys.modules["sqlite"] = imp.new_module("sqlite")
sys.modules["sqlite3.dbapi2"] = imp.new_module("sqlite.dbapi2")
from nltk import PorterStemmer

class SimLib:
	def __init__(self, doc1="", doc2=""):
		self.porter = PorterStemmer()
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
			keywords = [self.porter.stem(k.lower()) for k in keywords]
			word_list += keywords

		# extract entities also
		entity_data = resource.get('entity_data').get('Entities')
		for entity_obj in entity_data:
			entity = entity_obj['Text']

			# same as keywords, split if more that one word
			entities = entity.split()
			entities = [self.porter.stem(e.lower()) for e in entities]
			word_list += entities

		# remove stopwords
		word_list = [w for w in word_list if w not in stopwords]

		# count occurences
		count_vect = {}
		for word in word_list:
			count_vect[word] = count_vect.get(word, 0) + 1

		return count_vect

	def get_word_vector_tokn(self, doc):
		word_list = []

		for token in tokenizer.tokenize(doc):
			if token.kind == tokenizer.TOK.WORD:
				word_list.append(token.txt)

		word_list = [self.porter.stem(w.lower()) for w in word_list]

		# count word occurences

		count_vect = {}
		for word in word_list:
			count_vect[word] = count_vect.get(word, 0) + 1

		return count_vect

	def get_cos_vector(self, all_words, word_vect):
		vector = [0 for w in all_words]
		index = 0

		for word in all_words:
			vector[index] = word_vect.get(word, 0)
			index += 1

		return vector

	def get_mod(self, vect):
		sum_square = sum([v*v for v in vect])
		return float(sum_square**0.5)

	def get_dot_product(self, vect1, vect2):
		dot_product = sum([v1 * v2 for v1, v2 in zip(vect1, vect2)])
		return dot_product

	def get_cos_sim(self, vect1, vect2):
		costheta = float(self.get_dot_product(vect1, vect2) / (self.get_mod(vect1) * self.get_mod(vect2)))
		return costheta

	def findsim(self):
		kextractor = KnowledgeExtractor()
		kextractor.set_text_and_extract(self.doc1)
		resource1 = kextractor.get_response()

		kextractor.set_text_and_extract(self.doc2)
		resource2 = kextractor.get_response()

		#print (self.doc1)
		#print (self.doc2)

		#print (json.dumps(resource1, indent=4))
		#print (json.dumps(resource2, indent=4))

		word_vect_doc1 = self.get_word_vector(resource1)
		word_vect_doc2 = self.get_word_vector(resource2)

		if len(word_vect_doc1.keys()) == 0 or len(word_vect_doc2.keys()) == 0:
			print ("comprehend is not able to return keywords or entities, use tokenizer")
			word_vect_doc1 = self.get_word_vector_tokn(self.doc1)
			word_vect_doc2 = self.get_word_vector_tokn(self.doc2)

		print (word_vect_doc1)
		print (word_vect_doc2)

		all_words = list(word_vect_doc1.keys()) + list(word_vect_doc2.keys())
		all_words = list(set(all_words))

		#print (all_words)

		cos_vect1 = self.get_cos_vector(all_words, word_vect_doc1)
		cos_vect2 = self.get_cos_vector(all_words, word_vect_doc2)

		#print (cos_vect1)
		#print (cos_vect2)

		cos_sim = self.get_cos_sim(cos_vect1, cos_vect2)
		self.response = cos_sim

	def get_word_vector_img(self, resource):
		word_list = []
		labels = resource.get("label_data").get("Labels")

		for label in labels:
			label_text = label['Name']

			# label might consists of more than one word
			# we need to split it and add it to list as separate words
			label_words = label_text.split()
			label_words = [self.porter.stem(k.lower()) for k in label_words]
			word_list += label_words

		texts = resource.get("text_data").get("TextDetections")
		for text in texts:
			text_word = text['DetectedText']

			text_words = text_word.split()
			text_words = [self.porter.stem(k.lower()) for k in text_words]
			word_list += text_words

		# remove stopwords
		word_list = [w for w in word_list if w not in stopwords]

		# count occurences
		count_vect = {}
		for word in word_list:
			count_vect[word] = count_vect.get(word, 0) + 1

		return count_vect

	def findsim_img(self, img1, img2):
		iinfo_extractor = ImageInfoExtractor()
		iinfo_extractor.set_img_and_extract(img1)
		resource1 = iinfo_extractor.get_response()

		iinfo_extractor.set_img_and_extract(img2)
		resource2 = iinfo_extractor.get_response()

		word_vect_img1 = self.get_word_vector_img(resource1)
		word_vect_img2 = self.get_word_vector_img(resource2)

		print (word_vect_img1)
		print (word_vect_img2)

		all_labels = list(word_vect_img1.keys()) + list(word_vect_img2.keys())
		all_labels = list(set(all_labels))

		cos_vect1 = self.get_cos_vector(all_labels, word_vect_img1)
		cos_vect2 = self.get_cos_vector(all_labels, word_vect_img2)

		cos_sim = self.get_cos_sim(cos_vect1, cos_vect2)
		self.response = cos_sim

	def findsim_img_text(self, img, doc):
		iinfo_extractor = ImageInfoExtractor()
		iinfo_extractor.set_img_and_extract(img1)
		img_resource = iinfo_extractor.get_response()

		kextractor = KnowledgeExtractor()
		kextractor.set_text_and_extract(doc)
		txt_resource = kextractor.get_response()

		word_vect_txt = self.get_word_vector(txt_resource)

		word_vect_img = self.get_word_vector_img(img_resource)

		print (word_vect_txt)
		print (word_vect_img)

		all_words = list(word_vect_txt.keys()) + list(word_vect_img.keys())
		all_words = list(set(all_words))

		#print (all_words)

		cos_vect1 = self.get_cos_vector(all_words, word_vect_txt)
		cos_vect2 = self.get_cos_vector(all_words, word_vect_img)

		#print (cos_vect1)
		#print (cos_vect2)

		cos_sim = self.get_cos_sim(cos_vect1, cos_vect2)
		self.response = cos_sim


	def get_response(self):
		return self.response

# for testing
if __name__ == '__main__':
	#text1 = 'I live in India. I am from west bengal, kolkata'
	#text2 = 'I am from India. I have come from west bengal, kolkata'

	with open('/home/deep/cthrough/skate.jpg', 'rb') as image1:
		img1 = image1.read()
	with open('/home/deep/cthrough/skate1.jpg', 'rb') as image2:
		img2 = image2.read()
	txt = "A human loves skate boarding. I too have a skateboard at my house. I often use it in my garden while playing."

	slib = SimLib()
	slib.findsim_img_text(img1, txt)
	score = slib.get_response()
	print (score)
