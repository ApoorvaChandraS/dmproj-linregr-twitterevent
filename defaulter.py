import os
import nltk
import time
import math
import pylab



def readTweet(filename):
 f= open(filename,"r")
 fields = []
 for line in f:
   fields=line.split(",")
   print fields[2][:14]




readTweet("tester2.csv") 
