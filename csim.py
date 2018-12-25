from simlib import SimLib

class Csim:
	def __init__(self):
		self.slib = SimLib()

	def find_sim_between_two(doc1, doc2):
		self.slib.set_data_and_find_sim(doc1, doc2)
		return self.slib.get_response()

	def find_similar_docs(primary_doc, list_of_docs, threshold=0.5):
		similar_docs = []

		for doc in list_of_docs:
			score = self.slib.set_data_and_find_sim(primary_doc.get('content'), doc.get('content')).get_response()
			if score > threshold:
				similar_docs.append({
					"name": doc.get("name"),
					"score": score 
				})

		return similar_docs
