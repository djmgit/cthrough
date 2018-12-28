'''
	some utility methods
'''

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
			return False
	return False

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
