# File: RecursiveFunctions.py
# Student: Johnny Nguyen
# UT EID: jn28999
# Course Name: CS303E
# 
# Date: 4-14-2026
# Description of Program: List of recursive functions to use that return a value.

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in list L. """
    if not L:                 # same as L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   """ Return the sum of the non-negative integers to n.
   E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5 """
   if n == 0:
       return 0
   else:
       return n + addToN(n-1)

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. 
   E.g., findSumOfDigits( 1234 ) = 10 """
   if 0 <= n <= 9:
       return n
   else:
       return (n % 10) + findSumOfDigits(n // 10)
    
   
def integerToBinary( n ):
   """ Given a nonnegative integer n, return the 
   binary representation as a string. E.g., 
   integerToBinary( 10 ) = '1010' """
   if n == 0:
       return "0"
   if n//2 == 0:
       return "1"
   else:
       return  integerToBinary(n//2) + format(n%2,"0.0f")
         

def integerToList( n ):
   """ Given a nonnegative integer, return a list of the 
   digits (as strings). 
   E.g., integerToList( 123 ) = ['1', '2', '3'] """
   if 0 <= n <= 9:
       return [str(n)]
   else:
       return integerToList(n//10) + [str(n%10)]


def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome.
   Case counts: 'abA' is not a palindrome. """
   if len(s) <= 1:
       return True
   if s[0] != s[-1]:
       return False
   else:
       return isPalindrome(s[1:len(s)-1])

def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if len(s) == 0:
      return None
   if 65 <= ord(s[0]) <= 90:
      return s[0]
   else:
      return findFirstUppercase(s[1:])


# for this one, don't reverse the string.
def findLastUppercase( s ):
   """ Return the last uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if len(s) == 0:
      return None
   if 65 <= ord(s[len(s)-1]) <= 90:
      return s[len(s)-1]
   else:
      return findLastUppercase(s[0:len(s)-1])
                

def negateItems( lst ):
   """Assume lst is a list of numbers.  Return a list
   of the negations of those numbers."""
   if len(lst) == 0:
      return []
   else:
       return [-lst[0]] + negateItems(lst[1:])


def findLargest( lst ):
   """Assume lst is a list of numbers. Recursively find
   and return the largest element."""
   if lst == []:
       return None
   if len(lst) == 1:
      return lst[-1]
   if lst[0] >= lst[1]:
      return findLargest([lst[0]]+lst[2:])
   else:
      return findLargest(lst[1:])


# This one is designed to see if you can think recursively on more
# "real world" problems.  Assume the dictionary d you pass in has
# 25, 10, 5, 1 as keys associated with integer values. It might be
# called like this:
#
# >>> dInit = {25: 0, 10: 0, 5: 0, 1: 0}
# >>> print( makeChange( dInit, 142 ) ) 
# {25: 5, 10: 1, 5: 1, 1: 2}

def makeChange( d, cash ):
   """Given coins with values of 25, 10, 5, 1, return a 
   dictionary that associates a count with each coin so that
   the total added matches cash and you added the minimum total
   number of coins.  You might assume that in the top-leval call of 
   makeChange d has value {25: 0, 10: 0, 5: 0, 1: 0}, but there's
   nothing that guarantees that."""
   
   if cash >= 25:
      d[25] += 1
      return makeChange(d,cash-25)
   if 10 <= cash < 25:
      d[10] += 1
      return makeChange(d,cash-10)
   if 5 <= cash < 10:
      d[5] += 1
      return makeChange(d,cash-5)
   if 1 <= cash < 5:
      d[1] += 1
      return makeChange(d,cash-1)
   if cash == 0:
      return d
       


# I posted a short video on the class webpage explaining 
# helper functions.  If you're stuck on this one, view
# that video and see if it helps.

def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex.
   Return the offset of the first uppercase letter;
   assume you are starting at index. Return -1 
   if there is none."""
   if s == "":
       return -1
   if 65 <= ord(s[0]) <= 90:
       return index
   else:
       return findFirstUppercaseIndexHelper( s[1:], index + 1)

# The following function is already completed for you. But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any. Return -1 if there is none. This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )
