 # Pair Programmers:  Hyo Lee and Jennifer Dunham
# CST 205
# Lab 14 - Files in Python
# 12/08/2014

# Problem 1:

def countTotalWords():    
  #count words in eggs.txt
  
  eggs = r"C:\Users\white_000\Documents\School\CSUMB\CST 205\Python Working Folders\14_Lab14\eggs.txt"
  textFile = open(eggs, "rt")
  
  wordCount = 0
  
  for line in textFile:
    words = line.split()
    wordCount += len(words)
  print "Word Count: " + str(wordCount)
  textFile.close()
  
def countSameWords():
  #counts the number of times words occur in eggs.txt
  textFile = r"C:\Users\white_000\Documents\School\CSUMB\CST 205\Python Working Folders\14_Lab14\eggs.txt"
  openFile = open(textFile, "rt")
  text = openFile.read()
  wordsLower = text.lower()
  words = wordsLower.split()
  d = dict()
  for word in words:
    if word in d:
      d[word] += 1
    else:
      d[word] = 1
  print d
  openFile.close()

def totalAndWordCount():
  #prints the total words and count of each word in eggs.txt
  countTotalWords()
  print "Count for each of the words:"
  countSameWords()
  
