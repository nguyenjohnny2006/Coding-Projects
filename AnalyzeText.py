# Assignment: HW11
# File: AnalyzeText.py
# Student: Johnny Nguyen
# UT EID: jn28999
# Course Name: CS303E
# 
# Date: 4-20-2026
# Description of Program: Takes a text and gives back certain statistics such as word count and most commonly occuring words.

wordsToExclude = ['a', 'about', 'after', 'all', 'also', 'am', 'an', 'and',
                  'any', 'are', 'as', 'at', 'back', 'be', 'because',
                  'but', 'by', 'can', 'come', 'could', 'day', 'do',
                  'even', 'first', 'for', 'from', 'get', 'give', 'go',
                  'good', 'had', 'have', 'he', 'her', 'him', 'his',
                  'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its',
                  'just', 'know', 'like', 'look', 'make', 'man', 'me',
                  'men', 'most', 'my', 'new', 'no', 'not', 'now',
                  'of', 'on', 'one', 'only', 'or', 'other', 'our',
                  'out', 'over', 'people', 'said', 'say', 'see',
                  'she', 'so', 'some', 'take', 'than', 'that', 'the',
                  'their', 'them', 'then', 'there', 'these', 'they',
                  'think', 'this', 'time', 'to', 'two', 'up', 'us',
                  'use', 'want', 'was', 'way', 'we', 'well', 'went',
                  'were', 'what', 'when', 'which', 'who', 'will',
                  'with', 'work', 'would', 'year', 'you', 'your']

def cleanLine( s ):
    """Given a string s, remove designated punctuation and convert others:
    non-ascii single quotes to ascii equivalents; underscore and dash
    to space."""

    # Create a translation table that maps any character in string
    # toRemove to a None.  Also translates the non-ascii single quote
    # to an ascii single quote and underscore/dash to blank.

    toTranslate = "\u2018\u2019\u2010\u2014\u2012-"
    translateTo = "''    "
    toRemove = ".,;:?$()[]\u201C\u201D\u00A3!\"'"
    translationTable = str.maketrans(toTranslate, translateTo, toRemove)
    
    # Use the translate() method to apply the mapping to string s
    translatedText = s.translate(translationTable)

    # print("Translated Text:", translatedText)
    return translatedText

def createDictionary( filename ):
    """Create a dictionary associating each word in a text file with the
    number of times the word occurs.  Also count the total number of
    words and the number of unique words in the text.  Certain very
    common words are not included in the dictionary, but are counted.
    Return a triple: (wordCount, uniqueWordCount, dictionary)."""
    myDict = {}
    totalwords = 0
    uniqueWords = set()
    
    for line in filename:
        line = cleanLine(line)
        words = line.split()
        for word in words:
            totalwords += 1
            word = word.lower()
            uniqueWords.add(word)
            if word in wordsToExclude:
                continue
            if word in myDict:
                myDict[word] += 1
            else:
                myDict[word] = 1
    filename.close()
    uniqueWordCount = len(uniqueWords)
    
    return totalwords, uniqueWordCount, myDict
            
def sortByFrequency( myDict ):
    """Return a list of pairs of (count, word)
    sorted by count in descending order. I.e., 
    the most frequent word should be first in the
    list."""
    pairs = []
    for item in myDict:
        pair = (myDict[item],item)
        pairs.append(pair)
    pairs.sort()
    return pairs
    
    pass

# Think about how to use the function sortByFrequency
# for this one.
def mostFrequentWords( myDict, k ):
    """Return a list of the k most frequently occurring 
    words."""
    a = sortByFrequency(myDict)
    a.reverse()
    b = a[0:k]
    c = []
    for item in b:
        c.append(item[1])
    print("[ ",end="")
    for item in c[0:len(c)-1]:
        print(item + ", ", end = "")
    print(c[-1], end = " ")
    print("]")
        
    pass

def sortByWordLength( myDict ):
    """Return a list of pairs of (length, word)
    sorted by length in descending order. I.e.,
    the longest word should be first in the list."""
    pairs = []
    for item in myDict:
        pair = (len(item), item)
        pairs.append(pair)
    pairs.sort()
    return pairs
    pass

# Think about how to use the function sortByWordLength
# for this one.
def longestWords(myDict,k ):
    """Return a list of the k longest words in the
    text."""
    a = sortByWordLength(myDict)
    a.reverse()
    b = a[0:k]
    c = []
    for item in b:
        c.append(item[1])
    print("[ ",end="")
    for item in c[:5]:
        print(item + ", ", end = "")
    print()
    print("     ", end = "")
    for item in c[5:]:
        print(item + ", ", end = "")
    print(c[-1], end = " ")
    print("]")
    pass

# Think about how to use the function sortByWordLength
# for this one.
def shortestWords(myDict, k ):
    """Return a list of the k shortest words in the
    text."""
    a = sortByWordLength(myDict)
    b = a[0:k]
    c = []
    for item in b:
        c.append(item[1])
    print("[ ",end="")
    for item in c[0:len(c)-1]:
        print(item + ", ", end = "")
    print(c[-1], end = " ")
    print("]")
    
    pass

def main():
    filename = str(input("Enter a filename: "))
    infile = open(filename,"r")
    totalwords, uniqueWordCount, myDict = createDictionary(infile)
    print()
    print("Text analysis of file:", filename)
    print("  Total word count: ", totalwords)
    print("  Unique word count:", uniqueWordCount)
    print("  10 most frequent words: ")
    print("   ", end = "")
    mostFrequentWords(myDict,10)
    print("  10 longest words: ")
    print("   ", end = "")
    longestWords(myDict,10)
    print("  10 shortest words: ")
    print("   ", end = "")
    shortestWords(myDict,10)
    
main()
