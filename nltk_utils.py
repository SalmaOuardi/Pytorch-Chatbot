# Created by Salma OUARDI

import numpy as np
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()


def tokenize(sentence):
    
    return nltk.word_tokenize(sentence, language="french")


def stem(word):
    stemmer = SnowballStemmer("french")
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
  
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag


