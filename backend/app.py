from flask import Flask, request
from flask_cors import CORS
import os
import json

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


@app.route("/api/question", methods=["POST", "GET"])
def process_question():
    question = request.args.getlist('question')
    return {"question": 12}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)

