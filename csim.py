from simlib import SimLib

class Csim:
	def __init__(self):
		self.slib = SimLib()

	def find_sim_between_two(self, doc1, doc2):
		self.slib.set_data_and_find_sim(doc1, doc2)
		return self.slib.get_response()

	def find_similar_docs(self, primary_doc, list_of_docs, threshold=0.5):
		similar_docs = []

		for doc in list_of_docs:
			score = self.slib.set_data_and_find_sim(primary_doc.get('content'), doc.get('content')).get_response()
			if score > threshold:
				similar_docs.append({
					"name": doc.get("name"),
					"score": score 
				})

		return similar_docs

	def find_similarity_pairs(self, list_of_docs):
		response = []

		for index_i in range(len(list_of_docs)):
			for index_j in range(index_i + 1, len(list_of_docs)):
				doc1 = list_of_docs[index_i]
				doc2 = list_of_docs[index_j]
				score = self.find_sim_between_two(doc1.get("content"), doc2.get("content"))
				response.append({
					"docs": [doc1.get("name"), doc2.get("name")],
					"score": score
				})

		return response

	def get_cluster_id(self, clusters, doc):
		for index in range(len(clusters)):
			cluster = clusters[index]
			if doc in cluster:
				return index
		return None

	def cluster_docs(self, list_of_docs, threshold=0.5):
		clusters = []
		has_cluster = {}

		for index_i in range(len(list_of_docs)):
			for index_j in range(index_i + 1, len(list_of_docs)):
				doc1 = list_of_docs[index_i]
				doc2 = list_of_docs[index_j]
				if has_cluster.get(doc1.get("name")) and has_cluster.get(doc2.get("name")):
					continue
				score = self.find_sim_between_two(doc1.get("content"), doc2.get("content"))

				doc1_cluster_id = self.get_cluster_id(clusters, doc1.get("name"))
				doc2_cluster_id = self.get_cluster_id(clusters, doc2.get("name"))

				if doc1_cluster_id == None and doc2_cluster_id == None:
					clusters.append([doc1.get("name"), doc2.get("name")])
					has_cluster[doc1.get("name")] = 1
					has_cluster[doc2.get("name")] = 1
				elif doc1_cluster_id == None and doc2_cluster_id != None:
					clusters[doc2_cluster_id].append(doc1.get("name"))
				elif doc1_cluster_id != None and doc2_cluster_id == None:
					clusters[doc1_cluster_id].append(doc2.get("name"))

		return clusters


