from flask import Flask, abort, jsonify
from flask import request
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    body = request.get_json()
    try:
        base64 = body['photo']['base64']
        return jsonify({'success': True, 'identification': { 'name':'Alex Supkay' }})
    except:
        abort(400)
