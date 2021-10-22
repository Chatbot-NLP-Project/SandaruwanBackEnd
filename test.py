
import nltk
from nltk.stem.lancaster import LancasterStemmer

import numpy
import tflearn
from tensorflow.python.framework import ops
import random
import json
import pickle
import numpy as np
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


stemmer = LancasterStemmer()
n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
print(n_estimators)

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        # print(wrds)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

# words1 = [stemmer.stem(w.lower()) for w in words if w not in "?"]
# print(words1)
# words2 = [lemmatizer.lemmatize(w.lower()) for w in words if w not in "?"]
# print(words2)
# words = sorted(list(set(words)))
# labels = sorted(labels)
# training = []
# output = []
#
# out_empty = [0 for _ in range(len(labels))]
# # print(out_empty)
# print(docs_y)
# for x, doc in enumerate(docs_x):
#     bag = []
#     wrds = [stemmer.stem(w) for w in doc]
#
#     for w in words:
#         if w in wrds:
#             bag.append(1)
#         else:
#             bag.append(0)
#     # print(bag)
#     output_row = out_empty[:]
#     output_row[labels.index(docs_y[x])] = 1
#
#     training.append(bag)
#     output.append(output_row)
