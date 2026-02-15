# File: ConvertUnits.py
# Student: Johnny Nguyen
# UT EID: jn28999
# Course Name: CS303E
#
# Date: 1-25-26
# Description of Program: find English and Metric unit conversions from input
# of feet and inches.

def main():
    inputFeet = float( input("Enter number of feet: "))
    inputInches = float( input("Enter number of inches: "))

    # find total inches from input
    inches = (inputFeet * 12) + inputInches

    # find total feet from input
    feet = (inputInches / 12) + inputFeet

    # find total yards from input
    yards = feet / 3

    # find total miles
    miles = feet / 5280

    # find meters
    meters = feet * 0.3048

    # find centimeters
    centimeters = meters * 100

    # find millimeters
    millimeters = centimeters * 10

    # find kilometers
    kilometers = meters / 1000

    print()
    print(inputFeet, "feet and", inputInches, "inches equals: ")
    print()
    print("English Units")
    print("  feet:", format(feet, "0.4f"))
    print("  inches:", format(inches, "0.4f"))
    print("  yards:", format(yards, "0.4f"))
    print("  miles:", format(miles, "0.4f"))
    print()
    print("Metric Units")
    print("  meters:", format(meters, "0.4f"))
    print("  centimeters:", format(centimeters, "0.4f"))
    print("  millimeters:", format(millimeters, "0.4f"))
    print("  kilometers:", format(kilometers, "0.4f"))
    print()
    

main()
