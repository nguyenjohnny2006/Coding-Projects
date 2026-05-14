# File: TextTranslator.py
# Student: Johnny Nguyen
# UT EID: jn28999
# Course Name: CS303E
# 
# Date: 4/3/2026
# Description of Program: Application that explains slang in a dictionary and can translate text.
import os.path

def printMenu():
    print()
    print("The following actions are available:")
    print("  1 - Explain a term.")
    print("  2 - Translate a message.")
    print("  3 - Extend/Change the dictionary.")
    print("  4 - Show this menu.")
    print("  5 - Exit the application")

def defineTerm(myDict):
    term = input("  Please enter a term to explain: ")
    x = term.lower()
    print()
    if x not in myDict:
        print("Term not defined:",term)
        return
    print(term, ": ", myDict[x],sep="")
    return

def translate(myDict):
    text = input("  Please enter a message to translate: ")
    words = spacePunc(text).split()
    result = ""
    for word in words:
        if word.lower() in myDict:
            x = myDict[word.lower()]
            result += str(x) + " "
            continue
        result += word + " "
    return result

def spacePunc(text):
    a = ""
    for b in text:
        if b in ".,!?:;)(":
            a += " "
        a +=b
    return a

def changeDict(myDict):
    key = input("  Add the following term: ")
    value = input("  With definition: ")
    myDict[key.lower().strip()] = value.strip()
    
def main():
    print("\nWelcome to the Text Translator application.\n")
    file = str(input("Specify file containing terms and definitions: "))
    if not os.path.isfile(file):
        print("File does not exist:",file)
        return
    myDict = {}
    infile = open(file,"r")
    for line in infile:
        key,value = line.split(":")
        myDict[key.strip().lower()] = value.strip()
    print("Building dictionary from:", file)
    
    printMenu()
    actionTrue = True
    while actionTrue:
        print()
        action = input("Choose an action (1-5): ")
        if action == "1":
            defineTerm(myDict)
        elif action == "2":
            print("Message translation:",translate(myDict))
        elif action == "3":
            changeDict(myDict)
        elif action == "4":
            printMenu()
        elif action == "5":
            print()
            print("Thanks for using this app. Goodbye!")
            infile.close()
            return
        else:
            print("Action not recognized; please enter 1-5.")
    
main()
