# Required imports
import os

from flask import Flask

# Esse import precisa ser depois do 'initialize_app'
from routes import bp

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(bp)

port = int(os.environ.get("PORT", 8080))

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=port)
