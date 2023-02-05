import pandas as pd
import json
from multiprocessing import Pool

with open("../data/stopwords.json") as f:
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
  df = pd.read_csv("../data/meditations.csv")

  with Pool(5) as p:
      ee = p.map(create_bag_of_words, df["Text"])
      print(ee[0])

