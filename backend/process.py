import pandas as pd
import json
from multiprocessing import Pool, cpu_count

INPUT_COL_NAME = "Text"
df = None
input_bag_of_words = None


def create_bag_of_words(text: str) -> dict:
    """
    Creates a bag of words from a text
    :param text: The text to create the bag of words from
    :return: A dictionary with the words as keys and the number of occurrences as values
    """
    with open("/Users/fdurrani/LocalGithub/Foreign/wise/backend/data/stopwords.json") as f:
        stopWordsList = json.load(f)["stopwords"]

    stopWordsSet = set(stopWordsList)

    words = [word.lower() for word in text.translate({ord(c): None for c in ".?!\"':;%*@[]("}).split(" ") if
             word not in stopWordsSet]
    bag_of_words = {}
    for word in words:
        if word in bag_of_words:
            bag_of_words[word] += 1
        else:
            bag_of_words[word] = 1
    return bag_of_words


def compare_bag_of_words(bag_of_words_1: dict, bag_of_words_2: dict) -> int:
    """
    Compares two bag of words

    :param bag_of_words_1: The first bag of words
    :param bag_of_words_2: The second bag of words
    :return: The similarity of the two bag of words
    """
    similarity = 1
    for word1 in bag_of_words_1.keys():
        if word1 in bag_of_words_2:
            similarity += bag_of_words_1[word1] * bag_of_words_2[word1]
    return similarity


def find_best_sentence(question: str) -> str:
    """
    Finds the best sentence from the input bag of words
    :param question: The question to find the best sentence for
    :return: The best sentence
    """
    question_bag_of_words = create_bag_of_words(question)
    best_sentence_i = -1
    best_sentence_similarity = 0
    for i, input_bow in enumerate(input_bag_of_words):
        similarity = compare_bag_of_words(input_bow, question_bag_of_words)
        if similarity > best_sentence_similarity:
            best_sentence_similarity = similarity
            best_sentence_i = i
        print(f"Completed {i + 1} / {len(input_bag_of_words)}")
    return df[INPUT_COL_NAME][best_sentence_i]


def create_input_bag_of_words() -> None:
    """
    Creates a list of bag of words from the input dataframe
    :return: A list of bag of words
    """
    global df
    global input_bag_of_words
    df = pd.read_csv("/Users/fdurrani/LocalGithub/Foreign/wise/backend/data/meditations.csv")
    with Pool(cpu_count()) as p:
        inp_bag_of_words = p.map(create_bag_of_words, df[INPUT_COL_NAME])
    input_bag_of_words = inp_bag_of_words

