def compareStr():
    myFruit = 'apple'
    if myFruit.upper() > myFruit:
        print 'True'
    else:
        print 'False'

def test():        
  x = 0
  while (x < 4):
    print "Looping x = " + str(x)
    x = x + 1

def test1():
  fruit = 'banana'
  index = len(fruit)-1
  while index >= 0:
    letter = fruit[index]
    print letter
    index = index - 1
    
    
def test2():
  fruit = 'banana'
  index = 0
  while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def word():
  word = 'banana'
  count = 0
  for letter in word:
    if letter == 'a':
        count = count + 1
  print count

def counting():
  count = 1
  while count < 10:
    print "Hello, I am a while and count is", count
    count = count + 2

def count():
  myString = "hello"
  index= 0
  while index< len(myString):
    print myString[index]























