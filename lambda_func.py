'''
 This is the handler method for aws lambda
'''

import json
from csim import Csim
from util import *

sim_handler = Csim()

def find_sim_between_two(doc1, doc2):
	if doc1 and doc2:
		score = sim_handler.find_sim_between_two(doc1, doc2)
		response = {
			"status": "OK",
			"data": {
				"score": score
			}
		}
	else:
		response = {
			"status": "FAILED",
			"data": "NOT ENOUGH PARAMETERS"
		}

	return response

def find_similar_docs(primary_doc, list_of_docs, threshold=None):
	if threshold != None:
		threshold = float(threshold)

	if not is_valid_doc(primary_doc):
		return build_response("FAILED", "INVALID PRIMARY DOC")
	if not is_valid_list(list_of_docs):
		return build_response("FAILED", "INVALID LIST OF DOCS")
	if threshold and not is_valid_threshold(threshold):
		return build_response("FAILED", "INVALID THRESHOLD")

	data = ""
	if threshold != None:
		data = sim_handler.find_similar_docs(primary_doc, list_of_docs, threshold)
	else:
		data = sim_handler.find_similar_docs(primary_doc, list_of_docs)

	return build_response("OK", data)

def find_similar_pairs(list_of_docs):
	if not is_valid_list(list_of_docs):
		return build_response("FAILED", "INVALID LIST OF DOCS")

	data = sim_handler.find_similarity_pairs(list_of_docs)

	return build_response("OK", data)

def cluster_docs(list_of_docs, threshold=None):
	if threshold != None:
		threshold = float(threshold)

	if not is_valid_list(list_of_docs):
		return build_response("FAILED", "INVALID LIST OF DOCS")
	if threshold and not is_valid_threshold(threshold):
		return build_response("FAILED", "INVALID THRESHOLD")

	data = ""
	if threshold:
		data = sim_handler.cluster_docs(list_of_docs, threshold)
	else:
		data = sim_handler.cluster_docs(list_of_docs)

	return build_response("OK", data)

def find_sim_between_two_images(img1, img2):
	if img1 and img2:
		score = sim_handler.find_sim_between_two_img(img1, img2)
		response = {
			"status": "OK",
			"data": {
				"score": score
			}
		}
	else:
		response = {
			"status": "FAILED",
			"data": "NOT ENOUGH PARAMETERS"
		}

	return response

def find_sim_between_image_text(img, doc):
	if img and doc:
		score = sim_handler.find_sim_between_img_txt(img, doc)
		response = {
			"status": "OK",
			"data": {
				"score": score
			}
		}
	else:
		response = {
			"status": "FAILED",
			"data": "NOT ENOUGH PARAMETERS"
		}

	return response

def find_docs_similar_to_image(primary_image, list_of_docs, threshold=0.5):
	if threshold != None:
		threshold = float(threshold)

	if not is_valid_doc(primary_image):
		return build_response("FAILED", "INVALID PRIMARY IMAGE")
	if not is_valid_list(list_of_docs):
		return build_response("FAILED", "INVALID LIST OF DOCS")
	if threshold and not is_valid_threshold(threshold):
		return build_response("FAILED", "INVALID THRESHOLD")

	data = ""
	if threshold != None:
		data = sim_handler.docs_similar_to_img(primary_doc, list_of_docs, threshold)
	else:
		data = sim_handler.docs_similar_to_img(primary_doc, list_of_docs)

	return build_response("OK", data)

def find_images_similar_to_doc(primary_doc, list_of_images, threshold=0.5):
	if threshold != None:
		threshold = float(threshold)

	if not is_valid_doc(primary_doc):
		return build_response("FAILED", "INVALID PRIMARY DOC")
	if not is_valid_list(list_of_images):
		return build_response("FAILED", "INVALID LIST OF IMAGES")
	if threshold and not is_valid_threshold(threshold):
		return build_response("FAILED", "INVALID THRESHOLD")

	data = ""
	if threshold != None:
		data = sim_handler.images_similar_to_doc(primary_doc, list_of_images, threshold)
	else:
		data = sim_handler.images_similar_to_doc(primary_doc, list_of_images)

	return build_response("OK", data)

def handler(event, context):
	operation = event.get("operation")
	print (event)

	if not is_valid_op(operation):
		return build_response("FAILED", "INVALID_OPERATION")

	if operation == "find_sim_between_two":
		return find_sim_between_two(event.get("doc1"), event.get("doc2"))

	if operation == "find_similar_docs":
		#primary_doc = conv_to_obj(event.get("primary_doc"))
		#list_of_docs = conv_to_obj(event.get("list_of_docs"))
		return find_similar_docs(event.get("primary_doc"), event.get("list_of_docs"), event.get("threshold"))

	if operation == "find_similar_pairs":
		return find_similar_pairs(event.get("list_of_docs"))

	if operation == "cluster_docs":
		return cluster_docs(event.get("list_of_docs"), event.get("threshold"))
