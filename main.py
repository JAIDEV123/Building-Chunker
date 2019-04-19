import sqlalchemy, sys
from sqlalchemy import create_engine
from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from model import data

app = Flask(__name__)

# database for the forum posts, the experiment it is used for 
database = data()

# Standard Routes for all web pages, the function names are used in the html for all anchor links

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html");

@app.route("/Experiment", methods=["GET", "POST"])
def experiments():
	return render_template("experiments.html");

@app.route("/Contribute", methods=["GET", "POST"])
def contribute():
	return render_template("contribute.html");

@app.route("/Building-Chunker", methods=["GET", "POST"])
def buildingchunker():
	return render_template("Experiments/Building-Chunker/index.html")

@app.route("/New", methods=["GET"])
def new():
	return render_template("new.html", posts = database.retrievepost())

@app.route("/Forum", methods=["GET"])
def forum():
	return render_template("new.html", posts = database.retrievepost())

@app.route("/New", methods=["POST"])
def createpost():
	new = request.get_json()
	database.createpost(new)
	print(request.get_json(), file=sys.stderr)
	return request.data

if __name__ == '__main__':
	app.run(debug=True)