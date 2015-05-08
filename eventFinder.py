#program to find the core and subordinate words in an event 
import os
import nltk
import math
import time
import pylab
import networkx
import re
from nltk.corpus import stopwords as sw


swords = sw.words('english') # to remove the stopwords from the tweets
word_list = [] #list of words in the whole dataset
word_scores = {} #overall score of all words in the dataset




def getCoreWords(filename,timestamp):
 global word_list
 global word_scores 
 fl = open(filename,"r")
 tweet = ''
 fields = []
 time_word_list = []  
 core_words = {}
 for line in fl :
  fields = line.split(",")
  tweet = fields[-3]
  tweet = nltk.pos_tag(nltk.word_tokenize(tweet))
  if fields[2][:14] == timestamp:
    for items in tweet :
       if items[0] not in swords and not(re.search("t.co",items[0])):
          time_word_list = time_word_list + [items[0].lower()] 
 freq_time_words_list = nltk.FreqDist(time_word_list)
 for word in freq_time_words_list.keys():
   core_words[word] = freq_time_words_list[word]/(word_scores[word]+0.0)

 print 'For the timestamp :' , timestamp
 #print '\n\n\n\n\n\n\n'
 for key in core_words.keys() :
   if core_words[key] > 0.4 :
        print key, core_words[key]

 print '\n\n\n\n\n\n'   


 


def formWords(filename) :
 global word_list
 global word_scores 
 timestamps = []
 fields = [] 
 counter = 0
 fl = open(filename,"r")
 tweet = ''
 
 for line in  fl :
  fields = line.split(",")  
  tweet = fields[-3]
  counter = counter + 1
  print counter
  tweet = nltk.pos_tag(nltk.word_tokenize(tweet)) # add the cmu parser here
  if fields[2][:14] not in timestamps:
     timestamps = timestamps + [fields[2][:14]] 
  for items in tweet:
    if  (items[0] not in word_list and items[0] not in swords) and not(re.search("t.co",items[0])):
      word_list = word_list + [items[0].lower()]
      word_scores[items[0].lower()] = 1
    if items[0] in word_list :
      word_scores[items[0].lower()] = word_scores[items[0].lower()]+1
    
  
  
 print len(word_list)
 fdist = nltk.FreqDist(timestamps)
 l=len(fdist.keys())
 for score in word_scores.values():
  score = score/l  
 for timestamp in sorted(fdist.keys()):
   getCoreWords(filename,timestamp)



formWords("tester2.csv")
