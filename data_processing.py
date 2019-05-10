from typing import Any, Union
import requests
import nltk
import jieba
import jieba.analyse
import time
from bs4 import BeautifulSoup
import re
import pickle
from selenium import webdriver
from requests import cookies
from nltk.corpus import sinica_treebank
import numpy as np



def load_stopwords(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding = 'utf-8').readlines()]
    c = stopwords.pop(0)
    #print(stopwords)
    return stopwords

def load_data(i):
    with open('page'+str(i)+'.plk', 'rb') as f:
        return pickle.load(f)

def anonymous():
    for i in range(2,17):
        ld = load_data(i)
        print()
        stop_words = load_stopwords('stopwords.txt')
        wl = cut_contents(ld, stop_words)
        get_word_freq(wl)

def cut_contents(filtered_contents, stop_words):
    words_list = []
    for c in filtered_contents:
        words_list += jieba.lcut(c[1])

    print(len(words_list))
    for w in words_list:
        if w in stop_words:
            words_list.remove(w)

    return words_list

def get_word_freq(words_list):
    freq_dist_posts = []
    freq_dist_posts = nltk.FreqDist(words_list)
    print(type(freq_dist_posts))
    f = open("word_freq.txt",'w', encoding="utf-8")
    for key in freq_dist_posts:
        ks = str(key)
        vs = str(freq_dist_posts[key])
        kvs = ks+' '+ vs+'\n'
        f.write(kvs)
    #with open("word_freq.txt",'w+') as f:
    #    f.writelines(freq_dist_str)
    f.close()
    return




anonymous()