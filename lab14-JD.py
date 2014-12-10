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
  print "Unique Words: " + str(len(d))
  openFile.close()

def totalAndWordCount():
  #prints the total words and count of each word in eggs.txt
  countTotalWords()
  print "Count for each of the words:"
  countSameWords()
  
def mostCommonWord():
  #prints the most common word in eggs.txt
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
  list = []
  list = d.values()
  list.sort()
  mostCommonWordValue = list[len(list)-1]
  for key in d:
    if d[key] == mostCommonWordValue:
        print "Most commonly occurring word:  " + str(key)
  openFile.close()

# Problem 2:

def extractHeadlines():
  #prints all the headlines from otterrealm.com
  #source: http://otterrealm.com/author/theotterrealm/
  htmlFile = r"C:\Users\white_000\Documents\School\CSUMB\CST 205\Python Working Folders\14_Lab14\theotterrealm.html"
  openFile = open(htmlFile, "rt")
  textFile = openFile.read()
  for line in textFile:
    word = line.strip(textFile, "h3")
    print word
  #string.find(text, sub, "<h3", "</h3>")
  #print sub
  #text.split('h3', 1)
  
  #print textFile.split('h3')
  
  
def find_between():
  #prints all the headlines from otterrealm.com
  #source: http://otterrealm.com/author/theotterrealm/
  htmlFile = r"C:\Users\white_000\Documents\School\CSUMB\CST 205\Python Working Folders\14_Lab14\theotterrealm.html"
  openFile = open(htmlFile, "rt")
  textFile = openFile.read()
  try:
      start = textFile.index( "<h3" ) + len( "<h3" )
      end = textFile.index( "</h3>", "<h3" )
      return textFile["<h3":"</h3>"]
  except ValueError:
      return ""
  print find_between( textFile, "<h3", "</h3>" )
  openFile.close()

def findBetween():
  import re

  s = '<h3asdf=5;iwantthis123jasd</h3>'
  result = re.search('<h3(*)</h3>', s)
  print result.group(1)

    
        
def headlines():
  file = r"C:\Users\white_000\Documents\School\CSUMB\CST 205\Python Working Folders\14_Lab14\theotterrealm.html"
  openFile = open(file, "rt")
  text = openFile.read()
  #noInequality = text.replace("<", "/")
  #print noInequality

# find index of substring h3 can't get it to work with <h3>
  print "start:"
  startLocation = -1
  startIndices = []
  while true:
    startLocation = text.find("<h3 class=\"archive_title\" id=\"post-", startLocation + 1)
    if startLocation == -1:
      break
    startIndices.append(startLocation)
    print startLocation
  print startIndices
  print len(startIndices)
        
  print "\nend:"

  endLocation = -1
  endIndices = []
  #for i in range (0,len(startIndices)):
  while true:
    endLocation = text.find("/h3", endLocation + 1)
    if endLocation == -1:
    #if endLocation <= startIndices[0] or endLocation >= (startIndices[len(startIndices)] + 200):
      break
    print endLocation
    if endLocation >= startIndices[0]:
      endIndices.append(endLocation)
    
    
  print endIndices

