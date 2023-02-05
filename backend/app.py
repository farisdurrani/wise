from flask import Flask, request
from flask_cors import CORS
from process import find_best_sentence, create_input_bag_of_words, upload_new_book

app = Flask(__name__)
CORS(app)

PORT = 8000


@app.route("/")
def hello_world():
    return {"hello": "world"}


@app.route("/api/question", methods=["POST", "GET"])
def process_question():
    question = request.args.getlist("question")[0]
    book = request.args.getlist("book")[0]
    best_sentence = find_best_sentence(question, book)
    return {"best_sentence": best_sentence}


@app.route("/api/upload", methods=['POST'])
def add_new_book():
    data = request.form.get('book_csv')
    title = request.form.get("title")
    return upload_new_book(data, title)


if __name__ == "__main__":
    create_input_bag_of_words()
    app.run(debug=True, host="0.0.0.0", port=PORT)
