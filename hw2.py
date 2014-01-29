# -*- coding: utf-8 -*-
"""
LING571 HW2

# This is the main function used to print all sentences' parses
# hw2.py

Created on Thu Jan 23 17:25:09 2014

@author: haotianhe
"""

import nltk
import sys
from parser import CKYParser

if __name__ == "__main__":

    if (len(sys.argv) == 2):
        sent = sys.argv[0]
        cnf = sys.argv[1]
    else:
        sent = "sentences.txt"
        cnf = "grammar.cnf"

    grammar = nltk.data.load("file:grammar.cnf")
    sentences = open(sent, 'r')
    parser = CKYParser(grammar)
    
    # initialize the counting
    sentCount = 0;
    parsCount = 0;
    totalParsCount = 0;
    
    for sentence in sentences: # reads each sentence
    
        tokens = nltk.tokenize.wordpunct_tokenize(sentence) # makes each sentence splitted
        sentCount += 1 # counts the number of sentences in this example
        
        parses = parser.nbest_parse(tokens) # parses the given sentence to get parse trees that represent possible structures for the given sentence
        for parse in parses: # prints the parse trees
            print str(parse) + "\n"
            parsCount += 1 # counts the number of parses for the sentence
            
        if parsCount == 1: # prints the number of parses under the tree
            print str(parsCount) + " parse" + "\n"
        else:
            print str(parsCount) + " parses" + "\n"
        print "\n"

        totalParsCount += parsCount
        parsCount = 0;

    print "The average number of parses per sentence obtained by the grammar is " + str(int(round(totalParsCount/sentCount))) # prints the statement of the performance