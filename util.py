'''
	some utility methods
'''

def is_valid_doc(doc):
	if doc.get("name") and doc.get("content"):
		return True
	return False

def is_valid_list(docs):
	for doc in docs:
		if doc.get("name") and doc.get("content"):
			continue
		else:
			return False
	return False

def build_response(status, data):
	response = {
		"status": status,
		"data": data
	}

	return response
