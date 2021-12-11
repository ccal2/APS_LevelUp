# Required imports
import os

from flask import Flask
from routes import bp

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(threaded=True)

# port = int(os.environ.get("PORT", 8082))

# if __name__ == "__main__":
#     app.run(threaded=True, host="0.0.0.0", port=port)
