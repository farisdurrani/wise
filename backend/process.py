import pandas as pd
import json
from multiprocessing import Pool, cpu_count
import re
from nltk.corpus import wordnet
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

INPUT_COL_NAME = "Text"
STOPWORDS_PATH = "../data/stopwords.json"
books = {
    "Bible": {"path": "../data/net_bible.csv"},
    "Quran": {"path": "../data/Quran_English.csv"},
    "Meditations": {"path": "../data/meditations.csv"}
}


def remove_symbols(string):
    return re.sub(r'[^\w\s]', '', string)


def create_bag_of_words(text: str) -> dict:
    """
    Creates a bag of words from a text
    :param text: The text to create the bag of words from
    :return: A dictionary with the words as keys and the number of occurrences as values
    """
    with open(STOPWORDS_PATH) as f:
        stopWordsList = json.load(f)["stopwords"]

    stopWordsSet = set(stopWordsList)

    words = [remove_symbols(word).lower() for word in text.split(" ") if
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


def find_best_sentence(question: str, book: str) -> str:
    """
    Finds the best sentence from the input bag of words
    :param question: The question to find the best sentence for
    :return: The best sentence
    """
    question_bag_of_words = create_bag_of_words(question)
    synonymized_bow = produce_synonym_dict([question_bag_of_words])[0]
    best_sentence_i = -1
    best_sentence_similarity = 0
    book_dict = books[book]
    input_bag_of_words = book_dict["input_bag_of_words"]
    for i, input_bow in enumerate(input_bag_of_words):
        similarity = compare_bag_of_words(input_bow, synonymized_bow)
        if similarity > best_sentence_similarity:
            best_sentence_similarity = similarity
            best_sentence_i = i
        if i % 100 == 0:
            print(f"Completed {i + 1} / {len(input_bag_of_words)}")
    print("best_sentence_i", best_sentence_i)
    return book_dict['sentences'][best_sentence_i]


def create_input_bag_of_words() -> None:
    """
    Creates a list of bag of words from the input dataframe
    :return: A list of bag of words
    """
    for book_name, book_dict in books.items():
        df = pd.read_csv(book_dict["path"])
        book_dict["sentences"] = remove_negatives(df[INPUT_COL_NAME])
        with Pool(cpu_count()) as p:
            inp_bag_of_words = p.map(create_bag_of_words, book_dict["sentences"])
        book_dict["input_bag_of_words"] = produce_synonym_dict(inp_bag_of_words)


def remove_negatives(sentences: list[str]) -> list[str]:
    pos_sentences = []
    analyzer = SentimentIntensityAnalyzer()
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        if (vs['compound']) < -.05:
            continue
        else:
            pos_sentences.append(sentence)
    return pos_sentences


def find_root_synonym(word):
    root_synonym = word
    synsets = wordnet.synsets(word)
    if synsets:
        # Choose the first synset
        synset = synsets[0]
        # Get the root hypernym of the first synset
        root_hypernym = synset.root_hypernyms()[0]
        # Get the first lemma of the root hypernym
        root_synonym = root_hypernym.lemmas()[0].name()
    return root_synonym


def produce_synonym_dict(input_dict: list[dict]) -> list[dict]:
    root_list = []  # updated list with root synonyms

    for in_dict in input_dict:
        root_dict = {}  # creates a new root dictionary for each dictionary read
        # print(root_dict)
        seen = set()  # keeps track of which keys have been seen
        # syn_seen = {}
        for key, value in in_dict.items():
            # print(key, value)
            root_syn = find_root_synonym(key)
            if root_syn == 'entity':
                continue
            # check if seen
            if root_syn in seen:
                # add value to value for relevant key in root dictionary
                # continue without adding root to dict
                old_val = root_dict[root_syn]
                root_dict[root_syn] = old_val + value
            else:
                root_dict[root_syn] = value
                seen.add(root_syn)
        root_list.append(root_dict)
    return root_list
