# Assignment: HW5
# File: GradeStats.py
# Student: Johnny Nguyen
# UT EID: jn28999
# Course Name: CS303E
# 
# Date: 2-14-26
# Description of Program: Ask for grade inputs from user then return a series of stats.

def main():
    
    grade = float(input("Enter a grade or -1 to finish: "))
    maxNum = grade
    minNum = grade
    total = grade + 1
    i = 0
    if 0 <= grade < 70:
        f = 1
    else:
        f = 0
    if 70 <= grade:
        p = 1
    else:
        p = 0
    p = 0
    if grade == -1:
        print("No numbers entered.")
        return
    while grade != -1:
        grade = float(input("Enter a grade or -1 to finish: "))
        if grade >= maxNum:
            maxNum = grade
        if 0 <= grade <= minNum:
            minNum = grade
        i += 1
         #i is the number of values entered.
        total += grade
        # sum of all, then divide by i to get average
        if 0 <= grade <70:
            f += 1
        if 70 <= grade:
            p += 1
    print("")
    print("  Number of grades: ", format(i,"6.0f"))
    print("  Number failing:   ", format(f,"6.0f"))
    print("  Number passing:   ", format(p,"6.0f"))
    print("  Minimum grade:    ", format(minNum,"6.2f"))
    print("  Maximum grade:    ", format(maxNum,"6.2f"))
    print("  Average grade:    ", format((total/i), "6.2f"))
    print("")
     
main()
