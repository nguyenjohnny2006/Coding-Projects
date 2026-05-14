""" This file includes a class Hand which implements a hand of five playing
    cards, where cards are defined in the Card class.   

    The Hand class defines the following methods:

    Hand( source, fromDeck ):  creates a new hand object of 5 Cards. This happens
         in one of two ways depending on the value of fromDeck: 
         (1) if fromDeck is True, deal 5 cards from an existing deck
             passed as source, 
         (2) if fromDeck is not True, create the cards from a list of 5 card 
             specifiers passed as source, e.g., ("2S", "9S", "TC", "AH", "4D") 
             will create a hand containing the 2 of Spades, 9 of Spades, 10 of Clubs, 
             Ace of Hearts, and 4 of Diamonds.  Generating a single card from a 
             spec is implemented in the Card class.  You need to check that this
             list is legal (contains exactly 5 legal card specifiers, all distinct).
    h.__str__(): generate the print representation of Hand h, using the
         str function on each of the individual Cards it contains (see the Deck
         class for a model for this);
    h.getCard( i ): recall that h is a hand of 5 Cards.  This provides a 
         way of getting the ith card from the hand, for example, to iterate 
         through the hand in a loop. 

    This file also contains a number of other functions (outside the class), mainly
    to allow evaluating a hand in the sense of playing Poker.  You can have as many
    functions as you need, but you must have the function evaluateHand( hand ). 
    Given a hand, it prints the hand and then the "evaluation" of the hand in 
    the sense of a Poker hand.  This is described in detail in the assignment description.   

"""

################################################################################
#                                                                              #
#                                 Hand Class                                   #
#                                                                              #
################################################################################

# I don't need to import Card, since Deck already does.
from Deck import *

def isLegalCardList( l ):
    """ Check that list l contains 5 legal card specifiers, 
        all distinct. You can assume that it's a list. """
    # You'll need to fill this in
    legal = True
    if len(l) != 5:
        return False
    for a in l:
        if isLegalCardSpecifier(a):
            continue
        else:
            return False
    return legal
        
    pass  

class Hand:

    def __init__(self, source, fromDeck = True):
        """ A hand is simply a list of 5 cards, dealt from the deck
            or given as a list of five card specifiers.  If fromDeck
            is True, expect to deal from a deck passed as source. 
            If False, expect source to be a list of five Card specifiers.
            Create the hand from the specified cards.
        """
        if fromDeck:
            if ( len(source) < 5 ):
                print ( "Not enough cards left!" )
                return None
            self.__cards = []
            for i in range(5):
                card = source.deal()              # deal next card
                self.__cards.append(card)         # append it to the hand
        elif not isLegalCardList( source ):
            print("Illegal card list provided.")
        else:
            # fill in this code, to generate a hand from
            # a list of Card specifiers.  You can assume that
            # source is a list,
            self.__cards = []
            for i in source:
                self.__cards.append(i)
            pass

    def __str__(self):
        """ Generates the print image of the Hand. """
        fullList = ""
        for i in self.__cards:
            fullList += str(i) + "\n"
        return fullList.strip()
        pass

    def getCard( self, i ):
        """ Get the ith card from the hand, where 
            i in [0..4]. Return None if i is not
            legal. """
        if not 0 <= i <= 4:
            return None
        else:
            return self.__cards[i]
        
        pass
            
################################################################################
#                                                                              #
#                                Evaluate Hand                                 #
#                                                                              #
################################################################################

def processHand( hand ):
    """ Given a poker hand, create and return two lists which
        record the ranks and suits in the hand. """
    myRanks = [0] * 13 
    mySuits = [0] * 4
    for i in range(5):
        card = hand.getCard(i)
        a = CARDRANKS.index(card.getRank().upper())
        myRanks[a] += 1
        b = CARDSUITS.index(card.getSuit().upper())
        mySuits[b] += 1
    return myRanks, mySuits
        
    
    pass

# You'll need to define all of the auxiliary functions called by
# evaluateHand.  Notice that these auxiliary functions don't all
# need both myRanks and mySuits, but I decided to pass them both
# just to make the interface more uniform.  You can change that 
# if you want to.

def hasPair( myRanks, mySuits ):
    pass
    pair = 0
    for i in myRanks:
        if i == 2:
            pair += 1
    if pair == 1:
        return True
    return False
    

def hasTwoPair(myRanks,mySuits):
    pair = 0
    for i in myRanks:
        if i == 2:
            pair += 1
    if pair == 2:
        return True
    return False

def hasThreeOfAKind(myRanks,mySuits):
    if 3 in myRanks:
        return True
    return False

def hasStraight(myRanks,mySuits):
    count = 0
    for i in myRanks:
        if i == 0:
            count = 0
        if i >= 1:
            count += 1
        if count == 5:
            return True
    if myRanks == [1,1,1,1,0,0,0,0,0,0,0,0,1]:
        return True
    return False

def hasFlush(myRanks,mySuits):
    if 5 in mySuits:
        return True
    return False
            
def hasFullHouse(myRanks,mySuits):
    if hasPair(myRanks,mySuits) and hasThreeOfAKind(myRanks,mySuits):
        return True
    return False

def hasFourOfAKind(myRanks,mySuits):
    if 4 in myRanks:
        return True
    return False

def hasStraightFlush(myRanks,mySuits):
    if hasFlush(myRanks,mySuits) and hasStraight(myRanks,mySuits):
        return True
    return False

def hasRoyalFlush(myRanks,mySuits):
    if myRanks == [0,0,0,0,0,0,0,0,1,1,1,1,1] and hasFlush(myRanks,mySuits):
        return True
    return False

    
# Add other recognizers here; evaluateHand tells you which ones you
# need.  I suggest doing them in "reverse order" so you define the 
# lowest hands first. Hopefully, you'll see why as you code them!

def evaluateHand( hand ):
    myRanks, mySuits = processHand( hand )
    print( hand )
    print()
    if hasRoyalFlush( myRanks, mySuits ):
        print( "Royal Flush" )
    elif hasStraightFlush( myRanks, mySuits ):
        print( "Straight Flush" )
    elif hasFourOfAKind( myRanks, mySuits ):
        print( "Four of a kind" )
    elif hasFullHouse( myRanks, mySuits ):
        print( "Full House" )
    elif hasFlush( myRanks, mySuits ):
        print( "Flush" )
    elif hasStraight( myRanks, mySuits ):
        print( "Straight" )
    elif hasThreeOfAKind( myRanks, mySuits ):
        print( "Three of a kind" )
    elif hasTwoPair( myRanks, mySuits ):
        print( "Two pair" )
    elif hasPair( myRanks, mySuits ):
        print( "Pair" )
    else:
        print( "Nothing" )

# This is some test code.  You can modify this or write your
# own.  You certainly should test additional hands. You can run 
# this in interactive mode with:
# 
# from Hand import *
# TestCode()
#
# You can also run this in batch mode by uncommenting the call to:
# TestCode()
#
# and running:
# 
# python3 Hand.py              # or whatever the python command is
#                              # is on your system. 

def TestCode():
    print("\nGenerating and printing deck")
    d = Deck()
    print(d)
    print("\nShuffling deck and printing deck")
    d.shuffle()
    print(d)

    print("\nGenerating hand from deck")
    h = Hand(d, True)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["as", "ad", "ah", "ac", "2d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["AS", "2S", "3C", "4H", "5D"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["2s", "9S", "tc", "AH", "4d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

# TestCode()
