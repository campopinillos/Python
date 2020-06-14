#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:46:34 2020

@author: campopinillos
"""
from stop_words import get_stop_words
from collections import namedtuple
import pandas as pd
import numpy as np

stopwords = get_stop_words('en')

def find_frequent_words(sentence):
    bagOfWords = sentence.split(' ')
    
    #uniqueWords = set(stopwords).union(set(bagOfWords))
    numOfWords = dict.fromkeys(bagOfWords, 0)
    for word in bagOfWords:
        numOfWords[word] += 1
        
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in numOfWords.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict