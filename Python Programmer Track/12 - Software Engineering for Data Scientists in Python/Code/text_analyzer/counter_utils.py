# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:33:29 2020

@author: juanc
"""

# Import needed functionality
import matplotlib.pyplot as plt
from collections import Counter

def plot_counter(counter, n_most_common=5):
    # Subset the n_most_common items from the input counter
    top_items = counter.most_common(n_most_common)
    # Plot `top_items`
    plot_counter_most_common(top_items)
    
    
def plot_counter_most_common(top_items):
    top_items_dict = dict(top_items)
    plt.figure()
    plt.bar(range(len(top_items_dict)), list(top_items_dict.values()), align='center')
    plt.xticks(range(len(top_items_dict)), list(top_items_dict.keys()), rotation='vertical')
    plt.tight_layout()
    plt.show()
    
    
def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())