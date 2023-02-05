import pandas as pd
import json
import nltk
from nltk.corpus import wordnet
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from multiprocessing import Pool

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


def remove_negatives(sentences):
    pos_sentences = []
    analyzer = SentimentIntensityAnalyzer()
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        if (vs['compound']) < -.05:
            #print(sentence)
            #print(vs['compound'])
            continue
        else:
            pos_sentences.append(sentence)
    return pos_sentences

#SYNONYM FUNCTION
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


if __name__ == "__main__":
   df = pd.read_csv("meditations.csv")
   #df = pd.read_csv("net_bible.csv")
   #df = pd.read_csv("Quran_English.csv")


ps = remove_negatives(df["Text"])
#print(ps)

with Pool(5) as p:
      ee = p.map(create_bag_of_words, ps)

#test ee
#ee = [{'from': 1, 'grandfather': 1, 'verus': 1, 'i': 1, 'learned': 1, 'morals': 1, 'government': 1, 'temper.': 1}, {'from': 1, 'reputation': 1, 'remembrance': 1, 'father,': 1, 'modesty': 2, 'manly': 1, 'character.': 1, 'modesty': 1}]

root_list = [] # updated list with root synonyms

for dict in ee:
    root_dict = {} # creates a new root dictionary for each dictionary read
    #print(root_dict)
    seen = set() #keeps track of which keys have been seen
    #syn_seen = {}
    for key, value in dict.items():
        #print(key, value)
        root_syn = find_root_synonym(key)
        # check if seen
        if root_syn in seen:
            #add value to value for relevant key in root dictionary
            #continue without adding root to dict
            old_val = root_dict[root_syn]
            root_dict[root_syn] = old_val + value
            #print("seen")
        else:
            root_dict[root_syn] = value
            seen.add(root_syn)
            #print("unseen")
        #root_list.append(root_dict)   #square bracket notation or keep as is?
        #print(root_list)
    root_list.append(root_dict)
print(root_list)








#for i in range(len(ee)):
    #x = (ee[i].keys())

#for dict in ee:
    #for i in range(len(ee)):
       #x = (ee[i].keys())
        #root_synonym = find_root_synonym(x)
        #root_list.append(root_synonym)
        #print(root_synonym)


    #for j in range(len(x)):


#print(root_dict)



#test_list = ["from", "grandfather", "verus", "i", "learned", "morals", "government", "temper", "entity"]

#root_list = []


# SYNONYM TESTER
#for query in ee:
#for query in test_list:
    #root_synonym = find_root_synonym(query)
    #root_list.append(root_synonym)
    #print(root_synonym)

#print(root_list)








#word = "entity"
#root_synonym = find_root_synonym(word)
#print("The root synonym of the word '{}' is: {}".format(word, root_synonym))
