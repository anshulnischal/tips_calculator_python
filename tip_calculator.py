print("Welcome to Tip Calculator App! ")
bill = float(input("What is the current total of your bill? $"))
tip = float(input("How much tip would you like to give in percent? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_split_person = total_bill / people
# final_amount = round (bill_split_person, 2)
final_amount = "{:.2f}".format(bil)
print(f"Each person should pay: ${final_amount}")