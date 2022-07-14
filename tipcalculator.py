print("Welcome to the tip calculator!\n")
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? ")
split_no = input("How many people to split the bill? ")

tip_amount = float(bill) * (float(tip)/100) #tip amount 
total_amount = float(bill) + tip_amount #total amount includind tip 
to_pay = total_amount/float(split_no) #total amount split amongst group 
print(f"Each person should pay: ${round(to_pay, 3)}")
