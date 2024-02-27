from flask import Flask, request, jsonify
from flask.helpers import send_file

app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def indexPage():
     return send_file("web/index.html")  

@app.route("/add")
def add():
    # Retrieve two numbers from query parameters, defaulting to 0 if not provided
    a = request.args.get('a', default=0, type=int)
    b = request.args.get('b', default=0, type=int)
    # Calculate the sum of the two numbers
    result = a + b
    # Return the result as JSON
    return jsonify(sum=result)