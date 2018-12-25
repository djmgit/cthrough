from knowledge_extractor import KnowledgeExtractor
from stopwords import stopwords

class SimLib:
	def __init__(self, doc1, doc2):
		self.doc1 = doc1
		self.doc2 = doc2

		self.findsim()

	def set_data_and_find_sim(self, doc1, doc2):
		self.doc1 = doc1
		self.doc2 = doc2

		self.findsim()
