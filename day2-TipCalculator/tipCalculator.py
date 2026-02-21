totalBill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tipAsPercent = tip / 100
totalTipAmount = totalBill * tipAsPercent
totalBillWithTip = totalBill + totalTipAmount
billPerPerson = totalBillWithTip / people
finalAmount = round(billPerPerson, 2)
finalAmount = "{:.2f}".format(billPerPerson)

print(f"Each person should pay: ${finalAmount}")