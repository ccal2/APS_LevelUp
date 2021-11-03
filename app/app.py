# Required imports
from flask import Flask
from firebase_admin import credentials, initialize_app

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('app/serviceAccountKey.json')
default_app = initialize_app(cred)
