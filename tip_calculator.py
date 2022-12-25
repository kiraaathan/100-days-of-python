#Tip Calculator
bill = float(input("Enter the bill amount :"))
tip = int((input("How much tip would you like to give (10% , 15% , 20%) :")))
people = int(input("How many people to split the bill :"))
bill_with_tip = (((tip/100)*bill) + bill)/people
print(bill_with_tip)
# rounded_bill = round(bill_with_tip,2)
# str(rounded_bill)
formatted_bill = "{.:2f}".format(bill_with_tip)
print(f"Each person should pay {formatted_bill}")
