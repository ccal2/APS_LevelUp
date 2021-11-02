# Required imports
import os
from app import app


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


port = int(os.environ.get("PORT", 8080))
if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=port)
