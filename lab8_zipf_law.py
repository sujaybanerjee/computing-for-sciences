"""
This program takes the name of the file as a command line argument, counts the frequencies of the words in this file, generates a graph using Matplotlib, and prints out the 10 most frequent words.

CS150 Lab 8
Name: Sujay Banerjee
Section: A
Creativity: Incorporated filename into title of the graph and used datascience table to compute counts and rankings in def chart(filename).
"""

import sys
import numpy as np
import datascience as ds
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

TOPRANKING = 10

def read_corpus(filename):
    """
    This function will return list of cleaned and normalized words (lower case, excluding punctuation)

    Args:
        filename: name of the file as a string

    Returns:
        returns a list of cleaned a normalized words
    """
    with open(filename, errors='ignore') as word_file:
        words = []
        for line in word_file:
            clean = line.split()
            for line in clean:
                words.append(line.strip(".!?:,;'\"").lower())
        return words

def print_lines(filename):
    num_lines = 0
    num_chars = 0
    with open(filename, errors='ignore') as text_file:
        for line in text_file:
            num_lines += 1
            print(str(num_lines)+ "\t" + line.strip())
            for char in line:
                num_chars += 1
        print("Number of lines: " + str(num_lines))
        print("Number of characters: " + str(num_chars))
            



def get_2nd(item):
    """
    This function will return the second item to be used as a key in def count_and_rank(words)

    Args:
        iterable item

    Returns:
        returns second item
    """
    return item[1]


def count_and_rank(words):
    """
    This function returns a tuple containing a list of words and a list of counts for those words and both lists should
    be sorted in decreasing order of count (the most common word and its count should the first element of the lists.)


    Args:
        words: list of words

    Returns:
        returns a tuple of list of words and a list of counts
    """
    counter = {}
    keys = []
    values = []
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    counter = sorted(counter.items(), key = get_2nd, reverse = True)
    for i in counter:
        keys.append(i[0])
        values.append(i[1])
    return (keys, values)


def chart(filename):
    """
    This function will print the top 10 ranked words and corresponding count using a datascience table

    Args:
        filename: name of the file as a string

    Returns:
        none
    """
    text = read_corpus(filename)
    chart = ds.Table().with_columns("Word", text, formatter = None)
    chart = chart.group("Word")
    chart = chart.relabeled("count", "Count")
    chart = chart.sort(1, descending = True)
    chart = chart.take[:TOPRANKING]
    print(chart.as_text(sep="\t"))





def find_rank(filename):
    """
    This function will print the top 10 ranked words and corresponding count

    Args:
        filename: name of the file as a string

    Returns:
        none
    """
    top_words = []
    top_rank = []
    text = read_corpus(filename)
    full_ranking = count_and_rank(text)
    print("Word\tCount")
    if len(full_ranking[0]) >= TOPRANKING:
        for i in range(TOPRANKING):
            top_words.append(full_ranking[0][i])
            top_rank.append(full_ranking[1][i])
            print(str(top_words[i]) + "\t" + str(top_rank[i]))
    else:
        for i in range(len(full_ranking[0])):
            top_words.append(full_ranking[0][i])
            top_rank.append(full_ranking[1][i])
            print(str(top_words[i]) + "\t" + str(top_rank[i]))



def gen_plot(filename):
    """
    This function will generate the plot from the words and rankings and calls find_rank

    Args:
        filename: name of file as a string

    Returns:
        none
    """
    text = read_corpus(filename)
    full_ranking = count_and_rank(text)
    chart(filename)
    x = range(1, len(full_ranking[0])+1)
    y = full_ranking[1]
    plt.scatter(x, y, color='purple')
    plt.xlabel('Rank')
    plt.ylabel('Count')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Log-Log Plot of Count vs. Rank of Words in ' + filename)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python3 lab8_zipf_law.py <filename>")
    else:
        print_lines("Story.txt")
        gen_plot(sys.argv[1])
