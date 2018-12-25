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
	pass


