# Required imports
import os

from flask import Flask
from firebase_admin import credentials, initialize_app

# Initialize Firestore DB
cred = credentials.Certificate("serviceAccountKey.json")
default_app = initialize_app(cred)

# Esse import precisa ser depois do 'initialize_app'
from routes import bp

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(bp)

port = int(os.environ.get("PORT", 5002))

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=port)
