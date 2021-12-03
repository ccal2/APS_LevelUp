# Required imports
import os

from flask import Flask
from firebase_admin import credentials, initialize_app
from dotenv import load_dotenv

from routes import bp

load_dotenv()
FLASK_APP_SECRET_KEY = os.getenv("FLASK_APP_SECRET_KEY")

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(bp)
app.secret_key = FLASK_APP_SECRET_KEY

# Initialize Firestore DB
cred = credentials.Certificate("app/serviceAccountKey.json")
default_app = initialize_app(cred)

port = int(os.environ.get("PORT", 8080))

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=port)
