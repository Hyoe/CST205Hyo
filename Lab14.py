# Hyo Lee
# CST 205
# Lab 14 - Files in Python
# 12/08/2014

# Problem 1:

#
def totalWords():
  #Open eggs.txt
  file = "C:\Users\Me\Documents\CST205\CST205\Functions\Lab14\eggs.txt"
  openFile = open(file, "rt")

  wordCount = 0   
  
  for lines in openFile:
    wordsNoSpaces = lines.split()  #Stores words in lists where default delimiter is blank space with built-in string method split(), resource: https://docs.python.org/2/library/stdtypes.html
    wordCount = wordCount + len(wordsNoSpaces)
  print "Total word count = ", str(wordCount)
  openFile.close()
   

def sameWords():
  file = "C:\Users\Me\Documents\CST205\CST205\Functions\Lab14\eggs.txt"
  openFile = open(file, "rt")
  
  text = openFile.read()
  wordsUpper = text.upper()
  noDashes = wordsUpper.replace("-", " ")
  words = noDashes.split()
  
  counts = {}
  
  for word in words:
    if word in counts:
      counts[word] = counts[word] + 1
    else:
      counts[word] = 1
  print counts
  print "Total unique words = ", str(len(counts))

  
  