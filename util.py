'''
	some utility methods
'''

import json

def is_valid_doc(doc):
	if not doc:
		return False
	if doc.get("name") and doc.get("content"):
		return True
	return False

def is_valid_list(docs):
	if not docs:
		return False
	for doc in docs:
		if doc.get("name") and doc.get("content"):
			continue
		else:
			print (doc)
			return False
	return True

def is_valid_threshold(threshold):
	if threshold < 0 or threshold > 1:
		return False
	return True

def build_response(status, data):
	response = {
		"status": status,
		"data": data
	}

	return response

def is_valid_op(operation):
	valid_ops = [
		"find_sim_between_two",
		"find_similar_docs",
		"find_similar_pairs",
		"cluster_docs",
		"find_sim_between_two_images",
		"find_sim_between_image_text",
		"find_docs_similar_to_image",
		"find_images_similar_to_doc",
		"cluster_images"

	]

	if not operation or operation not in valid_ops:
		return False

	return True

def conv_to_obj(param):
	if type(param).__name__ == "str":
		return json.loads(param)
	return param
