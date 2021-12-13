import os

from flask import Flask
from routes import bp
from dotenv import load_dotenv


load_dotenv()
FLASK_APP_SECRET_KEY = os.getenv("FLASK_APP_SECRET_KEY")

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(bp)
app.secret_key = FLASK_APP_SECRET_KEY

port = int(os.environ.get("PORT", 5003))

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=port)
