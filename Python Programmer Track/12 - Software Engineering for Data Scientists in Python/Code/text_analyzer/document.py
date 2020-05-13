# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:25:42 2020

@author: juanc
"""
from collections import Counter
from .tokenutils import tokenize, filter_word_counts
from .counter_utils import plot_counter
from .text_utils import filter_lines


# Define Document class
class Document:
  def __init__(self, text):
    self.text = text
    # Tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # Perform word count with non-public count_words method
    self.word_counts = self._count_words()


  def _tokenize(self):
    return tokenize(self.text)
	
  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)

  def plot_counts(self, attribute='word_counts', n_most_common=5):
    """ Plot most common elements of a ``collections.Counter`` instance attribute

    :param attribute: name of ``Counter`` attribute to use as object to plot
    :param n_most_common: number of elements to plot (using ``Counter.most_common()``)
    :return: None; a plot is shown using matplotlib

    >>> doc = Document("duck duck goose is fun when you're the goose")
    >>> doc.plot_counts('word_counts', n_most_common=5)  # same as default call
    """
    plot_counter(getattr(self, attribute), n_most_common)


# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    """Analyze text data from social media
    
    :param text: social media text to analyze

    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
    
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char = '#')
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char = '@')
    
    
# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)
