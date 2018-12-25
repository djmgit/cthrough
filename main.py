from flask import Flask, redirect, url_for, request, jsonify, render_template, g, flash
import json
import re
import os
from csim import Csim

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

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)


