print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like give -- 10, 12 or 15? :"))
person = int(input("How many people to split the bill? :"))
percentage_tip = tip / 100
bill_with_tip = percentage_tip * bill + bill
bill_per_person = (round(bill_with_tip / person, 2))
print(f"Each person should pay: ${bill_per_person}")
