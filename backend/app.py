from flask import Flask
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

#bag of words
with open("stopwords.json") as f:
    stopWordsList = json.load(f)["stopwords"]

stopWordsSet = set(stopWordsList)

def create_bag_of_words(text):
    words = [word.lower() for word in text.replace("[.?!\"':;%*@#]", "").split(" ") if word not in stopWordsSet]
    bag_of_words = {}
    for word in words:
        if word in bag_of_words:
            bag_of_words[word] += 1
        else:
            bag_of_words[word] = 1
    return bag_of_words

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)

