from flask import Flask, abort, jsonify, send_from_directory
from flask import request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import requests
import time
import os
import jwt
import sys
import json

app = Flask(__name__, static_folder = 'react_app/build')
cred = credentials.ApplicationDefault();
firebase_admin.initialize_app(cred, {
    'projectId': 'engineering-capstone'
})

db = firestore.client()

# AutoML prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Grab the json body
    body = request.get_json()

    # See if the image exists if it doesn't abort
    try:
        base64 = body['photo']['base64']
    except:
        abort(400)

    # Get the current time and create a jwt token for the api
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

    #Post to the model and return the response
    response = requests.post('https://automl.googleapis.com/v1beta1/projects/engineering-capstone/locations/us-central1/models/ICN2044687123149108018:predict', json = {'payload': {'image': { 'imageBytes': str(base64)}}}, headers={'Authorization':'Bearer ' + signed_jwt.decode("utf-8")})
    responseJson = response.json();
    doc_ref = db.collection(u'activities').document(u'houseA')

    doc = doc_ref.get()
    activities = doc.to_dict()
    print(activities)
    if activities != None:
        activitiesArray = activities.get('activities')
        activitiesArray.append({'confidence': responseJson['payload'][0]['classification']['score'], 'label': responseJson['payload'][0]['displayName'], 'time': datetime.datetime.now()})
        db.collection(u'activities').document('houseA').set({'activities': activitiesArray}) 
    else:
        db.collection(u'activities').document('houseA').set({'activities': [{'confidence': responseJson['payload'][0]['classification']['score'], 'label': responseJson['payload'][0]['displayName'], 'time': datetime.datetime.now()}]}) 
    return response.text

@app.route('/')
def serve_static_index():
    return send_from_directory('react_app/build/', 'index.html')

@app.route('/static/<path:path>') # serve whatever the client requested in the static folder
def serve_static(path):
    return send_from_directory('react_app/build/static/', path)

@app.route('/service-worker.js')
def serve_worker():
    return send_from_directory('react_app/build/', 'service-worker.js')

if __name__ == "__main__":
    app.run()
