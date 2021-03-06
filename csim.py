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
			self.slib.set_data_and_find_sim(primary_doc.get('content'), doc.get('content'))
			score = self.slib.get_response()
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

		for index_i in range(len(list_of_docs)):
			for index_j in range(index_i + 1, len(list_of_docs)):
				doc1 = list_of_docs[index_i]
				doc2 = list_of_docs[index_j]
				score = self.find_sim_between_two(doc1.get("content"), doc2.get("content"))
				#print (doc1.get("name"), doc2.get("name"), score)

				doc1_cluster_id = self.get_cluster_id(clusters, doc1.get("name"))
				doc2_cluster_id = self.get_cluster_id(clusters, doc2.get("name"))

				#print (doc1_cluster_id, doc2_cluster_id)

				if score > threshold:
					if doc1_cluster_id == None and doc2_cluster_id == None:
						clusters.append([doc1.get("name"), doc2.get("name")])
					elif doc1_cluster_id == None and doc2_cluster_id != None:
						clusters[doc2_cluster_id].append(doc1.get("name"))
					elif doc1_cluster_id != None and doc2_cluster_id == None:
						clusters[doc1_cluster_id].append(doc2.get("name"))
					else:
						clusters[doc1_cluster_id] += clusters[doc2_cluster_id]
						del clusters[doc2_cluster_id]
				else:
					if doc1_cluster_id == None:
						clusters.append([doc1.get("name")])
					if doc2_cluster_id == None:
						clusters.append([doc2.get("name")])

		return clusters

	def find_sim_between_two_img(self, img1, img2):
		self.slib.findsim_img(img1, img2)
		return self.slib.get_response()

	def find_sim_between_img_txt(self, img, text):
		self.slib.findsim_img_text(img, text)
		return self.slib.get_response()

	def docs_similar_to_img(self, primary_image, list_of_docs, threshold=0.5):
		similar_docs = []

		for doc in list_of_docs:
			score = self.find_sim_between_img_txt(primary_image.get("content"), doc.get("content"))
			if score > threshold:
				similar_docs.append({
					"name": doc.get("name"),
					"score": score 
				})

		return similar_docs

	def images_similar_to_doc(self, primary_doc, list_of_images, threshold=0.5):
		similar_images = []

		for image in list_of_images:
			score = self.find_sim_between_img_txt(image.get("content"), primary_doc.get("content"))
			if score > threshold:
				similar_images.append({
					"name": image.get("name"),
					"score": score
				})
		return similar_images

	def cluster_img(self, list_of_images, threshold=0.5):
		clusters = []

		for index_i in range(len(list_of_images)):
			for index_j in range(index_i + 1, len(list_of_images)):
				img1 = list_of_images[index_i]
				img2 = list_of_images[index_j]
				score = self.find_sim_between_two_img(img1.get("content"), img2.get("content"))
				#print (doc1.get("name"), doc2.get("name"), score)

				img1_cluster_id = self.get_cluster_id(clusters, img1.get("name"))
				img2_cluster_id = self.get_cluster_id(clusters, img2.get("name"))

				#print (doc1_cluster_id, doc2_cluster_id)

				if score > threshold:
					if img1_cluster_id == None and img2_cluster_id == None:
						clusters.append([img1.get("name"), img2.get("name")])
					elif img1_cluster_id == None and img2_cluster_id != None:
						clusters[img2_cluster_id].append(img1.get("name"))
					elif img1_cluster_id != None and img2_cluster_id == None:
						clusters[img1_cluster_id].append(img2.get("name"))
					else:
						clusters[img1_cluster_id] += clusters[img2_cluster_id]
						del clusters[img2_cluster_id]
				else:
					if img1_cluster_id == None:
						clusters.append([img1.get("name")])
					if img2_cluster_id == None:
						clusters.append([img2.get("name")])

		return clusters

if __name__ == "__main__":
	csim = Csim()

	doc1 = {"name":"test1.txt", "content": "I love burgers. Burger king is good for burgers. Whopper is best"}
	doc2 = {"name":"test2.txt", "content": "I love burgers too. Burger king is good but McDonalds is better. It has got lots of options"}
	doc3 = {"name":"test3.txt", "content": "I do not like burgers. I love pizzas. Dominos pizzas are great. I just love them"}
	doc4 = {"name":"test4.txt", "content": "I love cheese burst pizzas. Dominos and smokin joe are great pizza shops."}
	doc5 = {"name":"test5.txt", "content": "I do not like fast food. I like to eat home made food more."}

	#list_of_docs = [doc1, doc2, doc3, doc4, doc5]
	#print (csim.find_sim_between_two(doc1['content'], doc2['content']))
	#print ("\n")
	#print (csim.find_similar_docs(doc1, [doc2, doc3, doc4, doc5], 0.5))
	#print ("\n")
	#print (csim.find_similarity_pairs(list_of_docs))
	#print ("\n")
	#print (csim.cluster_docs(list_of_docs, 0.4))

	doc1 = {"name": "test1.txt", "content": "A human loves skate boarding. I too have a skateboard at my house. I often use it in my garden while playing."}
	doc2 = {"name": "test2.txt", "content": "i love burgers very much."}
	with open('/home/deep/cthrough/skate.jpg', 'rb') as image1:
		img1 = image1.read()

	with open('/home/deep/cthrough/basket.jpg', 'rb') as image2:
		img2 = image2.read()

	with open('/home/deep/cthrough/skate.jpg', 'rb') as image3:
		img3 = image3.read()

	img1 = {"name": "img1", "content": img1}
	img2 = {"name": "img2", "content": img2}
	img3 = {"name": "img3", "content": img3}

	print (csim.cluster_img([img1, img2, img3], 0.2))




