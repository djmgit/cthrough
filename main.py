from flask import Flask, redirect, url_for, request, jsonify, render_template, g, flash
import json
import re
import os
from csim import Csim
from util import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "THIS IS SECRET"
path = os.path.dirname(os.path.abspath(__file__))

sim_handler = Csim()

@app.route('/api/v1/find_sim_between_two', methods=["POST"])
def find_sim_between_two():
	json_data = request.json
	doc1 = json_data.get("doc1")
	doc2 = json_data.get("doc2")

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

	return jsonify(response)

@app.route('/api/v1/find_similar_docs', methods=["POST"])
def find_similar_docs():
	json_data = request.json
	primary_doc = json_data.get('primary_doc')
	list_of_docs = json_data.get("list_of_docs")
	threshold = json_data.get("threshold")

	if not is_valid(primary_doc):
		return jsonify(build_response("FAILED", "INVALID PRIMARY DOC"))
	if not is_valid(list_of_docs):
		return jsonify(build_response("FAILED", "INVALID LIST OF DOCS"))
	if threshold and not is_valid_threshold(threshold):
		return jsonify(build_response("FAILED", "INVALID THRESHOLD"))

	data = ""
	if threshold:
		data = sim_handler.find_similar_docs(primary_doc, list_of_docs, threshold)
	else:
		data = sim_handler.find_similar_docs(primary_doc, list_of_docs)

	return jsonify(build_response("FAILED", data))



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)


