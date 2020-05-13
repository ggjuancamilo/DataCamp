# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:54:50 2020

@author: juanc
"""
import re
from collections import Counter

def tokenize(text):
    """Split text into tokens using a regular expression

    This is a wrapper for re.findall with case ignored.

    :param text: text to be tokenized
    :return: a list of resulting tokens

    >>> tokenize("word word 1.22 can't. cannot")
    ['word', 'word', 'can', 't', 'cannot']
    """
    return re.findall(r'@?#?[a-zA-z]+', text, flags=re.IGNORECASE)

def filter_word_counts(word_counts, first_char):
    """Filter Document.word_counts by the first character of the word
    
    :param word_counts: the word_counts attribute of a Document class instance
    :param first_char: only keep word counts that start with this character
    
    >>> # How to filter to only words that start with 'A'
    >>> filter_word_counts(document.word_counts, 'A')
    """
    return Counter({k: v for k, v in word_counts.items() if k[0] == first_char})