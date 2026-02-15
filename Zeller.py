# Assignment: HW4
# File: Zeller.py
# Student: Johnny Nguyen
# UTEID: jn28999
# Course Name: CS 303E
#
# Date: 2-2-26
# Description of Program: Zeller's Congruence translates a given date into its
# corresponding day of the week.


def main():
    year = int(input("Enter year (e.g., 2008): "))
    if not year > 1752:
        print("Year must be > 1752. Illegal year entered: ", year, sep="")
        return

    month = int(input("Enter month (1-12): "))
    if not (1 <= month <= 12):
        print("Month must be in [1..12]. Illegal month entered: ", month, sep="")
        return

    # Allow for illegal dates such as Feb 31
    day = int(input("Enter day: "))
    if not 1 <= day <= 31:
        print("Day must be in [1..31]. Illegal day entered: ", day, sep="")
        return

    if 1 <= month <= 2:
        m = month + 12
        y = year - 1
    elif 3<= month <= 12:
        m = month
        y = year
    
    k = y % 100
    j = y // 100
  
    h = ( day + (13 * (m + 1))//5 + k + k//4 + j//4 + 5*j ) % 7

    if h == 0:
        h = "Saturday"
    elif h == 1:
        h = "Sunday"
    elif h == 2:
        h = "Monday"
    elif h == 3:
        h = "Tuesday"
    elif h == 4:
        h = "Wednesday"
    elif h == 5:
        h = "Thursday"
    elif h == 6:
        h = "Friday"

    print("Day of the week is", h)
    
    
    
main()

    
