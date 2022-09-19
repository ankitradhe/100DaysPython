print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
num = int(input("How many people to split the bill?"))
per = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
total_bill = bill + ((bill*per)/100)
share = total_bill/num
print("Each person should pay" + str(share))
