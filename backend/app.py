from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

PORT = os.getenv("PORT")
if PORT is not None:
    PORT = int(PORT)
else:
    PORT = 8000

@app.route("/")
def hello_world():
    return {"hello": "world"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
