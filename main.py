print("Welcome to the tip calculator")

total = float(input("What was the total bill? $"))

tip = int(input(f"What percentage tip would you like to give? 20, 22? Or 25?  "))

group_size = int(input("How many people will split the bill? "))

bill_with_tip = tip / 100 * total + total

amount = bill_with_tip / group_size

final_amount ="{:.2f}".format(amount)

print(f"Each person should pay ${final_amount}")