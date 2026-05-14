# Assignment: Project2
# File: Poker.py
# Student: Johnny Nguyen
# UT EID: jn28999
# Course Name: CS303E
# 
# Date: 4-6-2026
# Description of Program:

from Hand import *

def main():
    while True:
        iterations = int(input("How many hands should I deal? "))
        if iterations <= 0:
            print(" Positive number required. Try again!")
            continue
        break
    d = Deck()
    d.shuffle()
    for i in range(1,iterations+1):
        print()
        print("Hand drawn (",i,"):",sep="")
        h = Hand(d,True)
        print()
        evaluateHand(h)
        if len(d) < 5:
            print()
            print("Dealing a new deck.")
            d = Deck()
            d.shuffle()
            
        

main()
        
    
