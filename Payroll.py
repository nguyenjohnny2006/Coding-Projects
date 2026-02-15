# File: Payroll.py
# Student: Johnny Nguyen
# UT EID: jn28999
# Course Name: CS303E
#
# Date: 1-25-26
# Description of Program: finds employee paryoll from given pay minus any tax deductions

def main():
    
    name = input("Enter employee's name: ")
    hours = float(input("Enter number of hours worked in a week: "))
    payRate = float(input("Enter hourly pay rate: "))
    federalTax = float(input("Enter federal tax withholding rate: "))
    stateTax = float(input("Enter state tax withholding rate: "))

    grossPay = hours * payRate
    
    # Deductions calculations:
    federalWithholding = grossPay * federalTax
    stateWithholding = grossPay * stateTax
    totalDeduction = federalWithholding + stateWithholding

    # Net Pay
    netPay = grossPay - totalDeduction

    print()
    print("Employee Name:", name)
    print("Hours Worked:", format(hours,"0.1f"))
    print("Pay Rate: $", payRate, sep="")
    print("Gross Pay: $", format(grossPay,"0.2f"), sep="")
    print("Deductions:")
    print("  Federal Withholding (",format(federalTax,"0.1%"),"): $",format(federalWithholding,"0.2f"), sep="")
    print("  State Withholding (",format(stateTax,"0.1%"),"): $",format(stateWithholding,"0.2f"), sep="")
    print("  Total Deduction: $",format(totalDeduction,"0.2f"), sep="")
    print("Net Pay: $",format(netPay,"0.2f"),sep="")
    print()
    

main()

