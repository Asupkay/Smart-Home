from flask import Flask, abort, jsonify
from flask import request
import requests
import time
import os
import jwt
import sys
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
        #return jsonify({'success': True, 'identification': { 'name':'Alex Supkay' }})
    except:
        abort(400)

    iat = time.time()
    exp = iat + 3600
    payload = {'iss': 'automl@engineering-capstone.iam.gserviceaccount.com',
               'sub': 'automl@engineering-capstone.iam.gserviceaccount.com',
               'aud': 'https://automl.googleapis.com/google.cloud.automl.v1beta1.PredictionService',
               'iat': iat,
               'exp': exp}

    PRIVATE_KEY_FROM_JSON = os.environ['PRIVATE_KEY_FROM_JSON']
    PRIVATE_KEY_ID_FROM_JSON = os.environ['PRIVATE_KEY_ID_FROM_JSON']

    additional_headers = {'kid': PRIVATE_KEY_ID_FROM_JSON}
    signed_jwt = jwt.encode(payload, PRIVATE_KEY_FROM_JSON, headers = additional_headers, algorithm = 'RS256')

    response = requests.post('https://automl.googleapis.com/v1beta1/projects/engineering-capstone/locations/us-central1/models/ICN2044687123149108018:predict', json = {'payload': {'image': { 'imageBytes': str(base64)}}}, headers={'Authorization':'Bearer ' + signed_jwt.decode("utf-8")})
    return response.text;

